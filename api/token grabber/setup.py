
import os
import sys

def install_requirements():
    requirements = [
        "requests",  # Example requirement, you can add more here
        # Add more requirements separated by commas
    ]

    for requirement in requirements:
        print(f"Installing {requirement}...")
        os.system(f"pip install {requirement}")

def main():
    print("Welcome to Blitzed Installer!")
    print("Preparing to install requirements...")
    install_requirements()
    print("Installation complete. You may now open Blitzed!")

if __name__ == "__main__":
    main()
