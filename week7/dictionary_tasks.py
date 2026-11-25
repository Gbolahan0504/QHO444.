# Week 7 - Dictionaries


# Activity 1: Simple Dictionary

def pattern():
    # Each key (the sequence name) is paired with a value (a number)
    sequences = {"Short Sequence": 3, "Medium Sequence": 2, "Long Sequence": 1}
    return sequences


def run():
    print(pattern())


# Only run when this file is executed directly
if __name__ == "__main__":
    run()