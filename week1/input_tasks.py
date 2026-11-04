# Activity 1: Ask user to enter their name
print("What is your name?")
name = input()
print(f"It is nice to meet you {name}")

# Activity 2: ASCII robot with user-chosen eyes
print("Please enter a character for the eye")
eye = input()
print("The robots expression is now as follows:")
print("##########")
print(f"#  {eye}  {eye}  #")
print("#  ----  #")
print("##########")

# Activity 3: BMI calculator
print()
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

# Calculate BMI: weight divided by height squared
bmi = weight / height ** 2
print()
print(f"{user_name} you are {age} years old and your bmi is {bmi:.2f}.")

bmi = weight / height ** 2


# Activity 4: Health bars using string operators
print()
print("Please enter the number of lives.")
lives = int(input())

print()
print("Please enter the energy level.")
energy = int(input())

print()
print("Please enter the shield level.")
shield =int(input())

print()
print("Health has been set.")
print()
print(f"Lives:  {'♥' * lives}")
print(f"Energy: {'♦' * energy}")
print(f"Shield: {'♦' * shield}")