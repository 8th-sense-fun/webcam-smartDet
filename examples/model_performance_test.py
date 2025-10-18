#!/usr/bin/env python3
"""
Model Performance Tester
Test and compare different YOLO models to help you choose the best one.
"""

import time
import cv2
import sys
import os

# Add the parent directory to path so we can import src modules
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from src.camera_handler import CameraHandler
from src.object_detector import ObjectDetector

def test_model_performance(model_path: str, test_frames: int = 100):
    """Test a YOLO model's performance."""
    print(f"\n🧪 Testing {model_path}...")
    
    # Initialize components
    camera = CameraHandler(camera_id=0)
    detector = ObjectDetector(model_path=model_path, confidence_threshold=0.5)
    
    if not camera.initialize_camera():
        print("❌ Failed to initialize camera")
        return None
    
    if not detector.load_model():
        print("❌ Failed to load model")
        camera.release()
        return None
    
    print(f"✅ Model loaded successfully")
    
    # Warm up (first few predictions are slower)
    print("🔥 Warming up model...")
    for _ in range(5):
        ret, frame = camera.read_frame()
        if ret:
            detector.detect_objects(frame)
    
    # Performance test
    print(f"⏱️ Testing performance over {test_frames} frames...")
    start_time = time.time()
    total_detections = 0
    
    for i in range(test_frames):
        ret, frame = camera.read_frame()
        if not ret:
            print("❌ Failed to read frame")
            break
            
        # Time individual detection
        detect_start = time.time()
        detections = detector.detect_objects(frame)
        detect_time = time.time() - detect_start
        
        total_detections += len(detections)
        
        if (i + 1) % 20 == 0:
            print(f"   Frame {i+1}/{test_frames} - {len(detections)} objects - {1/detect_time:.1f} FPS")
    
    total_time = time.time() - start_time
    fps = test_frames / total_time
    avg_detections = total_detections / test_frames
    
    camera.release()
    
    return {
        'model': model_path,
        'fps': fps,
        'avg_detections': avg_detections,
        'total_time': total_time
    }

def compare_all_models():
    """Compare all available YOLO models."""
    print("🎯 YOLO MODEL PERFORMANCE COMPARISON")
    print("=" * 50)
    
    # Check available models
    model_files = []
    models_dir = "models"
    
    for model in ['yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt']:
        model_path = os.path.join(models_dir, model)
        if os.path.exists(model_path):
            model_files.append(model_path)
        else:
            print(f"⚠️ {model} not found in models/ directory")
    
    if not model_files:
        print("❌ No model files found!")
        print("💡 Run: make setup  or download models manually")
        return
    
    print(f"📁 Found {len(model_files)} models to test")
    print("🚀 Starting performance tests...\n")
    
    results = []
    
    for model_path in model_files:
        try:
            result = test_model_performance(model_path, test_frames=50)
            if result:
                results.append(result)
                print(f"✅ {model_path}: {result['fps']:.1f} FPS, {result['avg_detections']:.1f} avg objects")
        except Exception as e:
            print(f"❌ Error testing {model_path}: {e}")
    
    # Display comparison
    if results:
        print("\n📊 PERFORMANCE COMPARISON:")
        print("-" * 70)
        print(f"{'Model':<15} {'FPS':<10} {'Avg Objects':<12} {'Speed Rating':<15}")
        print("-" * 70)
        
        # Sort by FPS (fastest first)
        results.sort(key=lambda x: x['fps'], reverse=True)
        
        for result in results:
            model_name = os.path.basename(result['model'])
            fps = result['fps']
            avg_obj = result['avg_detections']
            
            # Speed rating
            if fps >= 80:
                speed_rating = "🚀 Excellent"
            elif fps >= 50:
                speed_rating = "⚡ Great"  
            elif fps >= 30:
                speed_rating = "👍 Good"
            else:
                speed_rating = "🐌 Slow"
            
            print(f"{model_name:<15} {fps:<10.1f} {avg_obj:<12.1f} {speed_rating:<15}")
        
        print("\n💡 RECOMMENDATIONS:")
        print("-" * 30)
        fastest = results[0]
        print(f"🏃 Fastest: {os.path.basename(fastest['model'])} ({fastest['fps']:.1f} FPS)")
        
        if len(results) > 1:
            balanced = results[len(results)//2]
            print(f"⚖️ Balanced: {os.path.basename(balanced['model'])} ({balanced['fps']:.1f} FPS)")

def main():
    """Main function."""
    if len(sys.argv) > 1:
        model_path = sys.argv[1]
        print(f"🎯 Testing single model: {model_path}")
        result = test_model_performance(model_path, test_frames=100)
        if result:
            print(f"\n📊 Results:")
            print(f"   FPS: {result['fps']:.1f}")
            print(f"   Average objects per frame: {result['avg_detections']:.1f}")
    else:
        compare_all_models()

if __name__ == "__main__":
    main()
