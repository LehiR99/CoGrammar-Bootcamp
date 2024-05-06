# Define the adult class
class Adult():
    # Define can_drive method to show that the adult can drive
    def can_drive(self, name, age, eye_colour, hair_colour):
        print(f"{name} is old enough to drive.")

# Define the Child class which inherits from Adult class
class Child(Adult):
    # Override the can_drive method inherited from the Adult class
    def can_drive(self, name, age, eye_colour, hair_colour):
        print(f"{name} is too young to drive.")

# Create a class variable for the Adult and Child classes
meets_legal_driving_age = Adult()
illegal_driving_age = Child()

# Prompt the user to enter their name with error handling
while True:
    try:
        name = input("Please enter your name here: ")
        if name.isalpha():
            break
        else:
            print("The name can only contain letters.")
    except ValueError:
        print("Invalid input. Please enter a valid name")

# Prompt the user to input their age with error handling
while True:
    try:
        age = int(input("Please enter your age here: "))
        if age >= 0:
            break
        else:
            print("Age cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a valid age as a number")

# Prompt the user to input their eye color with error handling
while True:
    try:
        eye_colour = input("Please enter your eye color here: ")
        if eye_colour.isalpha():
            break
        else:
            print("Eye color can only contain letters.")
    except ValueError:
        print("Invalid input. Please enter a valid eye color")

# Prompt the user to input their hair color with error handling
while True:
    try:
        hair_colour = input("Please enter your hair color here: ")
        if hair_colour.isalpha():
            break
        else:
            print("Hair color can only contain letters.")
    except ValueError:
        print("Invalid input. Please enter a valid hair color")

# Determine if the person can drive based on their age
if age >= 18:
    meets_legal_driving_age.can_drive(name, age, eye_colour, hair_colour)
else:
    illegal_driving_age.can_drive(name, age, eye_colour, hair_colour)