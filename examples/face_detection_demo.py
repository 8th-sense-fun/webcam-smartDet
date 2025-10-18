#!/usr/bin/env python3
"""
Face Detection Demo
Demonstrates face detection functionality using webcam feed.
"""

import cv2
import logging
import sys
import os

# Add the parent directory to path so we can import src modules
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from src.camera_handler import CameraHandler
from src.face_detector import FaceDetector

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def face_detection_demo():
    """Run face detection demo."""
    logger.info("Starting face detection demo...")
    
    # Initialize components
    camera = CameraHandler(camera_id=0)
    face_detector = FaceDetector()
    
    # Initialize camera
    if not camera.initialize_camera():
        logger.error("Failed to initialize camera")
        return
    
    logger.info("Face detection demo initialized successfully. Press 'q' to quit.")
    
    try:
        frame_count = 0
        while True:
            # Read frame from camera
            ret, frame = camera.read_frame()
            if not ret:
                logger.warning("Failed to read frame from camera")
                break
            
            # Detect faces every frame (for real-time detection)
            faces = face_detector.detect_faces(frame)
            
            # Draw face bounding boxes
            if faces:
                frame = face_detector.draw_faces(frame, faces)
                if frame_count % 30 == 0:  # Log every 30 frames to avoid spam
                    logger.info(f"Detected {len(faces)} faces")
            
            # Add frame info
            cv2.putText(frame, f'Faces: {len(faces)}', (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, 'Press Q to quit', (10, frame.shape[0] - 20), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
            
            # Display frame
            cv2.imshow('Face Detection Demo', frame)
            
            # Check for quit
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q') or key == 27:  # 'q' or ESC
                break
            
            frame_count += 1
    
    except KeyboardInterrupt:
        logger.info("Demo interrupted by user")
    
    finally:
        # Cleanup
        camera.release()
        cv2.destroyAllWindows()
        logger.info("Face detection demo finished")


if __name__ == "__main__":
    face_detection_demo()
