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