import cv2
import numpy as np
from typing import Optional, Tuple
import logging

logger = logging.getLogger(__name__)


class CameraHandler:
    """Handle webcam operations and video streaming."""

    def __init__(self, camera_id: int = 0):
        """Initialize camera handler.

        Args:
            camera_id: Camera device ID (default: 0 for default camera)
        """
        self.camera_id = camera_id
        self.cap = None
        self.is_opened = False

    def initialize_camera(self) -> bool:
        """Initialize the webcam connection.

        Returns:
            bool: True if camera initialized successfully, False otherwise
        """
        try:
            self.cap = cv2.VideoCapture(self.camera_id)
            if not self.cap.isOpened():
                logger.error(f"Cannot open camera {self.camera_id}")
                return False

            # Set camera properties for better performance
            self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            self.cap.set(cv2.CAP_PROP_FPS, 30)

            self.is_opened = True
            logger.info(f"Camera {self.camera_id} initialized successfully")
            return True

        except Exception as e:
            logger.error(f"Error initializing camera: {e}")
            return False

    def read_frame(self) -> Tuple[bool, Optional[np.ndarray]]:
        """Read a frame from the camera.

        Returns:
            Tuple of (success_flag, frame_array)
        """
        if not self.is_opened or self.cap is None:
            return False, None

        ret, frame = self.cap.read()
        return ret, frame

    def release(self):
        """Release the camera resources."""
        if self.cap is not None:
            self.cap.release()
            self.is_opened = False
            logger.info("Camera released")

    def get_camera_info(self) -> dict:
        """Get camera properties information.

        Returns:
            dict: Camera properties
        """
        if not self.is_opened:
            return {}

        return {
            "width": int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            "height": int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)),
            "fps": int(self.cap.get(cv2.CAP_PROP_FPS)),
            "fourcc": int(self.cap.get(cv2.CAP_PROP_FOURCC)),
        }
