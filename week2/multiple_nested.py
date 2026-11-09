# Ask where to look for the phone
print("Where should I look?")
room = input()

# Decide which room to search
if room == "in the bedroom":
    # Ask where in the bedroom to look
    print("Where in the bedroom should I look?")
    spot = input()

    # Decide what was found in the bedroom
    if spot == "under the bed":
        print("Found some shoes but no phone")
    else:
        print("Found some mess but no phone.")

elif room == "in the bathroom":
    # Ask where in the bathroom to look
    print("Where in the bathroom should I look?")
    spot = input()

    # Decide what was found in the bathroom
    if spot == "in the bathtub":
        print("Found a rubber duck but no phone")
    else:
        print("Found bathroom stuff but no phone.")

elif room == "in the living room":
    # Ask where in the living room to look
    print("Where in the living room should I look?")
    spot = input()

    # Decide what was found in the living room
    if spot == "on the table":
        print("Yes! I found my phone!")
    else:
        print("Found some stuff but no phone.")
else:
    print("I do not know where that is but I will keep looking.")
