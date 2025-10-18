import numpy as np
import torch
from ultralytics import YOLO
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)


class ObjectDetector:
    """Handle object detection using YOLO model."""

    def __init__(
        self, model_path: str = "yolov8n.pt", confidence_threshold: float = 0.5
    ):
        """Initialize the object detector.

        Args:
            model_path: Path to YOLO model file
            confidence_threshold: Minimum confidence score for detections
        """
        self.model_path = model_path
        self.confidence_threshold = confidence_threshold
        self.model = None
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def load_model(self) -> bool:
        """Load the YOLO model.

        Returns:
            bool: True if model loaded successfully, False otherwise
        """
        try:
            self.model = YOLO(self.model_path)
            self.model.to(self.device)
            logger.info(f"Model loaded successfully on {self.device}")
            return True
        except Exception as e:
            logger.error(f"Error loading model: {e}")
            return False

    def detect_objects(self, frame: np.ndarray) -> List[Dict[str, Any]]:
        """Detect objects in a frame.

        Args:
            frame: Input image frame

        Returns:
            List of detection dictionaries containing bbox, confidence, and class info
        """
        if self.model is None:
            logger.error("Model not loaded. Call load_model() first.")
            return []

        try:
            # Run inference
            results = self.model(frame, conf=self.confidence_threshold)

            detections = []
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        # Extract detection information
                        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                        confidence = box.conf[0].cpu().numpy()
                        class_id = int(box.cls[0].cpu().numpy())
                        class_name = self.model.names[class_id]

                        detection = {
                            "bbox": [int(x1), int(y1), int(x2), int(y2)],
                            "confidence": float(confidence),
                            "class_id": class_id,
                            "class_name": class_name,
                        }
                        detections.append(detection)

            return detections

        except Exception as e:
            logger.error(f"Error during detection: {e}")
            return []

    def draw_detections(
        self, frame: np.ndarray, detections: List[Dict[str, Any]]
    ) -> np.ndarray:
        """Draw detection boxes and labels on frame.

        Args:
            frame: Input image frame
            detections: List of detection dictionaries

        Returns:
            Frame with drawn detections
        """
        import cv2

        for detection in detections:
            bbox = detection["bbox"]
            confidence = detection["confidence"]
            class_name = detection["class_name"]

            # Draw bounding box
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)

            # Draw label
            label = f"{class_name}: {confidence:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
            cv2.rectangle(
                frame,
                (bbox[0], bbox[1] - label_size[1] - 10),
                (bbox[0] + label_size[0], bbox[1]),
                (0, 255, 0),
                -1,
            )
            cv2.putText(
                frame,
                label,
                (bbox[0], bbox[1] - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0),
                2,
            )

        return frame
