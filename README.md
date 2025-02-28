# Python Virtual Environments Lab

This lab demonstrates how to create and manage Python virtual environments using three different methods:
1. venv (built-in Python module)
2. virtualenv (third-party package)
3. conda (Anaconda distribution)

## Prerequisites

- Python 3.x installed on your system
- pip (Python package installer)
- Anaconda or Miniconda (for conda examples)

## 1. Using venv (Built-in Module)

The `venv` module is included in Python standard library and is the recommended way to create virtual environments.

### Create a virtual environment
```bash
# Create a new virtual environment
python -m venv venv_example
```

### Activate the virtual environment

On macOS/Linux:
```bash
source venv_example/bin/activate
```

On Windows:
```bash
venv_example\Scripts\activate
```

### Deactivate the virtual environment
```bash
deactivate
```

## 2. Using virtualenv

`virtualenv` is a third-party tool that needs to be installed first.

### Install virtualenv
```bash
pip install virtualenv
```

### Create a virtual environment
```bash
virtualenv virtualenv_example
```

### Activate the virtual environment

On macOS/Linux:
```bash
source virtualenv_example/bin/activate
```

On Windows:
```bash
virtualenv_example\Scripts\activate
```

### Deactivate the virtual environment
```bash
deactivate
```

## 3. Using conda

Conda is a package manager and environment manager that comes with Anaconda distribution.

### Create a virtual environment
```bash
conda create --name conda_example python=3.9
```

### Activate the virtual environment
```bash
conda activate conda_example
```

### Deactivate the virtual environment
```bash
conda deactivate
```

## Working with Virtual Environments

Once your virtual environment is activated, you can:

1. Install packages using pip:
```bash
pip install package_name
```

2. List installed packages:
```bash
pip list
```

3. Create requirements.txt:
```bash
pip freeze > requirements.txt
```

4. Install packages from requirements.txt:
```bash
pip install -r requirements.txt
```

## Best Practices

1. Always activate your virtual environment before installing packages
2. Keep your requirements.txt up to date
3. Use different virtual environments for different projects
4. Name your virtual environments meaningfully
5. Add virtual environment directories to your .gitignore file

## Common Issues and Solutions

1. If activation fails, make sure you're using the correct activation command for your OS
2. If `python` command is not found, ensure Python is properly installed and added to PATH
3. For conda, if the command is not found, ensure Anaconda/Miniconda is properly installed and initialized

## Cleaning Up

To remove virtual environments:

1. venv/virtualenv: Simply delete the environment directory
2. conda: `conda env remove --name environment_name` # Lab34012
