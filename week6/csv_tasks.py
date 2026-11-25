# Week 6 - CSV Files
import csv


# Activity 1: Reading a CSV File

def read_csv(file_path):
    with open(file_path) as file:
        # The reader splits each line at the commas into a list
        csv_reader = csv.reader(file)
        # Take the first row on its own: the headings
        headings = next(csv_reader)
        print(f"Headings:\n{headings}")
        print("Values:")
        # Go through every row that is left
        for values in csv_reader:
            print(values)


def run_task1():
    read_csv("clothing.csv")


# Only run when this file is executed directly
# Activity 3: Export CSV

def export(file_path, count):
    print("Exporting...")
    # "a" opens the file for appending: new lines go on the end
    with open(file_path, "a") as file:
        for item in range(count):
            print("Please enter the item id:")
            item_id = input()
            print("Please enter the item name:")
            item_name = input()
            print("Please enter the item colour:")
            item_colour = input()
            # Write one CSV row, ending with a new line
            file.write(f"{item_id},{item_name},{item_colour}\n")
    print("Done!")


def run():
    # Export 2 items to the CSV file
    export("exported_items.csv", 2)


# Activity 2: Extract Values from CSV

def extract(file_path):
    print("Extracting...", end="")
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        # Read the headings but do nothing with them, just to skip past them
        next(csv_reader)
        names = ""
        # Take the name (index 1) from each row
        for values in csv_reader:
            names = names + values[1] + "\n"
    print("Done! The extracted items are as follows:")
    print(names)


def run_task2():
    extract("clothing.csv")


if __name__ == "__main__":
    run()