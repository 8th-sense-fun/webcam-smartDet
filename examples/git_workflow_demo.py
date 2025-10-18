#!/usr/bin/env python3
"""
Git Workflow Demonstration
Visual explanation of add, commit, and push
"""

def demonstrate_git_workflow():
    print("🎯 GIT WORKFLOW: ADD → COMMIT → PUSH")
    print("=" * 60)
    
    print("\n📁 WORKING DIRECTORY (Your Local Files)")
    print("   ↓ You edit files here")
    print("   ↓ Files: main.py, src/camera_handler.py, README.md")
    print("   ↓")
    print("   ↓ git add <files>  ← STAGE FILES")
    print("   ↓")
    
    print("📦 STAGING AREA (Git Index)")
    print("   ↓ Files ready to be committed")
    print("   ↓ Like a 'shopping cart' before checkout")
    print("   ↓")
    print("   ↓ git commit -m 'message'  ← SAVE SNAPSHOT")
    print("   ↓")
    
    print("🏛️ LOCAL REPOSITORY (.git folder)")
    print("   ↓ Permanent record of changes")
    print("   ↓ History of all commits stored locally")
    print("   ↓")
    print("   ↓ git push origin main  ← UPLOAD TO REMOTE")
    print("   ↓")
    
    print("☁️ REMOTE REPOSITORY (GitHub)")
    print("   ↓ Shared with the world")
    print("   ↓ Backup and collaboration")
    
    print("\n" + "=" * 60)
    print("🔑 KEY INSIGHT: Each step serves a different purpose!")

if __name__ == "__main__":
    demonstrate_git_workflow()
