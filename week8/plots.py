# Week 8 - Plots
import matplotlib.pyplot as plt


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


# Only run when this file is executed directly
if __name__ == "__main__":
    run_task3()