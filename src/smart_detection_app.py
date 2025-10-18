import cv2
import logging
import time
from typing import Optional
from .camera_handler import CameraHandler
from .object_detector import ObjectDetector

logger = logging.getLogger(__name__)


class SmartDetectionApp:
    """Main application class for webcam smart detection."""

    def __init__(
        self,
        camera_id: int = 0,
        model_path: str = "yolov8n.pt",
        confidence_threshold: float = 0.5,
    ):
        """Initialize the smart detection application.

        Args:
            camera_id: Camera device ID
            model_path: Path to YOLO model file
            confidence_threshold: Minimum confidence score for detections
        """
        self.camera_handler = CameraHandler(camera_id)
        self.object_detector = ObjectDetector(model_path, confidence_threshold)
        self.running = False

    def initialize(self) -> bool:
        """Initialize camera and model.

        Returns:
            bool: True if initialization successful, False otherwise
        """
        logger.info("Initializing Smart Detection App...")

        # Initialize camera
        if not self.camera_handler.initialize_camera():
            logger.error("Failed to initialize camera")
            return False

        # Load detection model
        if not self.object_detector.load_model():
            logger.error("Failed to load detection model")
            return False

        logger.info("Smart Detection App initialized successfully")
        return True

    def run(
        self,
        display_window: bool = True,
        save_output: bool = False,
        output_path: Optional[str] = None,
    ):
        """Run the smart detection application.

        Args:
            display_window: Whether to display the video window
            save_output: Whether to save the output video
            output_path: Path to save output video (if save_output is True)
        """
        if not self.initialize():
            logger.error("Failed to initialize application")
            return

        self.running = True
        frame_count = 0
        start_time = time.time()

        # Video writer for saving output
        video_writer = None
        if save_output and output_path:
            camera_info = self.camera_handler.get_camera_info()
            fourcc = cv2.VideoWriter_fourcc(*"XVID")
            video_writer = cv2.VideoWriter(
                output_path,
                fourcc,
                camera_info.get("fps", 30),
                (camera_info.get("width", 640), camera_info.get("height", 480)),
            )

        try:
            while self.running:
                # Read frame from camera
                ret, frame = self.camera_handler.read_frame()
                if not ret:
                    logger.warning("Failed to read frame from camera")
                    break

                # Detect objects
                detections = self.object_detector.detect_objects(frame)

                # Draw detections on frame
                if detections:
                    frame = self.object_detector.draw_detections(frame, detections)
                    logger.info(f"Detected {len(detections)} objects")

                # Save frame if required
                if video_writer:
                    video_writer.write(frame)

                # Display frame
                if display_window:
                    cv2.imshow("Smart Detection", frame)

                    # Check for quit key
                    key = cv2.waitKey(1) & 0xFF
                    if key == ord("q") or key == 27:  # 'q' or ESC
                        break

                frame_count += 1

                # Log FPS every 30 frames
                if frame_count % 30 == 0:
                    elapsed_time = time.time() - start_time
                    fps = frame_count / elapsed_time
                    logger.info(f"FPS: {fps:.2f}")

        except KeyboardInterrupt:
            logger.info("Application stopped by user")

        finally:
            self.cleanup(video_writer)

    def cleanup(self, video_writer=None):
        """Clean up resources."""
        logger.info("Cleaning up resources...")

        self.running = False
        self.camera_handler.release()

        if video_writer:
            video_writer.release()

        cv2.destroyAllWindows()
        logger.info("Cleanup completed")

    def stop(self):
        """Stop the application."""
        self.running = False
