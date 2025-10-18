#!/usr/bin/env python3
"""
Quick Model Verification Test
Test that all YOLO models can be loaded by our application components.
"""

import sys
import os

# Add the parent directory to path so we can import src modules
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from src.object_detector import ObjectDetector
import numpy as np

def test_model_loading():
    """Test loading each YOLO model."""
    print("🧪 YOLO MODEL VERIFICATION TEST")
    print("=" * 50)
    
    # List of models to test
    models = ['yolov8n.pt', 'yolov8s.pt', 'yolov8m.pt', 'yolov8l.pt']
    
    # Create a dummy image for testing
    dummy_image = np.zeros((480, 640, 3), dtype=np.uint8)
    
    results = []
    
    for model_name in models:
        print(f"\n📝 Testing {model_name}...")
        
        try:
            # Initialize detector
            detector = ObjectDetector(model_path=model_name, confidence_threshold=0.5)
            
            # Load model
            if detector.load_model():
                print(f"✅ {model_name} loaded successfully!")
                
                # Test detection on dummy image
                detections = detector.detect_objects(dummy_image)
                print(f"   Detections on blank image: {len(detections)} (expected: 0)")
                
                results.append({
                    'model': model_name,
                    'status': 'SUCCESS',
                    'detections': len(detections)
                })
            else:
                print(f"❌ Failed to load {model_name}")
                results.append({
                    'model': model_name,
                    'status': 'FAILED',
                    'detections': -1
                })
                
        except Exception as e:
            print(f"❌ Error with {model_name}: {e}")
            results.append({
                'model': model_name,
                'status': 'ERROR',
                'detections': -1,
                'error': str(e)
            })
    
    # Summary
    print("\n📊 TEST RESULTS SUMMARY:")
    print("-" * 40)
    
    success_count = 0
    for result in results:
        status_icon = "✅" if result['status'] == 'SUCCESS' else "❌"
        print(f"{status_icon} {result['model']:<12} - {result['status']}")
        if result['status'] == 'SUCCESS':
            success_count += 1
    
    print(f"\n🎯 {success_count}/{len(models)} models working correctly!")
    
    if success_count == len(models):
        print("🎉 All models are ready to use!")
        print("\n💡 Try them with:")
        for model in models:
            print(f"   python main.py --model-path {model}")
    else:
        print("⚠️  Some models had issues. Check the errors above.")
    
    return results

if __name__ == "__main__":
    test_model_loading()
