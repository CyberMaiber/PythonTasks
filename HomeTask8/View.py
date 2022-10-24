import Model


def printPhoneBook():
    for i, item in enumerate(Model.phonebook):
        print(i , item)

def printPhoneBookFltr(textToFind:str):
    lst = []
    lst = list(filter(lambda x: textToFind in x, Model.phonebook))
    for i, item in enumerate(lst):
        print(i , item)
    if len(lst) == 0: print('Ничего не найдено.')