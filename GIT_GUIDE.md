# Git Version Control Guide 📚

## 🎯 **Git Workflow You Just Learned**

### **The Golden Rule:**
```
Working Directory → Staging Area → Local Repository → Remote Repository
     (edit)      →     (add)     →    (commit)     →      (push)
```

## 📋 **What We Just Did (Step by Step)**

### **✅ Step 1: Check Status**
```bash
git status          # See what changed
git diff filename   # See specific changes
```

### **✅ Step 2: Stage Changes** 
```bash
# Stage specific files (GOOD PRACTICE)
git add .gitignore requirements.txt    # Config files
git add src/ main.py                   # Source code  
git add tests/ examples/               # Tests & examples
git add README.md docs/                # Documentation

# Avoid: git add .  (stages everything, less control)
```

### **✅ Step 3: Commit with Good Message**
```bash
git commit -m "feat: Complete webcam smart detection system

- Add main application with CLI
- Implement YOLO object detection  
- Create examples and documentation
- Add comprehensive test suite

Features: Real-time detection, video recording, configurable parameters"
```

### **✅ Step 4: Push to Remote**
```bash
git push origin main
```

## 🏆 **Git Best Practices**

### **📝 Commit Messages (Follow Convention):**

**Format:**
```
type(scope): brief description

Detailed explanation of what and why
- Bullet points for multiple changes
- Include breaking changes if any
```

**Types:**
- `feat:` New feature
- `fix:` Bug fix  
- `docs:` Documentation
- `style:` Code formatting
- `refactor:` Code restructuring
- `test:` Adding tests
- `chore:` Maintenance tasks

**Examples:**
```bash
# Good ✅
git commit -m "feat: add YOLO model selection support"
git commit -m "fix: resolve camera initialization error on macOS"  
git commit -m "docs: update installation instructions"

# Bad ❌
git commit -m "update stuff"
git commit -m "fix bug"
git commit -m "changes"
```

### **📦 What to Include/Exclude:**

**✅ DO Include:**
- Source code (`src/`, `*.py`)
- Configuration files (`requirements.txt`, `pyproject.toml`)
- Documentation (`README.md`, docs)
- Tests (`tests/`)
- Build scripts (`Makefile`, `setup.sh`)

**❌ DON'T Include:**
- Large files (`*.pt` models > 100MB)
- Generated files (`__pycache__/`, `*.pyc`)
- Logs (`*.log`)
- Personal files (`.env`, IDE settings)
- Operating system files (`.DS_Store`)

### **🔄 Regular Workflow:**

**Daily Development:**
```bash
# 1. Start work session
git status                    # Check current state
git pull origin main         # Get latest changes

# 2. Make changes, then
git add specific_files       # Stage strategically  
git commit -m "type: description"  # Commit with good message

# 3. End of session
git push origin main         # Share your changes
```

## 🌟 **Advanced Git Commands You'll Need**

### **🔍 History and Information:**
```bash
git log --oneline           # See commit history
git log --graph --all       # Visual branch history
git show                    # Show last commit details
git blame filename          # See who changed each line
```

### **🔄 Undoing Changes:**
```bash
# Before staging
git restore filename        # Undo changes to file
git restore .              # Undo all changes

# After staging  
git restore --staged filename  # Unstage file
git reset HEAD filename     # Alternative unstage

# After committing
git commit --amend         # Fix last commit message
git reset --soft HEAD~1    # Undo last commit, keep changes
```

### **🌿 Branching (For Features):**
```bash
# Create and switch to new branch
git checkout -b feature/new-model-support
git switch -c feature/new-model-support  # Newer syntax

# Work on branch, then merge
git checkout main
git merge feature/new-model-support
git branch -d feature/new-model-support  # Delete branch
```

## 🎯 **Your Next Steps**

### **✅ Immediate Actions:**
1. **Configure Git globally:**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

2. **Set up your preferred editor:**
   ```bash
   git config --global core.editor "code --wait"  # VS Code
   ```

### **🔄 For Future Development:**

**When adding new features:**
```bash
git checkout -b feature/new-camera-support
# ... make changes ...
git add src/
git commit -m "feat: add support for multiple camera sources"
git push origin feature/new-camera-support
# Create Pull Request on GitHub
```

**When fixing bugs:**
```bash
git checkout -b fix/camera-permissions
# ... make changes ...  
git add specific_files
git commit -m "fix: resolve camera permission issues on Linux"
git push origin fix/camera-permissions
```

### **📊 Monitor Your Repository:**
```bash
git status              # Check what's changed
git log --oneline -10   # See last 10 commits
git remote -v          # See remote repositories
```

## 🚨 **Common Mistakes to Avoid**

1. **❌ Don't commit large files** (models, videos)
2. **❌ Don't use `git add .`** blindly  
3. **❌ Don't commit without reviewing** changes first
4. **❌ Don't use vague commit messages**
5. **❌ Don't work directly on main** for big features

## 🎉 **You're Now Set Up!**

Your repository is now:
- ✅ Properly organized with good structure
- ✅ Has comprehensive documentation  
- ✅ Excludes large files appropriately
- ✅ Uses professional commit messages
- ✅ Ready for collaborative development

**Happy coding!** 🚀
