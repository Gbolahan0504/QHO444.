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


# Activity 5: Multiple Parameters

def climb_ladder(remaining, crossed):
    # Compare the steps still to climb with the steps already climbed
    if remaining > crossed:
        print("Still some way to go!")
    else:
        print("We are almost there!")


# Check progress at two points on the ladder
print()
climb_ladder(5, 2)
climb_ladder(2, 5)


# Activity 1: Multiple User Defined Functions

def display_ladder(steps):
    # Draw the first side rail
    print("| |")
    # Add a rung and another rail for each step
    for step in range(steps):
        print("***")
        print("| |")


def create_ladder():
    # Ask how many steps the ladder needs
    print()
    print("How many steps remain?")
    steps = int(input())
    print()
    # Pass the number of steps to the drawing function
    display_ladder(steps)


# Call the second function, which calls the first one
create_ladder()


# Activity 2: Return Values

def sum_weights(person, inventory):
    # Add the two weights and send back the total
    return person + inventory


def calc_avg_weight(person, inventory):
    # Reuse sum_weights to get the total, then divide by the 2 items
    total = sum_weights(person, inventory)
    return total / 2


def run():
    print()
    print("What is the weight of the person?")
    person = int(input())
    print()
    print("What is the weight of their inventory?")
    inventory = int(input())
    print()
    print("What would you like to calculate (sum or average)?")
    choice = input()
    print()
    # Show the result the user asked for
    if choice == "sum":
        print(f"The sum of weights is {sum_weights(person, inventory)}.")
    elif choice == "average":
        print(f"The average weight is {calc_avg_weight(person, inventory)}.")


# Run the program
run()






