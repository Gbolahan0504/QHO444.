# Ask the user for the cover type
print("What type of cover does the book have?")
cover = input()

# Decide what to do based on the cover type
if cover == "soft":
    # Ask whether the soft cover book is perfect-bound
    print("Is the book perfect-bound?")
    bound = input()

    # Decide which soft cover message to show
    if bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif cover == "hard":
    print("Books with hard covers can be more expensive!")