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


# Only run when this file is executed directly
if __name__ == "__main__":
    run_task1()
