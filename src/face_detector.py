import cv2
import numpy as np
from typing import List, Tuple, Dict, Any
import logging

logger = logging.getLogger(__name__)


class FaceDetector:
    """Face detection using OpenCV Haar Cascades."""
    
    def __init__(self):
        """Initialize the face detector."""
        try:
            # Load the face detection classifier
            self.face_cascade = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
            
            if self.face_cascade.empty():
                raise RuntimeError("Could not load face cascade classifier")
                
            logger.info("Face detector initialized successfully")
            
        except Exception as e:
            logger.error(f"Error initializing face detector: {e}")
            raise
    
    def detect_faces(self, frame: np.ndarray) -> List[Dict[str, Any]]:
        """
        Detect faces in the given frame.
        
        Args:
            frame: Input image frame
            
        Returns:
            List of face detection dictionaries containing bbox and confidence info
        """
        if frame is None:
            return []
        
        try:
            # Convert to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = self.face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
            
            # Convert to our standard format
            detections = []
            for (x, y, w, h) in faces:
                detection = {
                    'bbox': [int(x), int(y), int(x + w), int(y + h)],
                    'confidence': 0.9,  # Haar cascades don't provide confidence scores
                    'class_id': 0,  # Face class
                    'class_name': 'face'
                }
                detections.append(detection)
            
            return detections
            
        except Exception as e:
            logger.error(f"Error during face detection: {e}")
            return []
    
    def draw_faces(self, frame: np.ndarray, faces: List[Dict[str, Any]]) -> np.ndarray:
        """
        Draw bounding boxes around detected faces.
        
        Args:
            frame: Input image frame
            faces: List of face detection dictionaries
            
        Returns:
            Frame with drawn face bounding boxes
        """
        for face in faces:
            bbox = face['bbox']
            confidence = face['confidence']
            class_name = face['class_name']
            
            # Draw bounding box
            cv2.rectangle(frame, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (255, 0, 0), 2)
            
            # Draw label
            label = f"{class_name}: {confidence:.2f}"
            label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)[0]
            cv2.rectangle(frame, (bbox[0], bbox[1] - label_size[1] - 10), 
                         (bbox[0] + label_size[0], bbox[1]), (255, 0, 0), -1)
            cv2.putText(frame, label, (bbox[0], bbox[1] - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        
        return frame
