# Week 7 - JSON Files
import json


# Activity 1: Reading a JSON File

def read(file_path):
    with open(file_path) as file:
        # Load the whole JSON file into a Python dictionary
        data = json.load(file)
    print(f"Place Name: {data['location']}")
    print(f"Population Size: {data['population']}")
    # "bots" holds a list, and each bot in it is a dictionary
    for bot in data["bots"]:
        print(f"{bot['name']} has the following stats: {bot['stats']}")


def run():
    read("futurama.json")


# Only run when this file is executed directly
if __name__ == "__main__":
    run()