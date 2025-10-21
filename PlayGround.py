"""
Python projects ideas - Dice roll with a gambling aspect to it. Bet x amount on what you think the number will be.
"""

"""
----> Start: Pizza Order project

print("Welcome to PPP! Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L: ").upper()
pepperoni = input("Do you wan pepperoni on you pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Input not recognized.")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")


----> End: Pizza order project
"""


"""
----> Start: phone book project.
>I was able to practice functions, if statement, loops, working with lists, and data types.
>I still need to complete the update_contact() function and the delete_contact()

#functions that will perform the chosen action - add, view, update, or delete
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
    if not phone_book:
        print("🦗It's pretty empty here!\n")
        return
    print("\nYour current contacts")
    print("------------------------")
    for i, contact in enumerate(phone_book, start=1):
        print(f"\nContact #{i}")
        for key, value in contact.items():
            print(f"{key:<13}: {value}")

#Phone book. Utilizing dictionaries - Note, this was originally a dic,
#I realized I needed a list that I could append to, so I updated it to start as an empty list.
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


-----> End: Phone book project
"""