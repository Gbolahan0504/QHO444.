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


# Only run when this file is executed directly
if __name__ == "__main__":
    run()