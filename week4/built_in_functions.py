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
