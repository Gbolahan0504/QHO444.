# Week 1 - Input


def greet_user():
    # Activity 1: Ask the user for their name and greet them
    print("What is your name?")
    name = input()
    print(f"It is nice to meet you {name}")


def robot_eyes():
    # Activity 2: ASCII robot with eyes chosen by the user
    print("Please enter a character for the eye")
    eye = input()
    print("The robots expression is now as follows:")
    print("##########")
    print(f"#  {eye}  {eye}  #")
    print("#  ----  #")
    print("##########")


def bmi_calculator():
    # Activity 3: Read the user's details and work out their BMI
    print("What is your name?")
    user_name = input()
    print()
    print("How old are you (in years)?")
    age = int(input())
    print()
    print("How tall are you (in meters)?")
    height = float(input())
    print()
    print("How much do you weigh (in kilograms)?")
    weight = float(input())
    # BMI is weight divided by height squared
    bmi = weight / height ** 2
    print()
    print(f"{user_name} you are {age} years old and your bmi is {bmi:.2f}.")


def health_bars():
    # Activity 4: Show health bars using string repetition
    print("Please enter the number of lives.")
    lives = int(input())
    print()
    print("Please enter the energy level.")
    energy = int(input())
    print()
    print("Please enter the shield level.")
    shield = int(input())
    print()
    print("Health has been set.")
    print()
    print(f"Lives:  {'♥' * lives}")
    print(f"Energy: {'♦' * energy}")
    print(f"Shield: {'♦' * shield}")


# Only run when this file is executed directly
if __name__ == "__main__":
    greet_user()
    print()
    robot_eyes()
    print()
    bmi_calculator()
    print()
    health_bars()