# Week 5 - Lists


# Activity 1: Simple List

def directions():
    # Create a list of the moves available in the maze
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    # Send the list back to whoever called this function
    return steps


def run_task1():
    # Call directions() and print the list it returns
    print(directions())


# Activity 2: Indexing

def movements():
    # Each direction is followed by the number of steps to take
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run_task2():
    print("Moving...")
    # Store the returned list in a local variable
    path = movements()
    # Jump through the list two items at a time
    for i in range(0, len(path), 2):
        direction = path[i]      # even index holds the direction
        steps = path[i + 1]      # next index holds the step count
        print(f"{direction} for {steps} steps")


# Activity 3: Iterate

def menu():
    print("Please select a direction:")
    # Get the list of directions from Activity 1
    steps = directions()
    # Loop through each index so we can show the number next to each direction
    for index in range(len(steps)):
        direction = steps[index]
        print(f"{index}: {direction}")


def run_task3():
    # Show the menu of directions
    menu()




# Activity 4: Populate

def menu_and_input():
    print("Please select a direction:")
    # Get the list of directions from Activity 1
    steps = directions()
    # Show each direction with its index number
    for index in range(len(steps)):
        direction = steps[index]
        print(f"{index}: {direction}")
    # Read the user's choice as a whole number
    choice = int(input())
    # Send back the direction that matches the number chosen
    return steps[choice]


def run_task4():
    # Start with an empty list to hold the route
    route = []
    print("Working out escape route...")
    # Ask for a direction 5 times
    for i in range(5):
        direction = menu_and_input()
        route.append(direction)
    print(f"Escape route: {route}")


# Only run when this file is executed directly
if __name__ == "__main__":
    run_task4()


