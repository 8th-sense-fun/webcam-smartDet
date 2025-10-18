# YOLO Model Comparison Guide

This directory contains different YOLO v8 models. Choose the right one based on your needs!

## 📊 **Model Comparison Table**

| Model | File Size | Speed | Accuracy | CPU Usage | Use Case |
|-------|-----------|-------|----------|-----------|----------|
| **YOLOv8n** | ~6MB | ⚡⚡⚡⚡⚡ Fastest | ⭐⭐⭐ Basic | 🔥 Low | Learning, Testing |
| **YOLOv8s** | ~22MB | ⚡⚡⚡⚡ Fast | ⭐⭐⭐⭐ Good | 🔥🔥 Medium | General Use |
| **YOLOv8m** | ~50MB | ⚡⚡⚡ Medium | ⭐⭐⭐⭐⭐ Great | 🔥🔥🔥 High | Professional |
| **YOLOv8l** | ~88MB | ⚡⚡ Slower | ⭐⭐⭐⭐⭐⭐ Excellent | 🔥🔥🔥🔥 Very High | High Precision |

## 🎯 **Which Model Should You Choose?**

### **🚀 YOLOv8n (Nano) - Best for Beginners**
```bash
python main.py --model-path models/yolov8n.pt
```
**Perfect for:**
- 📚 Learning and experimentation
- 💻 Older/slower computers
- 🎥 Real-time webcam (30+ FPS)
- 🔋 Battery-powered devices

**Specifications:**
- Size: ~6MB
- Speed: ~100 FPS on modern CPU
- mAP: 37.3% (COCO dataset)

### **⚖️ YOLOv8s (Small) - Best Balance**
```bash
python main.py --model-path models/yolov8s.pt
```
**Perfect for:**
- 🏠 Home security systems
- 🎮 Hobby projects
- 💼 Small business applications
- 📱 Mobile applications

**Specifications:**
- Size: ~22MB  
- Speed: ~80 FPS on modern CPU
- mAP: 44.9% (COCO dataset)

### **🏢 YOLOv8m (Medium) - Professional Grade**
```bash
python main.py --model-path models/yolov8m.pt
```
**Perfect for:**
- 🏭 Industrial applications
- 🚗 Automotive systems
- 🏥 Medical imaging
- 📹 Professional video analysis

**Specifications:**
- Size: ~50MB
- Speed: ~50 FPS on modern CPU
- mAP: 50.2% (COCO dataset)

### **🎯 YOLOv8l (Large) - Maximum Accuracy**
```bash
python main.py --model-path models/yolov8l.pt
```
**Perfect for:**
- 🔬 Research applications
- 🛡️ Critical security systems
- 📊 Data analysis projects
- 🎯 When accuracy is paramount

**Specifications:**
- Size: ~88MB
- Speed: ~30 FPS on modern CPU
- mAP: 52.9% (COCO dataset)

## 🖥️ **Hardware Recommendations**

### **💻 For Laptop/Desktop:**
- **Basic (Intel i3, 8GB RAM)**: Use YOLOv8n
- **Mid-range (Intel i5, 16GB RAM)**: Use YOLOv8s or YOLOv8m
- **High-end (Intel i7+, 32GB RAM)**: Any model
- **With GPU (NVIDIA)**: Any model with excellent performance

### **📱 For Embedded/Mobile:**
- **Raspberry Pi 4**: YOLOv8n only
- **Jetson Nano**: YOLOv8n or YOLOv8s
- **Mobile phones**: YOLOv8n recommended

## 🧪 **Testing Different Models**

Try each model and see the difference:

```bash
# Test Nano (fastest)
python main.py --model-path models/yolov8n.pt --log-level INFO

# Test Small (balanced)
python main.py --model-path models/yolov8s.pt --log-level INFO

# Test Medium (accurate)
python main.py --model-path models/yolov8m.pt --log-level INFO

# Test Large (most accurate)
python main.py --model-path models/yolov8l.pt --log-level INFO
```

## 📈 **Performance Benchmarks**

### **FPS (Frames Per Second) on Intel i7-10750H:**
- YOLOv8n: ~120 FPS
- YOLOv8s: ~85 FPS  
- YOLOv8m: ~55 FPS
- YOLOv8l: ~35 FPS

### **Detection Quality:**
- YOLOv8n: Good for obvious objects
- YOLOv8s: Good for most use cases
- YOLOv8m: Great for professional use
- YOLOv8l: Excellent for critical applications

## 🔧 **Optimization Tips**

1. **For Real-time Performance:**
   - Use YOLOv8n or YOLOv8s
   - Lower camera resolution
   - Process every N frames (like in simple_demo.py)

2. **For Maximum Accuracy:**
   - Use YOLOv8l or YOLOv8m
   - Higher confidence threshold (0.7+)
   - Process every frame

3. **For Recording/Analysis:**
   - Any model works
   - Higher resolution input
   - Save with `--save-output`

## 📝 **Model Files**

All models detect the same 80 object classes from COCO dataset:
- People, vehicles, animals
- Furniture, electronics
- Sports items, food items
- And much more!

The difference is in **speed** and **accuracy**, not in what they can detect.

## 🚀 **Quick Start Recommendations**

1. **New to YOLO?** Start with YOLOv8n
2. **Building an app?** Use YOLOv8s  
3. **Professional project?** Use YOLOv8m
4. **Research/Critical?** Use YOLOv8l

Happy detecting! 🎯
