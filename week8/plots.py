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


# Only run when this file is executed directly
if __name__ == "__main__":
    run_task2()