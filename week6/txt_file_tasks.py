# Week 6 - Text Files
import os


# Activity 1: Current Working Directory

def cwd():
    # Get the path of the folder this program is running in
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    # Show each file in that folder
    for file in os.listdir(path):
        print(file)


def run():
    print("Processing...")
    cwd()


# Only run when this file is executed directly
if __name__ == "__main__":
    run()