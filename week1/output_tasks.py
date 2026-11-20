# Week 1 - Output


def display_box():
    # Display an ASCII box
    print("##########")
    print("#        #")
    print("#        #")
    print("##########")


def display_escape_message():
    # \t adds a tab and \" displays a double quote
    print("\t\"I am programming!\"")


def display_robot():
    # Display an ASCII robot face
    print("##########")
    print("#  o  o  #")
    print("#  ----  #")
    print("##########")


# Only run when this file is executed directly
if __name__ == "__main__":
    display_box()
    display_escape_message()
    print()
    display_robot()