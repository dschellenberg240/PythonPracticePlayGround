#functions that will perform the chosen action - add, update, or delete
def add_contact(): #funciton actions to add new contact
    contact = {
        "First Name": input("First Name: "),
        "Last Name": input("Last Name: "),
        "Phone Number": input("Phone Number: "),
        "Email": input("Email: ")
    }
    phone_book.append(contact)
    print("Contact added successfully!\n")

def update_contact(): #function to update contact
    update_place_holder = "This is a place holder"

def delete_contact(): #function to delete a contact
    place_holder = "This is a place holder"

def viewing_contacts(): #Function that will return the current contact list
    for key, value in phone_book.items():
        print(f'{key}: {value}')

#Phone book. Utilizing dictionaries - Note, this was originally a dict, I realized I needed a list that I could append to
phone_book = []

print("   Your Phone Book   ")
print("---------------------")
next_action_choice = 0
#An option menu, what to do next
while next_action_choice != 5:
    next_action_choice = int(input("1: Add new contact\n2: Update contact\n3: Delete contact\n4: View contacts\n5: Exit\n\nChoice: "))
    if next_action_choice == 1:
        add_contact()
    elif next_action_choice == 2:
        update_contact()
    elif next_action_choice == 3:
        delete_contact()
    elif next_action_choice == 4:
        viewing_contacts()
    elif next_action_choice == 5:
        print("Good Bye!👋🏼")
    else:
        print("You'll need to make a selection")