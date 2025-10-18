#!/usr/bin/env python3
"""
Main entry point for the webcam smart detection application.
"""

import logging
import argparse
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from src.smart_detection_app import SmartDetectionApp


def setup_logging(log_level: str = "INFO"):
    """Setup logging configuration."""
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.StreamHandler(), logging.FileHandler("smart_detection.log")],
    )


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Webcam Smart Detection Application")
    parser.add_argument(
        "--camera-id", type=int, default=0, help="Camera device ID (default: 0)"
    )
    parser.add_argument(
        "--model-path",
        type=str,
        default="yolov8n.pt",
        help="Path to YOLO model file (default: yolov8n.pt). Available: yolov8n.pt (fastest), yolov8s.pt (balanced), yolov8m.pt (accurate), yolov8l.pt (most accurate)",
    )
    parser.add_argument(
        "--confidence",
        type=float,
        default=0.5,
        help="Confidence threshold for detections (default: 0.5)",
    )
    parser.add_argument(
        "--no-display", action="store_true", help="Run without displaying video window"
    )
    parser.add_argument("--save-output", type=str, help="Path to save output video")
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Logging level (default: INFO)",
    )

    args = parser.parse_args()

    # Setup logging
    setup_logging(args.log_level)
    logger = logging.getLogger(__name__)

    logger.info("Starting Webcam Smart Detection Application")
    logger.info(f"Camera ID: {args.camera_id}")
    logger.info(f"Model: {args.model_path}")
    logger.info(f"Confidence threshold: {args.confidence}")

    try:
        # Create and run the application
        app = SmartDetectionApp(
            camera_id=args.camera_id,
            model_path=args.model_path,
            confidence_threshold=args.confidence,
        )

        app.run(
            display_window=not args.no_display,
            save_output=bool(args.save_output),
            output_path=args.save_output,
        )

    except Exception as e:
        logger.error(f"Application error: {e}")
        sys.exit(1)

    logger.info("Application finished")


if __name__ == "__main__":
    main()
