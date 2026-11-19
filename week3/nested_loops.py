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
