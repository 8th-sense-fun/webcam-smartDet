# Configuration settings for webcam smart detection

# Camera settings
CAMERA_SETTINGS = {
    'default_camera_id': 0,
    'frame_width': 640,
    'frame_height': 480,
    'fps': 30
}

# Detection model settings
MODEL_SETTINGS = {
    'default_model': 'yolov8n.pt',
    'confidence_threshold': 0.5,
    'available_models': [
        'yolov8n.pt',  # Nano - fastest
        'yolov8s.pt',  # Small
        'yolov8m.pt',  # Medium
        'yolov8l.pt',  # Large
        'yolov8x.pt'   # Extra Large - most accurate
    ]
}

# Output settings
OUTPUT_SETTINGS = {
    'log_file': 'smart_detection.log',
    'default_output_format': 'XVID',
    'default_output_extension': '.avi'
}

# Display settings
DISPLAY_SETTINGS = {
    'window_name': 'Smart Detection',
    'quit_keys': ['q', 'Q', 'ESC'],  # Keys to quit the application
    'box_color': (0, 255, 0),  # Green
    'text_color': (0, 0, 0),   # Black
    'box_thickness': 2,
    'text_scale': 0.5,
    'text_thickness': 2
}
