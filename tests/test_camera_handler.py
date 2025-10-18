import unittest
import numpy as np
from unittest.mock import Mock, patch
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from src.camera_handler import CameraHandler


class TestCameraHandler(unittest.TestCase):
    """Test cases for CameraHandler class."""

    def setUp(self):
        """Set up test fixtures."""
        self.camera_handler = CameraHandler(camera_id=0)

    def tearDown(self):
        """Clean up after tests."""
        if hasattr(self.camera_handler, "cap") and self.camera_handler.cap:
            self.camera_handler.release()

    @patch("cv2.VideoCapture")
    def test_initialize_camera_success(self, mock_video_capture):
        """Test successful camera initialization."""
        # Mock successful camera initialization
        mock_cap = Mock()
        mock_cap.isOpened.return_value = True
        mock_video_capture.return_value = mock_cap

        result = self.camera_handler.initialize_camera()

        self.assertTrue(result)
        self.assertTrue(self.camera_handler.is_opened)
        mock_video_capture.assert_called_once_with(0)

    @patch("cv2.VideoCapture")
    def test_initialize_camera_failure(self, mock_video_capture):
        """Test camera initialization failure."""
        # Mock failed camera initialization
        mock_cap = Mock()
        mock_cap.isOpened.return_value = False
        mock_video_capture.return_value = mock_cap

        result = self.camera_handler.initialize_camera()

        self.assertFalse(result)
        self.assertFalse(self.camera_handler.is_opened)

    def test_read_frame_without_initialization(self):
        """Test reading frame without camera initialization."""
        ret, frame = self.camera_handler.read_frame()

        self.assertFalse(ret)
        self.assertIsNone(frame)

    @patch("cv2.VideoCapture")
    def test_read_frame_success(self, mock_video_capture):
        """Test successful frame reading."""
        # Setup mock
        mock_cap = Mock()
        mock_cap.isOpened.return_value = True
        mock_cap.read.return_value = (True, np.zeros((480, 640, 3), dtype=np.uint8))
        mock_video_capture.return_value = mock_cap

        # Initialize camera and read frame
        self.camera_handler.initialize_camera()
        ret, frame = self.camera_handler.read_frame()

        self.assertTrue(ret)
        self.assertIsNotNone(frame)
        self.assertEqual(frame.shape, (480, 640, 3))

    @patch("cv2.VideoCapture")
    def test_get_camera_info(self, mock_video_capture):
        """Test getting camera information."""
        # Setup mock
        mock_cap = Mock()
        mock_cap.isOpened.return_value = True
        mock_cap.get.side_effect = lambda prop: {
            "cv2.CAP_PROP_FRAME_WIDTH": 640,
            "cv2.CAP_PROP_FRAME_HEIGHT": 480,
            "cv2.CAP_PROP_FPS": 30,
            "cv2.CAP_PROP_FOURCC": 1234,
        }.get(str(prop), 0)
        mock_video_capture.return_value = mock_cap

        # Initialize camera and get info
        self.camera_handler.initialize_camera()
        info = self.camera_handler.get_camera_info()

        self.assertIsInstance(info, dict)
        self.assertIn("width", info)
        self.assertIn("height", info)
        self.assertIn("fps", info)
        self.assertIn("fourcc", info)


if __name__ == "__main__":
    unittest.main()
