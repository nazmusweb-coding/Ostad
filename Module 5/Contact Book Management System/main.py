from contact_manager import ContactManager
from file_handler import FileHandler


def main():
    manager = ContactManager()
    file_handler = FileHandler()

    manager.contacts = file_handler.load_contacts()

    while True:
        print("\nContact Book Management System")
        print("1. Add a Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Remove a Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_contact()
            file_handler.save_contacts(manager.contacts)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.remove_contact()
            file_handler.save_contacts(manager.contacts)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
