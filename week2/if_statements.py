# Activity 1: if statement
print("What type of book is this?")
book_type = input()
print()

# Check whether the book is an adventure book
if book_type == "adventure":
 print("I like adventure books!")

print()
print("Finished reading book.")


# Activity 2: if...else statement
print()
print("Please enter the activity to be performed.")
activity = input()
print()

# Check whether the activity is calculate
if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing activity...")

print()
print("Activity completed!")


# Activity 3: if...elif...else statement
print()
print("Towards which direction should I go (up, down, left or right)?")
direction = input()
print()

# Work out which direction the robot should move
if direction == "up":
    print("I am moving in an upward direction!")

elif direction == "down":
    print("I am moving in an downward direction!")
elif direction == "left":
    print("I am moving to the left!")
elif direction == "right":
    print("I am moving to the right!")
else:
    print("I do not know that direction!")


# Activity 4: Modulo operator
print()
print("Please enter a whole number.")
number = int(input())
print()

# A number is even if dividing by 2 leaves no remainder
if number % 2 == 0:
    print(f"The number {number} is an even number.")

else:
    print(f"The number {number} is an odd number.")


# Activity 5: Comparison operators
print()
print("Please enter the first number.")
first_number = float(input())
print("Please enter the second number.")
second_number = float(input())
print()

# Decide which number is the smallest
if first_number < second_number:
    print("The first number is the smallest!")
elif second_number < first_number:
    print("The second number is the smallest!")
else:
    print("Both are equal!")


# Activity 6: Counter
print()

# Start both counters at zero
even_count = 0
odd_count = 0

# First number
print("Please enter the first whole number.")
number_one = int(input())
if number_one % 2 == 0:
    even_count += 1
else:
    odd_count += 1

# Second number
print("Please enter the second whole number.")
number_two = int(input())


if number_two % 2 == 0:
    even_count += 1
else:
    odd_count += 1
# Third number
print("Please enter the third whole number.")
number_three = int(input())
if number_three % 2 == 0:
    even_count += 1
else:
    odd_count += 1

print()
print(f"There were {even_count} even and {odd_count} odd numbers.")



