### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email():
    # Declare the class variable, with default value, for emails.
    def __init__(self, email_address, subject_line, email_content):


    # Initialise the instance variables for emails.
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    # Create the method to change 'has_been_read' emails from False to True.
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
# --- Functions --- #
# Build out the required functions for your program.

    # Create 3 sample emails and add it to the Inbox list.
def populate_inbox():
    email_1 = Email("sample1@gmail.com", "Welcome to my website!", "Hello and Welcome to Lehi's Website!")
    email_2 = Email("sample2@gmail.com", "We Miss You!", "You haven't been on our site in a while, here's a discount code!")
    email_3 = Email("sample3@gmail.com", "You're going to Madrid", "Thank you for booking with our Airline")

    inbox.extend([email_1, email_2, email_3])

# Create a function which prints the email’s subject_line, along with a corresponding number.

def list_emails():
    if not inbox:
        print("Your inbox is empty")
        return

    print("Your Inbox")
    for index, email in enumerate(inbox):
        print(f"{index + 1}: {email.subject_line} {'(unread)' if not email.has_been_read else ''}") # print the index + 1

    # Create a function which displays a selected email.

def read_email(index):
    email = inbox[index]
    print(f"\nFrom: {email.email_address}")
    print(f"Subject: {email.subject_line}")
    print(f"\n{email.email_content}")
    # Once displayed, call the class method to set its 'has_been_read' variable to True.
    if not email.has_been_read:
        email.mark_as_read()

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program.
populate_inbox() #runs the "populate_inbox" method to add the sample emails to the inbox

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    if user_choice == 1:
        # add logic here to read an email

        list_emails() # Uses the list_emails method to show the emails in the inbox
        email_selection = int(input("Enter the number of the email you would like to read or enter -1 to return to the main menu: ")) # create a variable to ask the user to select the email they would like to read
        if email_selection == -1:
                continue
        else:
            read_email(email_selection-1)
            print(f"\n**Email from {inbox[email_selection-1].email_address} marked as read.**\n")

    elif user_choice == 2:
        # add logic here to view unread emails
        unread_emails = [email for email in inbox if not email.has_been_read] # variable to store unread emails which will store emails that havent been read using a for loop to iterate through the inbox

        if not unread_emails:
            print("You have no unread emails.")

        else:
            print("Unread Emails:")
            for index, email in enumerate(unread_emails):
                print(f"{index + 1}: {email.subject_line}")
            email_selection = int(input("Enter the number of the email you would like to read or -1 to go back to the main menu: "))
            if email_selection == -1:
                continue

            else:
                read_email(inbox.index(unread_emails[email_selection - 1]))

    elif user_choice == 3:
        # add logic here to quit appplication
        print("Leaving Lehi Mail")
        break

    else:
        print("Oops - incorrect input.")
