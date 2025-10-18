#!/usr/bin/env python3
"""
Demonstration script showing which files are used during execution
"""

import os
import sys
import logging


def show_file_usage():
    """Show which files are used during different phases"""

    print("🚀 FILE USAGE DURING EXECUTION:")
    print("=" * 50)

    print("\n📱 WHEN USER RUNS: python main.py")
    print("✅ Used during execution:")
    print("   • main.py - Entry point")
    print("   • src/*.py - Source code modules")
    print("   • config/settings.py - Configuration")
    print("   • .env (if exists) - Environment variables")
    print("   • yolov8n.pt - ML model weights")
    print("   • requirements.txt - Dependencies (already installed)")

    print("\n❌ NOT used during execution:")
    print("   • tests/ - Only for development")
    print("   • Makefile - Only for automation commands")
    print("   • .vscode/ - Only for IDE configuration")
    print("   • pyproject.toml - Only during build/install")
    print("   • .gitignore - Only for Git")

    print("\n🛠️ DURING DEVELOPMENT:")
    print("✅ Used by developers:")
    print("   • tests/ - Run with 'make test' or 'pytest'")
    print("   • Makefile - Run with 'make <command>'")
    print("   • pyproject.toml - Used by pip, black, pytest")
    print("   • .vscode/ - Used by VS Code IDE")

    print("\n🏗️ DURING BUILD/INSTALL:")
    print("✅ Used by build tools:")
    print("   • pyproject.toml - Package metadata & dependencies")
    print("   • requirements.txt - Dependency list")
    print("   • setup.sh - Initial setup script")

    # Show what's actually loaded in memory right now
    print("\n🧠 CURRENTLY LOADED IN MEMORY:")
    print("Modules loaded in this Python process:")
    for module_name in sorted(sys.modules.keys())[:10]:  # Show first 10
        if not module_name.startswith("_"):
            print(f"   • {module_name}")
    print("   ... and more")

    # Show environment variables being used
    print(f"\n🌍 ENVIRONMENT VARIABLES:")
    print(f"   • Python path: {sys.executable}")
    print(f"   • Working directory: {os.getcwd()}")
    if os.path.exists(".env"):
        print("   • .env file: FOUND (would be loaded)")
    else:
        print("   • .env file: NOT FOUND (using defaults)")


if __name__ == "__main__":
    show_file_usage()
