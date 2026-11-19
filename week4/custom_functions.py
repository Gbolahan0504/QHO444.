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


# Activity 3: Parameters

def escape_by(plan):
    # Check which escape plan was passed in
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("We cannot escape that way! The boulder is in the way!")


# Try three different escape plans
print()
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")


# Activity 4: Loop

def cross_bridge(steps):
    # Show a message for each step crossed
    for step in range(steps):
        print("Crossed step.")
    # Check whether the bridge was too long to cross safely
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep going!")


# Cross a short bridge, then a long one
print()
cross_bridge(3)
cross_bridge(6)


