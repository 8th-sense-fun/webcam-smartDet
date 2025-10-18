#!/bin/bash
# Quick setup script for webcam-smartDet

echo "🚀 Setting up webcam-smartDet project..."

# Check Python version
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "📍 Python version: $python_version"

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create directories for outputs
mkdir -p output_videos
mkdir -p logs

echo "✅ Setup complete!"
echo ""
echo "🎯 Quick start options:"
echo "  • Run demo: python simple_demo.py"
echo "  • Run main app: python main.py"
echo "  • Run with options: python main.py --help"
echo ""
echo "📁 Project structure created:"
echo "  • src/ - Source code"
echo "  • tests/ - Unit tests"  
echo "  • config/ - Configuration files"
echo "  • models/ - ML models (auto-populated)"
echo "  • output_videos/ - Saved videos"
echo ""
echo "🔧 Development commands:"
echo "  • make help - Show all available commands"
echo "  • make test - Run tests"
echo "  • make format - Format code"
