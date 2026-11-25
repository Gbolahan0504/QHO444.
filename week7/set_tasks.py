# Week 7 - Sets


# Activity 1: Simple Set

def observed():
    # A set ignores duplicates, so each item is only kept once
    observations = {"Car", "Sky Scraper", "Sky Scraper", "Bike", "House", "House"}
    return observations


def run_task1():
    print(observed())


# Only run when this file is executed directly
if __name__ == "__main__":
    run_task1()