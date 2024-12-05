from validation import validate_name, validate_phone

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter Name: ")
        if not validate_name(name):
            print("The contact’s name must be a string.")
            return

        phone = input("Enter Phone Number: ")
        if not validate_phone(phone):
            print("The phone number must be an integer.")
            return
        elif self.is_duplicate(phone):
            print("Invalid or duplicate phone number. Try again.")
            return

        email = input("Enter Email: ")
        address = input("Enter Address: ")
        self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print(f"\n{'Name':<20} {'Phone':<15} {'Email':<25} {'Address':<30}")
        print("-" * 90)
        for contact in self.contacts:
            print(f"{contact['Name']:<20} {contact['Phone']:<15} {contact['Email']:<25} {contact['Address']:<30}")

    def search_contact(self):
        query = input("Enter a name, phone, or email to search: ").lower()
        results = [c for c in self.contacts if
                   query in c['Name'].lower() or query in c['Phone'] or query in c['Email'].lower()]
        if results:
            print(f"\n{'Name':<20} {'Phone':<15} {'Email':<25} {'Address':<30}")
            print("-" * 90)
            for contact in results:
                print(f"{contact['Name']:<20} {contact['Phone']:<15} {contact['Email']:<25} {contact['Address']:<30}")
        else:
            print("No matching contacts found.")

    def remove_contact(self):
        phone = input("Enter the phone number of the contact to remove: ")
        self.contacts = [c for c in self.contacts if c['Phone'] != phone]
        print("Contact removed successfully!" if len(self.contacts) else "No such contact found.")

    def is_duplicate(self, phone):
        return any(contact['Phone'] == phone for contact in self.contacts)
