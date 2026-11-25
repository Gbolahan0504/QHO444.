# Week 7 - Dictionaries


# Activity 1: Simple Dictionary

def pattern():
    # Each key (the sequence name) is paired with a value (a number)
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


# Activity 2: Iterate Through Dictionaries

def display_keys(data):
    # A loop over a dictionary gives each key
    for key in data:
        print(key)


def display_values(data):
    # values() gives each value
    for value in data.values():
        print(value)


def display_items(data):
    # items() gives each key and value together
    for key, value in data.items():
        print(f"{key}: {value}")


def run():
    sequences = pattern()
    print("Dictionary:")
    print(sequences)
    print()
    print("Keys:")
    display_keys(sequences)
    print()
    print("Values:")
    display_values(sequences)
    print()
    print("Pairs:")
    display_items(sequences)


# Activity 3: Dictionary of Dictionaries

def short_pattern():
    pattern = {"sequence": "101", "occurrences": 5}
    return pattern


def medium_pattern():
    pattern = {"sequence": "111000", "occurrences": 25}
    return pattern


def long_pattern():
    pattern = {"sequence": "1100110011001100", "occurrences": 50}
    return pattern


def run_task3():
    print("Analysing patterns...")
    # Each value in this dictionary is itself a dictionary
    patterns = {
        "short sequence": short_pattern(),
        "medium sequence": medium_pattern(),
        "long sequence": long_pattern()
    }
    # Show each key with the dictionary stored under it
    for key, value in patterns.items():
        print(f"{key}: {value}")


# Only run when this file is executed directly
if __name__ == "__main__":
    run_task3()