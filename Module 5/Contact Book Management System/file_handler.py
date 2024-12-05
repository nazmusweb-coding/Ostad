import os
import csv

class FileHandler:
    FILE_PATH = "data/contacts.csv"

    def load_contacts(self):
        contacts = []
        try:
            with open(self.FILE_PATH, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                contacts = [row for row in reader]
        except FileNotFoundError:
            pass
        return contacts

    def save_contacts(self, contacts):
        os.makedirs(os.path.dirname(self.FILE_PATH), exist_ok=True)

        with open(self.FILE_PATH, mode='w', newline='') as file:
            fieldnames = ["Name", "Phone", "Email", "Address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(contacts)
