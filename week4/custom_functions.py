# Activity 1: Simple User Defined Function

def listen():
    # Ask the user for a sound
    print("What sound did you hear?")
    sound = input()
    print()
    print(f"That was a loud {sound}!")


# Call the function so it runs
listen()


# Activity 2: Nesting

def identify():
    # Ask the user what they can see
    print()
    print("What lies before us?")
    seen = input()
    print()
    # Decide how to react to what was seen
    if seen == "a large boulder":
        print("It's time to run!")
    else:
        print("We will be fine.")


# Call the function so it runs
identify()

