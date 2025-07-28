contact_book = {"Bob": {"phone": "234-567-8901", "email": "bob@example.com", "address": "456 Oak Ave"}}

def display_menu():
    while True:
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. List All Contacts")
        print("6. Exit")

        choice = int(input())
        if choice == 1:
            add_contact(contact_book)
        elif choice == 2:
            view_contact(contact_book)
        elif choice == 3:
            edit_contact(contact_book)
        elif choice == 4:
            delete_contact(contact_book)
        elif choice == 5:
            list_contacts(contact_book)
        elif choice == 6:
            break
        else:
            print("Invalid choice. Please try again.")

def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()  
    if name in contact_book:
        print(f"Contact already exists!")
    else:
        contact_book[name] = {"phone": phone, "email": email, "address": address}
        print(f"Contact added successfully!")
        
def view_contact(contact_book):
    name = input("")
    if name in contact_book:
        print(f"Name: {name}")
        for key, value in contact_book[name].items():
            print(f"{key.capitalize()}: {value}")
    else: 
        print("Contact not found!")

def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        for key in contact_book[name]:
            new_value = input()
            if new_value:
                contact_book[name][key] = new_value
        print("Contact updated successfully!")        
    else:
        print("Contact not found!")
        
def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        del contact_book[name]
        print(f"Contact deleted successfully!")        
    else:
        print("Contact not found!")

def list_contacts(contact_book):
    if contact_book:
        for name, details in contact_book.items():
            print(f"Name: {name}")
            for key, value in details.items():
                print(f"{key.capitalize()}: {value}")
            print("")           
    else:
        print("No contacts available.")
        
display_menu()