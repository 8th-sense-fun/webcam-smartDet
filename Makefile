# Makefile for webcam-smartDet project

.PHONY: help install test run demo clean format lint setup examples models test-models download-models

# Default target
help:
	@echo "Available targets:"
	@echo "  setup      - Set up the development environment"
	@echo "  install    - Install project dependencies"
	@echo "  run        - Run the main application"
	@echo "  demo       - Run the simple demo"
	@echo "  test       - Run unit tests"
	@echo "  format     - Format code with black"
	@echo "  lint       - Run linting with flake8"
	@echo "  clean      - Clean up generated files"
	@echo "  examples   - Show available example scripts"
	@echo "  models     - Show available YOLO models"
	@echo "  test-models - Test performance of all models"
	@echo "  download-models - Download all YOLO models"
	@echo "  help       - Show this help message"

# Set up development environment
setup: install
	@echo "Development environment setup complete!"

# Install dependencies
install:
	pip install -r requirements.txt

# Run the main application
run:
	python main.py

# Run the simple demo
demo:
	python examples/simple_demo.py

# Run unit tests
test:
	python -m pytest tests/ -v

# Format code
format:
	black src/ tests/ *.py

# Lint code
lint:
	flake8 src/ tests/ *.py

# Clean up generated files
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.log" -delete
	rm -rf .pytest_cache/
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/

# Quick start - install and run demo
quickstart: install demo

# Show examples
examples:
	@echo "📁 Available examples:"
	@echo "  python examples/simple_demo.py             - Basic webcam detection demo"
	@echo "  python examples/compare_versions.py        - Compare main.py vs demo"
	@echo "  python examples/show_usage.py              - Show file usage during execution"
	@echo "  python examples/demo_tools.py              - Learn about Black and Flake8"
	@echo "  python examples/model_performance_test.py  - Test and compare YOLO models"
	@echo ""
	@echo "📚 See examples/README.md for detailed information"

# Test model performance
test-models:
	python examples/model_performance_test.py

# Show available models
models:
	@echo "🤖 Available YOLO models:"
	@ls -lh models/*.pt 2>/dev/null || echo "   No models found - run 'make download-models'"
	@echo ""
	@echo "📖 See models/README.md for model comparison guide"

# Download all YOLO models
download-models:
	@echo "📥 Downloading YOLO models..."
	@mkdir -p models
	curl -L -o models/yolov8n.pt https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8n.pt
	curl -L -o models/yolov8s.pt https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8s.pt
	curl -L -o models/yolov8m.pt https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8m.pt
	curl -L -o models/yolov8l.pt https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8l.pt
	@echo "✅ All models downloaded!"
