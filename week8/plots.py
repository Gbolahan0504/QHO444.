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


# Only run when this file is executed directly
if __name__ == "__main__":
    run_task1()