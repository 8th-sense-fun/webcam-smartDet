#!/usr/bin/env python3
"""
Side-by-side comparison of main.py vs simple_demo.py
"""

def show_comparison():
    print("🆚 MAIN.PY vs SIMPLE_DEMO.PY")
    print("=" * 60)
    
    print("\n📱 RUNNING main.py:")
    print("✅ Basic usage:")
    print("   python main.py")
    print("   make run")
    print()
    print("✅ Advanced usage:")  
    print("   python main.py --camera-id 1")
    print("   python main.py --confidence 0.7")
    print("   python main.py --save-output my_video.avi")
    print("   python main.py --no-display --save-output headless.avi")
    print("   python main.py --log-level DEBUG")
    
    print("\n📱 RUNNING simple_demo.py:")
    print("✅ Only one way:")
    print("   python simple_demo.py")
    print("   make demo")
    print("❌ No options - everything is fixed!")
    
    print("\n🎯 WHEN TO USE EACH:")
    print("=" * 30)
    print("📚 Use simple_demo.py when:")
    print("   • Learning how the code works")
    print("   • Testing if camera works")
    print("   • Quick demonstration")
    print("   • You're new to the project")
    
    print("\n🏢 Use main.py when:")
    print("   • Production deployment") 
    print("   • Need to save videos")
    print("   • Different cameras/models")
    print("   • Headless server deployment")
    print("   • Professional logging needed")
    
    print("\n⚡ PERFORMANCE DIFFERENCE:")
    print("=" * 30)
    print("🐎 main.py:")
    print("   • Processes EVERY frame")
    print("   • Higher CPU usage")
    print("   • More accurate detection")
    print("   • Professional logging with FPS counter")
    
    print("\n🐌 simple_demo.py:")
    print("   • Processes every 5th frame")  
    print("   • Lower CPU usage")
    print("   • Good for testing/demo")
    print("   • Basic logging")

if __name__ == "__main__":
    show_comparison()
