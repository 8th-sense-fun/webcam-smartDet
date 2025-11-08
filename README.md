# Webcam Smart Detection

Python scripts to streamline videos from connected cameras and using ML model to detect and label objects in real time.

## Features

- 🎥 **Real-time webcam capture** - Stream video from any connected camera
- 🤖 **AI-powered object detection** - Using YOLO v8 for accurate and fast detection
- 👤 **Face detection** - Real-time face detection using OpenCV Haar Cascades
- 🏷️ **Real-time labeling** - Automatically label detected objects with confidence scores
- 🔄 **Combined detection** - Run both object and face detection simultaneously
- 💾 **Video recording** - Save detection results to video files
- ⚙️ **Configurable settings** - Customize detection parameters and camera settings
- 🖥️ **Command-line interface** - Easy to use CLI with various options

## Installation

### Prerequisites

- Python 3.8 or higher
- Webcam or camera device
- CUDA-compatible GPU (optional, for better performance)

### Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd webcam-smartDet
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download YOLO model (optional):**
   The application will automatically download the default YOLOv8n model on first run. For other models:
   ```bash
   # Download other YOLO models manually if needed
   wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s.pt
   ```

## Quick Start

### Try the Demo First
If you're new to this project, start with the simple demo:
```bash
python examples/simple_demo.py
# OR
make demo
```

### Face Detection Demos
Try the face detection features:
```bash
# Face detection only
python examples/face_detection_demo.py

# Combined object and face detection
python examples/combined_detection_demo.py
```

## Usage

### Basic Usage

Run the application with default settings:
```bash
python main.py
```

### Advanced Usage

```bash
# Use specific camera
python main.py --camera-id 1

# Use different YOLO model
python main.py --model-path yolov8s.pt

# Set confidence threshold
python main.py --confidence 0.7

# Save output video
python main.py --save-output output_video.avi

# Run without display (headless mode)
python main.py --no-display --save-output output.avi

# Set logging level
python main.py --log-level DEBUG
```

### Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--camera-id` | Camera device ID | 0 |
| `--model-path` | Path to YOLO model file | yolov8n.pt |
| `--confidence` | Confidence threshold for detections | 0.5 |
| `--save-output` | Path to save output video | None |
| `--no-display` | Run without displaying video window | False |
| `--log-level` | Logging level (DEBUG, INFO, WARNING, ERROR) | INFO |

### Controls

- Press `q` or `ESC` to quit the application
- Press `Ctrl+C` in terminal to stop

## Project Structure

```
webcam-smartDet/
├── src/                          # Source code
│   ├── __init__.py
│   ├── camera_handler.py         # Camera operations
│   ├── object_detector.py        # YOLO-based detection
│   ├── face_detector.py          # Face detection using OpenCV
│   └── smart_detection_app.py    # Main application class
├── tests/                        # Unit tests
│   └── test_camera_handler.py
├── config/                       # Configuration files
│   └── settings.py
├── examples/                     # Demo scripts and examples
│   ├── simple_demo.py           # Basic demo
│   ├── face_detection_demo.py   # Face detection demo
│   ├── combined_detection_demo.py # Combined object + face detection
│   ├── compare_versions.py      # Compare main vs demo
│   └── README.md                # Examples documentation
├── models/                       # Model files (auto-created)
├── main.py                       # Entry point
├── requirements.txt              # Python dependencies
├── pyproject.toml               # Project configuration
└── README.md                    # This file
```

## Configuration

Edit `config/settings.py` to customize:

- Camera settings (resolution, FPS)
- Detection model settings
- Display settings (colors, box thickness)
- Output settings

## Development

### Running Tests

```bash
python -m pytest tests/
```

### Code Formatting

```bash
black src/ tests/
```

### Linting

```bash
flake8 src/ tests/
```

## Supported Models

- YOLOv8n (Nano) - Fastest, lowest accuracy
- YOLOv8s (Small) - Balanced speed and accuracy
- YOLOv8m (Medium) - Good accuracy
- YOLOv8l (Large) - High accuracy
- YOLOv8x (Extra Large) - Highest accuracy, slowest

## Troubleshooting

### Common Issues

1. **Camera not detected:**
   - Check camera permissions
   - Try different camera IDs (0, 1, 2, etc.)
   - Ensure camera is not being used by another application

2. **Low FPS:**
   - Use a smaller YOLO model (yolov8n.pt)
   - Lower camera resolution in config
   - Use GPU acceleration if available

3. **Import errors:**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

### Performance Tips

- Use GPU acceleration for better performance
- Lower confidence threshold may increase detections but reduce precision
- Adjust camera resolution based on your needs
- Use appropriate YOLO model size for your hardware

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if needed
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8
- [OpenCV](https://opencv.org/) for computer vision operations
