import Model
import View



def main_menu():
    while True:
        print('\nГлавное меню:')
        print('1. Добавить контакт')
        print('2. Удалить контакт')
        print('3. Изменить контакт')
        print('6. Поиск контакта')
        print('7. Открыть файл')
        print('8. Сохранить файл')
        print('0. Выйти из программы')
        choice = int(input('Выберите пункт: '))
        match (choice):
            case 1:
                add_contact()
                print('\nКонтакт добавлен\n')
            case 2:
                remove_contact()
                print('\nКонтакт удален\n')
            case 3:
                change_contact()
            case 6:
                find_contacts()
            case 7:
                open_file()
            case 8:
                save_file()
                print('\nФайл сохранен!\n')
            case 0:
                break


def start():
    # open_file()
    View.printPhoneBook()
    main_menu()



def open_file():
    while True:
        file_name = input('Введите имя файла телефонной книги: ')
        try:    
            with open(file_name, "r", encoding="UTF-8") as data:
                Model.path = file_name
                contacts_list = data.read().split("\n")
                Model.phonebook = contacts_list
                break
        except:
            print('Файл не найден. Введите заново имя файла, либо введите exit')
            if file_name == 'exit': break
    View.printPhoneBook()

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def add_contact():
    name = input('Введите имя: ')
    surname = input('Введите фамилию: ')
    last_name = input('Введите отчество: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {surname}; {last_name}; {phone};\n'
    Model.phonebook.append(contact)
    View.printPhoneBook()

def remove_contact():
    choice = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(choice)
    View.printPhoneBook()

def change_contact():

    choice = int(input('Введите номер элемента для изменения: '))
    choice2 = int(input('Что изменяем (0-имя, 1-фамилия, 2-отчество, 3-телефон): '))

    contact = Model.phonebook.pop(choice).split(';')
    print(contact)
    contact[choice2] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(choice, ';'.join(contact))
    View.printPhoneBook()

def find_contacts():
    toSearch = input('Введите данные для поиска: ')
    View.printPhoneBookFltr(toSearch)
