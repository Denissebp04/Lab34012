import sys
import os

def get_environment_info():
    """Get information about the current Python environment."""
    
    # Get Python version
    python_version = sys.version.split()[0]
    
    # Get virtual environment path
    virtual_env = os.environ.get('VIRTUAL_ENV')
    
    # Get conda environment name
    conda_env = os.environ.get('CONDA_DEFAULT_ENV')
    
    print("\nPython Environment Information:")
    print("-" * 30)
    print(f"Python Version: {python_version}")
    print(f"Executable Path: {sys.executable}")
    
    if virtual_env:
        print(f"Virtual Environment: {os.path.basename(virtual_env)}")
    elif conda_env:
        print(f"Conda Environment: {conda_env}")
    else:
        print("No virtual environment activated")
    
    print("\nPython Path:")
    for path in sys.path:
        print(f"  - {path}")

if __name__ == "__main__":
    get_environment_info() 