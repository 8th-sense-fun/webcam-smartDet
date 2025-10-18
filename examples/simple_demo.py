#!/usr/bin/env python3
"""
Simple example demonstrating basic webcam object detection functionality.
This is a minimal example to test the setup.
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

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def simple_detection_demo():
    """Run a simple detection demo."""
    logger.info("Starting simple detection demo...")

    # Initialize camera and detector
    camera = CameraHandler(camera_id=0)
    detector = ObjectDetector(model_path="yolov8n.pt", confidence_threshold=0.5)

    # Initialize components
    if not camera.initialize_camera():
        logger.error("Failed to initialize camera")
        return

    if not detector.load_model():
        logger.error("Failed to load detection model")
        camera.release()
        return

    logger.info("Demo initialized successfully. Press 'q' to quit.")

    try:
        frame_count = 0
        while True:
            # Read frame
            ret, frame = camera.read_frame()
            if not ret:
                logger.warning("Failed to read frame")
                break

            # Detect objects every 5 frames (for better performance)
            if frame_count % 5 == 0:
                detections = detector.detect_objects(frame)
                if detections:
                    frame = detector.draw_detections(frame, detections)
                    logger.info(f"Frame {frame_count}: Found {len(detections)} objects")

            # Display frame
            cv2.imshow("Simple Detection Demo", frame)

            # Check for quit
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q") or key == 27:  # 'q' or ESC
                break

            frame_count += 1

    except KeyboardInterrupt:
        logger.info("Demo stopped by user")

    finally:
        # Cleanup
        camera.release()
        cv2.destroyAllWindows()
        logger.info("Demo finished")


if __name__ == "__main__":
    simple_detection_demo()
