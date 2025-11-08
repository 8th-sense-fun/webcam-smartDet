#!/usr/bin/env python3
"""
Combined Detection Demo
Demonstrates both object detection (YOLO) and face detection working together.
"""

import cv2
import logging
import sys
import os

# Add the parent directory to path so we can import src modules
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from src.camera_handler import CameraHandler
from src.object_detector import ObjectDetector
from src.face_detector import FaceDetector

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def combined_detection_demo():
    """Run combined object and face detection demo."""
    logger.info("Starting combined detection demo...")
    
    # Initialize components
    camera = CameraHandler(camera_id=0)
    object_detector = ObjectDetector(model_path="yolov8n.pt", confidence_threshold=0.5)
    face_detector = FaceDetector()
    
    # Initialize camera
    if not camera.initialize_camera():
        logger.error("Failed to initialize camera")
        return
    
    # Load YOLO model
    if not object_detector.load_model():
        logger.error("Failed to load YOLO model")
        camera.release()
        return
    
    logger.info("Combined detection demo initialized successfully. Press 'q' to quit.")
    
    try:
        frame_count = 0
        while True:
            # Read frame from camera
            ret, frame = camera.read_frame()
            if not ret:
                logger.warning("Failed to read frame from camera")
                break
            
            # Detect objects with YOLO (every 5 frames for performance)
            objects = []
            if frame_count % 5 == 0:
                objects = object_detector.detect_objects(frame)
                if objects:
                    frame = object_detector.draw_detections(frame, objects)
            
            # Detect faces (every frame for responsiveness)
            faces = face_detector.detect_faces(frame)
            if faces:
                frame = face_detector.draw_faces(frame, faces)
            
            # Add statistics
            stats_y = 30
            cv2.putText(frame, f'Objects: {len(objects)}', (10, stats_y), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            cv2.putText(frame, f'Faces: {len(faces)}', (10, stats_y + 25), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            cv2.putText(frame, 'Press Q to quit', (10, frame.shape[0] - 20), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
            
            # Display frame
            cv2.imshow('Combined Detection Demo', frame)
            
            # Check for quit
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # 'q' or ESC
                break
            
            frame_count += 1
            
            # Log status every 30 frames
            if frame_count % 30 == 0:
                logger.info(f"Frame {frame_count}: {len(objects)} objects, {len(faces)} faces")
    
    except KeyboardInterrupt:
        logger.info("Demo interrupted by user")
    
    finally:
        # Cleanup
        camera.release()
        cv2.destroyAllWindows()
        logger.info("Combined detection demo finished")


if __name__ == "__main__":
    combined_detection_demo()
