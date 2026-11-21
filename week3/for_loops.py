# Week 3 - For Loops


def display_mountains():
    # Activity 1: Simple Loop
    print("How many mountains should I display?")
    mountains = int(input())
    print()
    print("Displaying...")
    print()

    # Draw one mountain each time round the loop
    for count in range(mountains):
        print("     __")
        print("    /  \\_")
        print("   /^    \\")
        print("  /  ^    \\_")
        print("_/ ^ ^     ^\\")
        print()

    print("Done!")


def count_down():
    # Activity 2: Count Down
    print("How far are we from the target?")
    steps = int(input())
    print()

    # Count down from the number entered to 1
    for remaining in range(steps, 0, -1):
        print(f"{remaining} steps remaining")

    print()
    print("Target achieved!")


def adjust_brightness():
    # Activity 3: Range
    print("What level of brightness is required?")
    brightness = int(input())
    print()
    print("Adjusting brightness...")
    print()

    # Go up in even numbers from 2 to the level entered (+1 so it is included)
    for level in range(2, brightness + 1, 2):
        # Show one star for each level of brightness
        print("Brightness level: " + "*" * level)

    print()
    print("Complete!")


def show_characters():
    # Activity 4: Characters
    print("What word do you see?")
    word = input()
    print()
    print("Displaying index positions...")
    print()

    # Go through every index position in the word
    for position in range(0, len(word), 1):
        # Show the index number and the character at that position
        print(f"index {position}: {word[position]}")

    print()
    print("Done!")


def reverse_phrase():
    # Activity 5: Reverse Word
    print("What phrase do you want to see in reverse?")
    phrase = input()
    print()
    print("Reversing...")
    print()

    # Start with empty text and build the reversed phrase one character at a time
    reversed_phrase = ""

    # Go from the last index down to 0
    for position in range(len(phrase) - 1, -1, -1):
        reversed_phrase = reversed_phrase + phrase[position]

    print(f"The phrase is: {reversed_phrase}")


def print_letters():
    # Activity 6: Membership Operators
    print("What phrase do you want to print?")
    user_phrase = input()
    print()
    print("outputting...")
    print()
    print("The phrase is: ")

    # Take each character in the phrase one at a time and print it on its own line
    for letter in user_phrase:
        print(letter)


# Only run when this file is executed directly
if __name__ == "__main__":
    display_mountains()
    print()
    count_down()
    print()
    adjust_brightness()
    print()
    show_characters()
    print()
    reverse_phrase()
    print()
    print_letters()




