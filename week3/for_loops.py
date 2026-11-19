# Activity 1: Simple Loop
print("How many mountains should I display?")
mountains = int(input())
print()
print("Displaying...")
print()

# Draw one mountain each time round the loop
for count in range(mountains):
    print("     __")
    print("    /  \\_")
    print("   /^    \\")
    print("  /  ^    \\_")
    print("_/ ^ ^     ^\\")
    print()

print("Done!")


# Activity 2: Count Down
print()
print("How far are we from the target?")
steps = int(input())
print()

# Count down from the number entered to 1
for remaining in range(steps, 0, -1):
    print(f"{remaining} steps remaining")

print()
print("Target achieved!")


# Activity 3: Range
print()
print("What level of brightness is required?")
brightness = int(input())
print()
print("Adjusting brightness...")
print()

# Go up in even numbers from 2 to the level entered (+1 so it is included)
for level in range(2, brightness + 1, 2):
    # Show one star for each level of brightness
    print("Brightness level: " + "*" * level)

print()
print("Complete!")

