# Activity 1: Nested Loop
print("How many rows should I have?")
rows = int(input())
print()
print("How many columns should I have?")
columns = int(input())
print()
print("Here I go:")
print()

# Outer loop: one turn for each row
for row in range(rows):
    # Inner loop: one emoji for each column, all on the same line
    for column in range(columns):
        print(":-) ", end="")
    # Row finished, so move to a new line
    print()

print()
print("Done!")


# Activity 2: Nesting
print()
print("Please enter a sequence")
sequence = input()
print()
print("Please enter the character for the marker")
marker = input()
print()

# How many markers we have passed so far
markers_seen = 0
# How many characters sit between the two markers
distance = 0

# Check each character in the sequence
for character in sequence:
    if character == marker:
        # Found a marker, so add 1 to the marker count
        markers_seen = markers_seen + 1
    elif markers_seen == 1:
        # We are between the two markers, so count this character
        distance = distance + 1

print(f"The distance between the markers is {distance}.")

