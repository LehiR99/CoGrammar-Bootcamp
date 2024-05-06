# this program will take a user input for the amount of students, with their student ID's and then create a txt file to register their attendance to an exam

# create a variable with an input to store how many students will be registered for the exam
num_students = int(input("How many students are you registering for the exam? " ))

# create and open the reg_form.txt in "write" mode
with open("reg_form.txt","w") as file:
    # iterate through the range of how many students there are
    for i in range(num_students):
        # create a variable to store the student ID that the user inputs, corresponding to each student
        student_id = input(f"Please enter student {i + 1}'s ID: ")
        # write the student id on the file with a dotted line to write the registration details
        file.write(f"{student_id}\n")
        file.write("--------------\n")

print("Registration form created.")

