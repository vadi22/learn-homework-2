"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('list_prof.csv', 'w', encoding='UTF-8', newline = '') as file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for name in my_dict:
            writer.writerow(name)


my_dict = [{'name': 'Tom', 'age':'23', 'job': 'doctor'},
            {'name': 'Lora', 'age':'33', 'job': 'teacher'},
            {'name': 'Jon', 'age':'43', 'job': 'engineer'},
            {'name': 'Tery', 'age':'28', 'job': 'cook'}]


if __name__ == "__main__":
    main()
