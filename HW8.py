class Phonebook:
    def __init__(self, file_path):
        self.file_path = file_path
        self.contacts = self.load_contacts()

def load_contacts(self):
    contacts = {}
    try:
        with open(self.file_path, 'r') as file:
            for line in file:
                name, phone_number = line.strip().split(',')
                contacts[name] = phone_number
    except FileNotFoundError:
        print(f"Файл {self.file_path} не найден. Создание нового файла.")

    return contacts

def save_contacts(self):
    with open(self.file_path, 'w') as file:
        for name, phone_number in self.contacts.items():
            file.write(f"{name},{phone_number}\n")

def add_contact(self, name, phone_number):
    self.contacts[name] = phone_number
    self.save_contacts()
    print("Контакт успешно добавлен.")

def remove_contact(self, name):
    if name in self.contacts:
        del self.contacts[name]
        self.save_contacts()
        print("Контакт успешно удален.")
    else:
        print("Контакт не найден.")

def update_contact(self, name, new_phone_number):
    if name in self.contacts:
        self.contacts[name] = new_phone_number
        self.save_contacts()
        print("Контакт успешно обновлен.")
    else:
        print("Контакт не найден.")

def search_contact(self, name):
    if name in self.contacts:
        return f"Имя: {name}, Телефон: {self.contacts[name]}"
    else:
        return "Контакт не найден."

# Пример использования
phonebook = Phonebook("contacts.txt")

while True:
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Изменить контакт")
    print("4. Поиск контакта")
    print("5. Выйти")

phonebook = Phonebook("contacts.txt")

while True:
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Изменить контакт")
    print("4. Поиск контакта")
    print("5. Выйти")

choice = input("Выберите действие (1-5): ")

if choice == "1":
    name = input("Введите имя контакта: ")
    phone_number = input("Введите номер телефона контакта: ")
    phonebook.add_contact(name, phone_number)
elif choice == "2":
    name = input("Введите имя контакта для удаления: ")
    phonebook.remove_contact(name)
elif choice == "3":
    name = input("Введите имя контакта для изменения: ")
    new_phone_number = input("Введите новый номер телефона: ")
    phonebook.update_contact(name, new_phone_number)
elif choice == "4":
    name = input("Введите имя контакта для поиска: ")
    print(phonebook.search_contact(name))
elif choice == "5":
    exit()