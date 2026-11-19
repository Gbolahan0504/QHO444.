# Activity 1: Simple loop
print ("How many apples should I remove?")
apples = int(input())
print()


# Track how many apples have been removed so far
removed = 0

# Keep removing apples until we reach the number asked for
while removed < apples:
    print("Removed apple.")
    # Add 1 to the count so the loop eventually stops
    removed = removed + 1


# Activity 2: Count
print()
print("How many obstacles must I avoid?")
obstacles = int(input())
print()

# Track how many obstacles have been avoided so far
avoided = 0

# Keep avoiding obstacles until we reach the number asked for
while avoided < obstacles:
    # Stay on the same line so "Done!" appears next to "Avoiding..."
    print("Avoiding...", end="")
    avoided = avoided + 1
    print(f"Done! {avoided} obstacles avoided.")

print()
print("All obstacles have been avoided.")



# Activity 3: ASCII
print()
print("How many bars should be charged?")
bars = int(input())
print()

# Track how many bars have been charged so far
charged = 0

# Keep charging until we reach the number of bars asked for
while charged < bars:
    charged = charged + 1
    # "\u2588" is the block character, repeated once for each charged bar
    print("Charging: " + "\u2588 " * charged)

print()
print("The battery is fully charged.")


# Activity 4: Repeating Word
print()
print("Please enter a phrase:")
phrase = input()
print()

# Count the characters in the phrase, spaces included
length = len(phrase)

# Track how many times "Hi" has been shown
count = 0

# Show "Hi" once for each character, all on the same line
while count < length:
    print("Hi ", end="")
    count = count + 1

# Move to a new line once the loop is finished
print()


# Activity 5: Sum 100
print()
print("Calculating the sum of the first 100 numbers...")

# Running total starts at 0
total = 0
# Start counting from 1
number = 1

# Keep going until we have added 100
while number <= 100:
    # Add the current number to the running total
    total = total + number
    # Move on to the next number
    number = number + 1

print(f"...Done! The answer is {total}.")


# Activity 6: Sum User Numbers
print()
print("How many numbers should I sum up?")
how_many = int(input())
print()

# Running total of the numbers entered
user_total = 0
# Track how many numbers have been entered so far
count = 0

# Keep asking until we have the number of values requested
while count < how_many:
    print(f"Please enter number {count + 1} of {how_many}:")
    value = int(input())
    # Add the new number to the running total
    user_total = user_total + value
    count = count + 1

print()
print(f"The answer is {user_total}.")
