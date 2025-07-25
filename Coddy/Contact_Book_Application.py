contact_book = {"Bob": {"phone": "234-567-8901", "email": "bob@example.com", "address": "456 Oak Ave"}}

def display_menu():
    print("""Contact Book Menu:
1. Add Contact
2. View Contact
3. Edit Contact
4. Delete Contact
5. List All Contacts
6. Exit""")
    
    while True:
        choice = input()
        if choice == '1':
            add_contact(contact_book)
        elif choice == '2':
            view_contact()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            list_contacts()
        elif choice == '6':
            print("Exiting the Contact Book.")
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
    
display_menu()