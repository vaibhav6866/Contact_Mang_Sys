import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    return contacts

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

def add_contact(contacts):
    name = input("Enter the name of the contact: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if contacts:
        print("List of Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("No contacts found.")

def edit_contact(contacts):
    name = input("Enter the name of the contact you want to edit: ")
    if name in contacts:
        print("Current Information:")
        print(f"Name: {name}, Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        choice = input("What do you want to edit? (phone/email): ").lower()
        if choice == "phone":
            contacts[name]["phone"] = input("Enter the new phone number: ")
        elif choice == "email":
            contacts[name]["email"] = input("Enter the new email address: ")
        else:
            print("Invalid choice!")
            return
        save_contacts(contacts)
        print("Contact edited successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact you want to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n===== Contact Management System =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
