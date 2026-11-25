# Week 7 - Sets


# Activity 1: Simple Set

def observed():
    # A set ignores duplicates, so each item is only kept once
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    print(observed())


# Only run when this file is executed directly
# Activity 2: Set From Other Data Structures

def observed_items():
    observations = []
    # Read 7 observations from the user into a list
    for count in range(7):
        print("Please enter an observation:")
        observations.append(input())
    return observations


def run_task2():
    print("Counting observations...")
    observations = observed_items()
    print()
    # An empty set: written set() because {} would make a dictionary
    counted = set()
    # Pair each value with how many times it appears in the list
    for value in observations:
        counted.add((value, observations.count(value)))
    # Each tuple holds the name at [0] and the count at [1]
    for item in counted:
        print(f"{item[0]} observed {item[1]} times.")


if __name__ == "__main__":
    run_task2()
