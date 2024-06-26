# initialize variables
num_total = 0
times_iterated = 0
num = 0

# create a while loop that will repeat until broken
while True:

    # create a variable with input function to ask the user to enter a number
    num = int(input("Please enter a number here. Once you are finished, enter '-1'"))

    # create an if statement to break the while loop when the user inputs -1
    if num == -1:
        if times_iterated == 0:
            print("You didn't enter any numbers.")
            break
        else:
            break

    # create a variable to add the "num" input to "total"
    num_total += num

    # create a variable to store the count of times the user has input a number
    times_iterated += 1

# create a variable to store calculation of 'total' divided by 'count'
if times_iterated > 0:
    average = num_total / times_iterated
    # print the sentence with the 'average' variable using the 'f-string' to simplify concatenation
    print(f"The average of the numbers entered is {average}")

