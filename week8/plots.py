# Week 8 - Plots
import matplotlib.pyplot as plt
import random


# Activity 1: Simple Line Plot

def display_line(x, y):
    # Draw a line through the points and show the graph
    plt.plot(x, y)
    plt.show()


def run_task1():
    x_values = [1, 2, 3, 4, 5]
    # Each y value is the x value squared
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)


# Activity 2: Squares with Line Plot

def small():
    # Small square: red, circle markers, dotted line
    plt.plot([4, 6, 6, 4, 4], [4, 4, 6, 6, 4], "ro:")


def medium():
    # Medium square: green, square markers, dashed line
    plt.plot([3, 7, 7, 3, 3], [3, 3, 7, 7, 3], "gs--")


def large():
    # Large square: blue, pentagon markers, solid line
    plt.plot([2, 8, 8, 2, 2], [2, 2, 8, 8, 2], "bp-")


def run_task2():
    # Draw all three squares, then show them on one graph
    small()
    medium()
    large()
    # Make one step on x the same size as one step on y, so squares look square
    plt.axis("equal")
    plt.show()


# Activity 3: Path with Line Plots

def coordinate():
    print("Please enter an x value:")
    x = int(input())
    print("Please enter a y value:")
    y = int(input())
    # Send back both values together as a tuple
    return (x, y)


def path():
    print("Retrieving path...")
    x_values = []
    y_values = []
    # Ask for 4 points
    for count in range(4):
        data = coordinate()
        # The tuple holds x at [0] and y at [1]
        x_values.append(data[0])
        y_values.append(data[1])
    return [x_values, y_values]


def run_task3():
    values = path()
    # Label the axes
    plt.xlabel("x values")
    plt.ylabel("y values")
    # Red dashed line with circle markers
    plt.plot(values[0], values[1], "ro--")
    plt.show()


# Activity 4: Data Dictionary and Plots

def data():
    paths = {}
    # Store each of the user's choices in the dictionary under its own key
    print("What type of line would you like (:, -- or -)?")
    paths["line"] = input()
    print("What colour would you like (r, g or b)?")
    paths["colour"] = input()
    print("What style of marker would you like (o, s or ^)?")
    paths["marker"] = input()
    return paths


def generate():
    print("How many lines would you like to display?")
    lines = int(input())
    for count in range(lines):
        values = data()
        # 5 different random numbers from 1 to 10 (x sorted so the line runs left to right)
        x = sorted(random.sample(range(1, 11), 5))
        y = random.sample(range(1, 11), 5)
        # Join the choices into one style code, e.g. "r" + "o" + "--" gives "ro--"
        style = values["colour"] + values["marker"] + values["line"]
        plt.plot(x, y, style)
    # Show all the lines together on one graph
    plt.show()


def run():
    print("Running....")
    generate()
    print("Done!")


# Only run when this file is executed directly
if __name__ == "__main__":
    run()