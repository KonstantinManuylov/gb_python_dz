from data_create import *


def search_line():
    print('Выбертите вариант поиска:\n'
          '1. Имя\n'
          '2. Фамилия\n'
          '3. Отчество\n'
          '4. Телефон\n'
          '5. Адрес')
    index = int(input('Введите вариант: ')) - 1
    searched = input('Введите поисковые данные: ').title()
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        for item in data:
            new_item = item.replace('\n', ' ').split()
            if searched in new_item[index]:
                print(item, end="\n\n")


def enter_data():
    name = enter_first_name()
    surname = enter_second_name()
    family = enter_family_name()
    number = enter_phone_number()
    address = enter_address_number()
    with open('book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family}\n{number}\n{address}\n\n')


def delete():
    result = []
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        searched = input('Введите контакт для удаления: ').title()
        for item in data:
            if searched in item:
                result.append(item)
        if len(result) == 1:
            confirm_del = input(f'Желаете удалить контакт {result[0]}?\n Введите "y" для подтверждения: ').lower()
            if confirm_del == 'y':
                with open('book.txt', 'w', encoding='utf-8') as rewrite_file:
                    for item in data:
                        if item != result[0]:
                            rewrite_file.write(item + "\n\n")
        elif len(result) == 0:
            print('Такого контакта нет. ')
        else:
            print(f'Список совпадений по вашему запросу:\n')
            for number, name in enumerate(result):
                print(number + 1, name)
            conf_num = int(input(f'Выберите номер контакта для удаления: ')) - 1
            confirm_del = input(
                f'Желаете удалить контакт {result[conf_num]}?\n Введите "y" для подтверждения: ').lower()
            if confirm_del == 'y':
                with open('book.txt', 'w', encoding='utf-8') as rewrite_file:
                    for item in data:
                        if item != result[conf_num]:
                            rewrite_file.write(item + "\n\n")


def edit_contact():
    result = []
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        searched = input('Введите контакт для редактирования: ').title()
        for item in data:
            if searched in item:
                result.append(item)
        if len(result) == 1:
            confirm_edit = input(
                f'Желаете редактировать контакт {result[0]}?\n Введите "y" для подтверждения: ').lower()
            if confirm_edit == 'y':
                with open('book.txt', 'w', encoding='utf-8') as rewrite_file:
                    for item in data:
                        if item != result[0]:
                            rewrite_file.write(item + "\n\n")
                enter_data()
        elif len(result) == 0:
            print('Такого контакта нет. ')
        else:
            print(f'Список совпадений по вашему запросу:\n')
            for number, name in enumerate(result):
                print(number + 1, name)
            conf_num = int(input(f'Выберите номер контакта для редактирования: ')) - 1
            confirm_edit = input(
                f'Желаете редактировать контакт {result[conf_num]}?\n Введите "y" для подтверждения: ').lower()
            if confirm_edit == 'y':
                with open('book.txt', 'w', encoding='utf-8') as rewrite_file:
                    for item in data:
                        rewrite_file.write(item + "\n\n")
                        if item != result[conf_num]:
                            rewrite_file.write(item + "\n\n")
                enter_data()


def print_data():
    with open('book.txt', 'r', encoding='utf-8') as file:
        print(file.read())
