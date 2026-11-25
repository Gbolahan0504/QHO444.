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
# Activity 2: Exporting to a JSON file

def read_task2(file_path):
    print("Reading...", end="")
    with open(file_path) as file:
        data = json.load(file)
    print("Done!")
    return data


def save(file_path, data):
    print("Exporting...", end="")
    # "w" opens the file for writing (it is created if it does not exist)
    with open(file_path, "w") as file:
        # Write the data as JSON, indented 4 spaces per level
        json.dump(data, file, indent=4)
    print("Done!")


def run_task2():
    json_data = read_task2("futurama.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run_task2()