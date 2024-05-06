#This program will read the data from DOB.txt text fill and print into 2 separate lists: "Names" and "Birth Date"

# Open DOB.txt in read only mode
with open("DOB.txt","r") as file:
    lines = file.readlines()

names = [] # Create a list that will store the names from DOB.txt
birthdates = [] # Create a list that will store the names from DOB.txt

# for loop to iterate over each line in DOB.txt and split into names and birthdates
for line in lines:
    split_string = line.split() # split each string into a list
    name = " ".join(split_string[:-3]) # join the name elements from the split string list
    birthdate = " ".join(split_string[-3:]) # join the birthdate elements from the split string list
    names.append(name)
    birthdates.append(birthdate)

# iterate to print each name in a new line from the list
print("\n Name ")
for name in names:
    print(name)

#iterate to print each birthdate in a new line from the list
print("\n Birthdate ")
for birthdate in birthdates:
    print(birthdate)