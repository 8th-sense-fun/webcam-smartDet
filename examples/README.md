# Examples and Demo Scripts

This folder contains auxiliary scripts and examples for learning and demonstrating the webcam smart detection functionality.

## 📁 Files in this folder:

### **🎯 Demo Scripts**
- **`simple_demo.py`** - Basic webcam detection demo
  - Minimal example for learning
  - Processes every 5th frame for performance
  - Good starting point for beginners
  - Run with: `python examples/simple_demo.py` or `make demo`

- **`face_detection_demo.py`** - Face detection demo
  - Real-time face detection using OpenCV Haar Cascades
  - Draws bounding boxes around detected faces
  - Run with: `python examples/face_detection_demo.py`

- **`combined_detection_demo.py`** - Combined object and face detection
  - Runs both YOLO object detection and face detection simultaneously
  - Shows the power of multiple AI models working together
  - Run with: `python examples/combined_detection_demo.py`

### **📊 Comparison & Analysis**
- **`compare_versions.py`** - Shows differences between main.py and simple_demo.py
  - Educational tool to understand the architecture
  - Run with: `python examples/compare_versions.py`

- **`show_usage.py`** - Demonstrates which files are used during execution
  - Shows runtime vs development file usage
  - Run with: `python examples/show_usage.py`

### **🛠️ Development Tools Demo**
- **`demo_tools.py`** - Explains Black and Flake8 tools
  - Educational script about code quality tools
  - Run with: `python examples/demo_tools.py`

## 🚀 Quick Start

If you're new to this project, start here:

1. **Learn the basics:**
   ```bash
   python examples/simple_demo.py
   ```

2. **Try face detection:**
   ```bash
   python examples/face_detection_demo.py
   ```

3. **Try combined detection:**
   ```bash
   python examples/combined_detection_demo.py
   ```

4. **Understand the differences:**
   ```bash
   python examples/compare_versions.py
   ```

5. **See the development tools:**
   ```bash
   python examples/demo_tools.py
   ```

6. **Understand file usage:**
   ```bash
   python examples/show_usage.py
   ```

## 🎓 Learning Path

1. **Start with `simple_demo.py`** - See basic functionality
2. **Run `compare_versions.py`** - Understand main vs demo
3. **Try the main application** - `python main.py --help`
4. **Explore development tools** - `make format`, `make lint`, `make test`

These examples are separate from the main application to keep the project structure clean and organized!
