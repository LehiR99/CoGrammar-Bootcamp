#store the users sentence input into a the "str_manip" variable.
str_manip =  input("Enter a sentence here: ")

#calculate the length of the string, then display it with an explanation to the number.
print("The length of the string is", len(str_manip))

#Find the last letter of the str_manip sentence
last_letter = str_manip[-1]

# Replace every reoccurnce of this letter with '@' then print the new string
modified_sentence = str_manip.replace(last_letter, "@")
print (modified_sentence)

# Reorder the last 3 letters of str_manip backwards and print
print("Last three characters backwards:", str_manip[-3:][::-1])

# Find the first 3 characters and last 3 characters of str_manip and print the combination
print("The first 3 charaters and last 2 characters combined makes: ", str_manip[:3]+ str_manip[-2:])