#initialise the variables

star = "*"
row = 0

#create a user input and if statement to start the program
start = input("Type 'Go' to start the program ")
if start == "Go":

    #allow following statement to iterate up to 10 times
    for i in range (1,10):
        
        #create if statement to run whilst there are less than 5 rows
        if i <= 5:
            #Add '1' to the row each iteration then print the star * number of rows
            row = (row + 1)
            print(star * row)
        
        #create else statement to run whilst there are 5 or more rows    
        else:
            #Subtract '1' to the row each iteration then print the star * number of rows
            row = (row - 1)
            print(star * row)

