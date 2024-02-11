import pickle

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class AddressBook:
    def __init__(self, filename):
        self.contacts = []
        self.filename = filename

    def add_contact(self, contact):
        self.contacts.append(contact)

    def save_to_file(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_from_file(self):
        try:
            with open(self.filename, 'rb') as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            self.contacts = []

    def search_contacts(self, search_term):
        matching_contacts = [contact for contact in self.contacts
                             if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        return matching_contacts

    def __enter__(self):
        self.load_from_file()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save_to_file()

# Приклад використання
filename = 'address_book.pickle'
with AddressBook(filename) as address_book:
    # Додавання контактів
    address_book.add_contact(Contact("John Doe", "123456789"))
    address_book.add_contact(Contact("Jane Doe", "987654321"))
    address_book.add_contact(Contact("Taras", "087654321"))

    # Пошук контактів за ім'ям або номером телефону
    search_term = input("Введіть ім'я або номер телефону для пошуку: ")
    matching_contacts = address_book.search_contacts(search_term)

    if matching_contacts:
        print("Знайдені контакти:")
        for contact in matching_contacts:
            print(f"{contact.name}: {contact.phone}")
    else:
        print("Контакти не знайдені.")

