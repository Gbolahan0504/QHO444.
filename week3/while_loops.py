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