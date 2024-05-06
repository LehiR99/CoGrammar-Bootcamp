# create a function to alternate each letter in a string to upper and lower case
def alternate_characters(string):
     # Split the input string into words
    word_list = string.split()
    final_sentence = []
    for word in word_list:
        altered_word = ''
        # Loop through each character in the word
        for i in range(len(word)):
             # Alternate between upper and lower case characters
            if i % 2 == 0:
                altered_word += word[i].upper()
            else:
                altered_word += word[i].lower()
        # Append the modified word to the result list
        final_sentence.append(altered_word)
     # Join the modified words back into a single string
    return ' '.join(final_sentence)

# create a function to alternate each word in a string to upper and lower case

def alternate_words(string):
    # Split the input string into words
    words = string.split()
    modified_words = []
    # Loop through each word in the input string
    for i in range(len(words)):
        # Check if the index is even or odd to determine the case
        if i % 2 == 0:
            # Convert even-indexed words to lowercase and append to the result list
            modified_words.append(words[i].lower())
        else:
            # Convert odd-indexed words to uppercase and append to the result list
            modified_words.append(words[i].upper())
    # Join the modified words back into a single string
    return ' '.join(modified_words)

# create an variable to store the users input string
user_sentence = input("Enter a sentence here: ")
# Print the users string with alternative upper and lower case characters
print("Your sentence with alternate characters is: ", alternate_characters(user_sentence))
# Print the users string with alternative upper and lower case words
print("Your sentence with alternate words is: ", alternate_words(user_sentence))