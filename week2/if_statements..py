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

