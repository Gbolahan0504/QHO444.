# Week 2 - Multiple Conditions


def choose_route():
    # Ask the user for the type of adventure
    print("What type of adventure should I have?")
    adventure = input()

    # Choose a route based on the type of adventure
    if adventure == "scary" or adventure == "short":
        print("Entering the dark forest!")
    elif adventure == "safe" or adventure == "long":
        print("Taking the safe route!")
    else:
        print("Not sure which route to take.")


def check_creature():
    # Ask what was heard in the forest
    print("What did I hear?")
    heard = input()

    # Ask what was seen in the forest
    print("What did I see?")
    seen = input()

    # Decide whether the creature is scary
    if heard == "grrr" and seen == "two red eyes":
        print("There is a scary creature. I should get out of here!")
    else:
        print("I am a little scared but I will continue.")


# Only run when this file is executed directly
if __name__ == "__main__":
    choose_route()
    print()
    check_creature()
