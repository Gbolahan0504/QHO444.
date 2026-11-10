# Ask which path to take in the cave
print("Which path should I take (left, right or straight)?")
path = input()

# Decide what happens on each path
if path == "left":
    # Ask whether to light a torch
    print("Should I light a torch (yes/no)?")
    torch = input()

    # Decide what I can see
    if torch == "yes":
        print("I can see gold coins on the floor!")
    else:
        print("It is too dark to see anything.")
elif path == "right":
    # Ask what to do when a bat appears
    print("A bat flies at me! What should I do (run, hide or fight)?")
    action = input()

    # Decide whether I stay safe
    if (action == "run") or (action == "hide"):
        print("I stayed safe from the bat.")
    else:
        print("The bat scratched me, but I keep going.")
elif path == "straight":
    # Ask whether I feel brave
    print("I hear a dragon ahead. Am I feeling brave (yes/no)?")
    brave = input()

    # Ask whether I have a sword
    print("Do I have a sword (yes/no)?")
    sword = input()

    # Decide what to do about the dragon
    if not (brave == "yes"):
        print("I am not brave enough. I will turn back.")
    elif (brave == "yes") and (sword == "yes"):
        print("I will face the dragon")
    else:
        print("I am brave but have no sword. I will sneak past quietly.")
else:
    print("That path does not exist. I will stay here.")