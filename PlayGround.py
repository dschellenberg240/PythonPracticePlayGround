#functions that will perform the chosen action - add, update, or delete
def add_contact(): #funciton actions to add new contact
    phone_book["First Name"] = input("First Name: ")
    phone_book["Last Name"] = input("Last Name: ")
    phone_book["Phone Number"] = input("Phone Number: ")
    phone_book["Email"] = input("Email: ")

def update_contact(): #function to update contact
    update_place_holder = "This is a place holder"

def delete_contact(): #function to delete a contact
    place_holder = "This is a place holder"

def viewing_contacts(): #Function that will return the current contact list
    for key, value in phone_book.items():
        print(f'{key}: {value}')

#Phone book. Utilizing dictionaries
phone_book = {
    "First Name": " ",
    "Last Name": " ",
    "Phone Number": " ",
    "Email": " "
}

print("   Your Phone Book   ")
print("---------------------")

#An option menu, what to do next
next_action_choice = input("1: Add new contact\n2: Update contact\n3: Delete contact\n4: View contacts\n5: Exit\n\nChoice: ")