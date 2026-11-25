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
# Activity 4: Writing to a File

def search_books(file_path):
    print("Searching...", end="")
    # Two pieces of text to sort the lines into
    sections = ""
    books = "Books:\n"
    with open(file_path) as file:
        for line in file:
            # Remove the hidden new-line character from the end
            line = line.strip()
            # Lines starting with "Section" are sections, the rest are books
            if line.startswith("Section"):
                sections = sections + line + "\n"
            else:
                books = books + line + "\n"
    print("Done!")
    # Join the two pieces with two new lines between them
    return f"{sections}\n\n{books}"


def save(file_path, data):
    print("Saving...", end="")
    # "w" opens the file for writing (it is created if it does not exist)
    with open(file_path, "w") as file:
        file.write(data)
    print("Done!")


def run_task4():
    # Sort the books, then save the result to a new file
    data = search_books("books.txt")
    save("section-books.txt", data)


# Activity 3: Reading a File line by line

def search(file_path):
    print("Searching...")
    # Open the file and go through it one line at a time
    with open(file_path) as file:
        for line in file:
            print(f"Looked in {line.strip()}")
    print("...Done!")


def run_task3():
    # Search through the library sections
    search("library.txt")


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
    run_task4()
