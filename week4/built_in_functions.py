# Week 4 - Built In Functions


def ascii_value():
    # Activity 1: ASCII Value
    print("Program Started!")
    print("Please enter a standard character:")
    letter = input()

    # Check that exactly one character was entered
    if len(letter) == 1:
        # ord() gives the ASCII code for the character
        value = ord(letter)
        print(f"The ASCII code for {letter} is {value}.")
    else:
        print("Error: please enter a single character only.")

    print("Program Ended!")


def ascii_character():
    # Activity 2: ASCII Character
    print("Program Started!")
    print("Please enter an ASCII code:")
    # int() turns the text into a number, abs() removes any minus sign
    code = abs(int(input()))

    # Check the code is a printable character (32 to 126 inclusive)
    if code in range(32, 127):
        # chr() gives the character for the ASCII code
        character = chr(code)
        print(f"The character represented by the ASCII code {code} is {character}.")
    else:
        print("Error: please enter a number between 32 and 126.")

    print("Program Ended!")


# Only run when this file is executed directly
if __name__ == "__main__":
    ascii_value()
    print()
    ascii_character()

