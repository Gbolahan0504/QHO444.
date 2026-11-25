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
# Activity 2: Reading a File

def display_chars(file_path, chars):
    # Open the file and show only the first few characters
    with open(file_path) as file:
        print(f"The first {chars} characters are:")
        print(file.read(chars))


def display_line(file_path):
    # Open the file and show only the first line
    with open(file_path) as file:
        print("The first line is:")
        print(file.readline().strip())


def display_text(file_path):
    # Open the file and show all the text in it
    with open(file_path) as file:
        print("The full text is:")
        print(file.read())


def run_task2():
    # Call each function with the library file
    display_chars("library.txt", 5)
    print()
    display_line("library.txt")
    print()
    display_text("library.txt")


if __name__ == "__main__":
    run_task2()