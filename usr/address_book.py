class AddressBook:
    def __init__(self):
        # Store contacts in a dictionary with phone numbers as keys for easy uniqueness checks
        self.contacts = {}

    def add_contact(self, name, phone):
        if phone in self.contacts:
            print(f"Error: Phone number {phone} already exists for contact '{self.contacts[phone]}'.")
            return False
        
        self.contacts[phone] = name
        print(f"Success: Contact '{name}' added with phone number {phone}.")
        return True

    def edit_contact(self, old_phone, new_name=None, new_phone=None):
        if old_phone not in self.contacts:
            print(f"Error: Phone number {old_phone} not found.")
            return False

        current_name = self.contacts[old_phone]
        name = new_name if new_name else current_name
        phone = new_phone if new_phone else old_phone

        if phone != old_phone and phone in self.contacts:
            print(f"Error: The new phone number {phone} is already in use by another contact.")
            return False

        # Remove the old entry if the phone number changed
        if phone != old_phone:
            del self.contacts[old_phone]
        
        self.contacts[phone] = name
        print(f"Success: Contact updated. Name: '{name}', Phone: {phone}.")
        return True

    def delete_contact(self, phone):
        if phone in self.contacts:
            name = self.contacts.pop(phone)
            print(f"Success: Contact '{name}' with phone number {phone} deleted.")
            return True
        else:
            print(f"Error: Phone number {phone} not found.")
            return False

    def list_contacts(self):
        if not self.contacts:
            print("Address book is empty.")
            return

        print("\n--- Address Book ---")
        for phone, name in self.contacts.items():
            print(f"Name: {name}, Phone: {phone}")
        print("--------------------\n")

def main():
    book = AddressBook()
    
    while True:
        print("\nOptions:")
        print("1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. List Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            book.add_contact(name, phone)
            
        elif choice == '2':
            old_phone = input("Enter the phone number of the contact to edit: ")
            print("Leave blank if you do not want to change a field.")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            book.edit_contact(old_phone, new_name if new_name else None, new_phone if new_phone else None)
            
        elif choice == '3':
            phone = input("Enter the phone number of the contact to delete: ")
            book.delete_contact(phone)
            
        elif choice == '4':
            book.list_contacts()
            
        elif choice == '5':
            print("Exiting Address Book.")
            break
            
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
