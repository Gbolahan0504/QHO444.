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
