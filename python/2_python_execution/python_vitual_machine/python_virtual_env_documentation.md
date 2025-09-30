# Python Virtual Environment Documentation

## Table of Contents

1. [Python Virtual Environment - Definitions and Characteristics](#python-virtual-environment---definitions-and-characteristics)
2. [Python Virtual Environment Operations](#python-virtual-environment-operations)
3. [Python Virtual Environment Methods](#python-virtual-environment-methods)
4. [Common Errors in Python Virtual Environment](#common-errors-in-python-virtual-environment)

---

## Python Virtual Environment - Definitions and Characteristics

### What is a Python Virtual Environment?

A Python virtual environment is an isolated Python environment that allows you to install packages and dependencies for a specific project without affecting the global Python installation or other projects. It creates a self-contained directory tree that includes a Python installation and additional packages.

### What is PVM (Python Virtual Machine)?

**PVM** stands for **Python Virtual Machine**. The PVM is always present as part of the Python system and is technically the last step of what is called the Python interpreter. It's the runtime engine that executes Python bytecode.

**Simple definition**: A machine that is built from software, not hardware.
[Real life example](https://tech.blog.aknin.name/2010/07/04/pythons-innards-for-my-wife/)

### Characteristics of Python Virtual Environments

#### 1. **Isolation**

- Each virtual environment has its own Python interpreter
- Separate package installations don't interfere with each other
- Different projects can use different versions of the same package

```bash
# Example: Two projects with different Django versions
project1/venv/  # Django 3.2
project2/venv/  # Django 4.1
```

#### 2. **Independence**

- Virtual environments are independent of the system Python
- Can be created, modified, and deleted without affecting other environments
- Portable across different systems

#### 3. **Project-Specific Dependencies**

- Each project maintains its own `requirements.txt` file
- Dependencies are installed only for that specific project
- Easy to replicate environments on different machines

#### 4. **Version Control**

- Can specify exact Python versions for each environment
- Helps maintain consistency across development, testing, and production
- Prevents version conflicts between projects

### Structure of a Virtual Environment

```tree
my_project/
├── venv/                    # Virtual environment directory
│   ├── bin/                # Executables (Linux/Mac)
│   │   ├── activate        # Activation script
│   │   ├── pip            # pip for this environment
│   │   └── python         # Python interpreter
│   ├── lib/               # Installed packages
│   │   └── python3.x/
│   │       └── site-packages/
│   ├── include/           # Header files
│   └── pyvenv.cfg        # Configuration file
├── src/                   # Project source code
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

### Benefits of Using Virtual Environments

1. **Dependency Management**: Keep project dependencies separate
2. **Version Control**: Use specific package versions per project
3. **Clean Development**: Avoid cluttering global Python installation
4. **Reproducibility**: Easily recreate environments on different machines
5. **Testing**: Test with different package versions safely
6. **Deployment**: Ensure production matches development environment

---

## Python Virtual Environment Operations

### 1. Creating Virtual Environments

#### Using `venv` (Python 3.3+, Recommended)

```bash
# Create a virtual environment with default Python version
python -m venv myproject_env

# Create with specific Python version (if multiple versions installed)
python3.9 -m venv myproject_env

# Create in a specific directory
python -m venv /path/to/myproject_env
```

#### Using `virtualenv` (Third-party tool)

```bash
# Install virtualenv first
pip install virtualenv

# Create virtual environment
virtualenv myproject_env

# Create with specific Python version
virtualenv --python=python3.8 myproject_env
virtualenv --python=/usr/bin/python3.9 myproject_env

# Create with system site packages
virtualenv --system-site-packages myproject_env
```

#### Using `conda` (Anaconda/Miniconda)

```bash
# Create environment with specific Python version
conda create --name myproject python=3.9

# Create environment with specific packages
conda create --name myproject python=3.9 numpy pandas matplotlib

# Create from environment file
conda env create -f environment.yml
```

### 2. Activating Virtual Environments

#### Linux/Mac Activation

```bash
# Using venv or virtualenv
source myproject_env/bin/activate

# Alternative syntax
. myproject_env/bin/activate

# Using conda
conda activate myproject
```

#### Windows Activation

```bash
# Command Prompt
myproject_env\Scripts\activate.bat

# PowerShell
myproject_env\Scripts\Activate.ps1

# Using conda
conda activate myproject
```

#### Verification of Activation

```bash
# Check which Python is being used
which python
# Output: /path/to/myproject_env/bin/python

# Check Python version
python --version

# Check pip location
which pip
# Output: /path/to/myproject_env/bin/pip

# List installed packages
pip list
```

### 3. Installing Packages in Virtual Environment

```bash
# Activate environment first
source myproject_env/bin/activate

# Install single package
pip install requests

# Install specific version
pip install Django==4.1.0

# Install from requirements file
pip install -r requirements.txt

# Install multiple packages
pip install numpy pandas matplotlib

# Install in development mode
pip install -e .

# Install from Git repository
pip install git+https://github.com/user/repo.git
```

### 4. Managing Dependencies

#### Creating Requirements File

```bash
# Generate requirements.txt with current packages
pip freeze > requirements.txt

# Generate with specific format
pip freeze --local > requirements.txt

# Example requirements.txt content
# Django==4.1.0
# requests==2.28.1
# numpy==1.23.0
```

#### Installing from Requirements

```bash
# Install all packages from requirements.txt
pip install -r requirements.txt

# Upgrade all packages
pip install -r requirements.txt --upgrade
```

### 5. Deactivating Virtual Environments

```bash
# Deactivate current environment (works for venv and virtualenv)
deactivate

# For conda environments
conda deactivate
```

### 6. Listing and Managing Environments

#### Using `venv`/`virtualenv`

```bash
# List environments (manual check of directories)
ls ~/venvs/  # If you store environments in ~/venvs/

# Check current environment
echo $VIRTUAL_ENV
```

#### Using `conda`

```bash
# List all conda environments
conda env list
conda info --envs

# Get current environment info
conda info

# Remove environment
conda env remove --name myproject
```

### 7. Removing Virtual Environments

```bash
# For venv/virtualenv - simply delete the directory
rm -rf myproject_env

# For conda environments
conda env remove --name myproject

# Remove with confirmation
conda env remove --name myproject --yes
```

---

## Python Virtual Environment Methods

### Best Practices and Methods

#### 1. Project Structure Method

```bash
# Recommended project structure
mkdir myproject
cd myproject

# Create virtual environment inside project
python -m venv venv

# Activate environment
source venv/bin/activate

# Install project dependencies
pip install -r requirements.txt

# Project structure:
# myproject/
# ├── venv/
# ├── src/
# ├── tests/
# ├── requirements.txt
# ├── setup.py
# └── README.md
```

#### 2. Centralized Environment Management

```bash
# Create a central directory for all virtual environments
mkdir ~/venvs

# Create environments in central location
python -m venv ~/venvs/project1
python -m venv ~/venvs/project2

# Create activation aliases in ~/.bashrc or ~/.zshrc
alias activate_project1="source ~/venvs/project1/bin/activate"
alias activate_project2="source ~/venvs/project2/bin/activate"
```

#### 3. Environment Naming Conventions

```bash
# Method 1: Project name + version
python -m venv myproject_v1
python -m venv myproject_v2

# Method 2: Project name + Python version
python -m venv myproject_py39
python -m venv myproject_py310

# Method 3: Descriptive names
python -m venv web_development
python -m venv data_analysis
python -m venv machine_learning
```

#### 4. Requirements Management Methods

##### Development vs Production Requirements

```bash
# Create separate requirement files
requirements/
├── base.txt          # Common requirements
├── development.txt   # Development-only packages
└── production.txt    # Production-only packages
```

**base.txt**:

```txt
Django==4.1.0
requests==2.28.1
psycopg2==2.9.0
```

**development.txt**:

```txt
-r base.txt
pytest==7.1.0
black==22.0.0
flake8==5.0.0
```

**production.txt**:

```txt
-r base.txt
gunicorn==20.1.0
```

##### Version Pinning Strategies

```bash
# Exact version pinning (most restrictive)
Django==4.1.0

# Compatible release (recommended)
Django~=4.1.0  # >=4.1.0, <4.2.0

# Minimum version
Django>=4.1.0

# Version range
Django>=4.0.0,<5.0.0
```

#### 5. Automation Methods

##### Using Makefile

```makefile
# Makefile
.PHONY: venv install test clean

venv:
 python -m venv venv
 source venv/bin/activate && pip install --upgrade pip

install: venv
 source venv/bin/activate && pip install -r requirements.txt

test:
 source venv/bin/activate && python -m pytest

clean:
 rm -rf venv
 find . -type d -name __pycache__ -delete
```

##### Using Shell Scripts

```bash
#!/bin/bash
# setup_env.sh

echo "Setting up virtual environment..."

# Create virtual environment
python -m venv venv

# Activate environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "Requirements installed successfully!"
else
    echo "No requirements.txt found"
fi

echo "Virtual environment setup complete!"
echo "To activate: source venv/bin/activate"
```

#### 6. Environment Variable Management

```bash
# Create .env file for environment variables
# .env
DEBUG=True
DATABASE_URL=postgresql://user:pass@localhost/dbname
SECRET_KEY=your-secret-key-here

# Load environment variables in Python
# Using python-dotenv package
pip install python-dotenv

# In your Python code
from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = os.getenv('DEBUG', False)
DATABASE_URL = os.getenv('DATABASE_URL')
```

---

## Common Errors in Python Virtual Environment

### 1. Activation Errors

#### Error: `command not found: activate`

**Problem:**

```bash
# Wrong activation command
activate
# bash: activate: command not found
```

**Solution:**

```bash
# Correct activation commands
# Linux/Mac:
source venv/bin/activate
# or
. venv/bin/activate

# Windows Command Prompt:
venv\Scripts\activate.bat

# Windows PowerShell:
venv\Scripts\Activate.ps1
```

#### Error: PowerShell Execution Policy

**Problem:**

```powershell
PS> venv\Scripts\Activate.ps1
# Execution of scripts is disabled on this system
```

**Solution:**

```powershell
# Temporarily allow script execution
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Or use alternative activation
venv\Scripts\activate.bat
```

### 2. Package Installation Errors

#### Error: Installing in Global Environment

**Problem:**

```bash
# Forgot to activate virtual environment
pip install django
# Installs in global Python instead of virtual environment
```

**Prevention:**

```bash
# Always verify environment before installing
echo $VIRTUAL_ENV  # Should show path to your venv
which pip         # Should point to venv/bin/pip

# Then install
pip install django
```

#### Error: Permission Denied

**Problem:**

```bash
pip install package_name
# ERROR: Could not install packages due to an EnvironmentError: [Errno 13] Permission denied
```

**Solution:**

```bash
# Don't use sudo with virtual environments
# Instead, ensure you're in the correct virtual environment
source venv/bin/activate
pip install package_name

# If still having issues, upgrade pip
pip install --upgrade pip
```

### 3. Path and Environment Errors

#### Error: Wrong Python Version

**Problem:**

```bash
# Created venv with wrong Python version
python2 -m venv myproject  # Creates Python 2 environment
```

**Solution:**

```bash
# Specify correct Python version
python3 -m venv myproject
# or
python3.9 -m venv myproject

# Verify Python version after activation
source myproject/bin/activate
python --version
```

#### Error: Virtual Environment Not Found

**Problem:**

```bash
source myproject/bin/activate
# bash: myproject/bin/activate: No such file or directory
```

**Solution:**

```bash
# Check if virtual environment exists
ls -la myproject/

# If not exists, create it
python -m venv myproject

# Check correct path structure
ls -la myproject/bin/  # Linux/Mac
dir myproject\Scripts\ # Windows
```

### 4. Dependency Conflicts

#### Error: Package Version Conflicts

**Problem:**

```bash
pip install package1 package2
# ERROR: package1 requires version X, but package2 requires version Y
```

**Solution:**

```bash
# Use pip-tools for dependency resolution
pip install pip-tools

# Create requirements.in with high-level dependencies
echo "django" > requirements.in
echo "requests" >> requirements.in

# Generate locked requirements.txt
pip-compile requirements.in

# Install from locked file
pip-sync requirements.txt
```

### 5. Environment Management Errors

#### Error: Multiple Active Environments

**Problem:**

```bash
# Activated multiple environments without deactivating
source env1/bin/activate
source env2/bin/activate  # This can cause confusion
```

**Solution:**

```bash
# Always deactivate before switching
deactivate
source env2/bin/activate

# Check current environment
echo $VIRTUAL_ENV
```

#### Error: Corrupted Virtual Environment

**Problem:**

```bash
source venv/bin/activate
python
# ImportError: No module named 'encodings'
```

**Solution:**

```bash
# Remove and recreate the environment
deactivate
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Prevention and Best Practices

#### 1. Use Environment Indicators

```bash
# Add to ~/.bashrc or ~/.zshrc
export PS1="(venv) $PS1"  # Show environment in prompt
```

#### 2. Automate Environment Setup

```bash
# Create setup script
#!/bin/bash
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

if [ -f "requirements.txt" ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
fi

echo "Environment ready!"
```

#### 3. Use .gitignore

```gitignore
# .gitignore
venv/
env/
ENV/
.venv/
.env
__pycache__/
*.pyc
```

---

## Summary

Python virtual environments are essential tools for managing project dependencies and maintaining clean, isolated development environments. Understanding how to create, manage, and troubleshoot virtual environments is crucial for Python development.

**Key Takeaways:**

- Always use virtual environments for Python projects
- Keep requirements.txt files updated and version-pinned
- Use consistent naming conventions and project structure
- Automate environment setup with scripts or Makefiles
- Be aware of platform-specific differences
- Always activate the environment before installing packages
- Document environment setup in project README files
