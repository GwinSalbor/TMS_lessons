     #Функции и аргументы
# # Задание 1.1
# def add(Var_1, Var_2):
#     return Var_1 + Var_2
# def sub(Var_1, Var_2):
#     return Var_1 - Var_2
# def mult(Var_1, Var_2):
#     return Var_1 * Var_2
# def div(Var_1, Var_2):
#     return Var_1 / Var_2 \
#         if Var_2 != 0 \
#         else "Деление на 0 невозможно!"
# def calculate():
#     Var_1 = int(input('Введите значение: '))
#     Var_2 = int(input('Введите значение: '))
#     action = input('Выбор функции +, -, *, /: ')
#     if action == '+':
#         return add(Var_1, Var_2)
#     elif action == '-':
#         return sub(Var_1, Var_2)
#     elif action == '*':
#         return mult(Var_1, Var_2)
#     elif action == '/':
#         return div(Var_1, Var_2)
#     else:
#         return "Ошибка!"
# print(calculate())

# Задание 1.2

def calculate_statistics(*args, **kwargs):
    stat = kwargs.get('stat')

    if stat == 'sum':
        return sum(args)
    elif stat == 'avg':
        return sum(args) // len(args)
    elif stat == 'max':
        return max(args)
    elif stat == 'min':
        return min(args)
    else:
        return 'Доступные функции sum, avg, max, min'

print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='sum'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='avg'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='max'))
print(calculate_statistics(1, 2, 3, 4, 5, 6, 7, stat='min'))

#Работа с файлами
#1.1

import random
import string

def generate_random_string(length=10):
    # Генерируем случайную строку длиной 'length', используя буквы и цифры
    characters = string.ascii_letters + string.digits  # Строка из всех букв и цифр
    return ''.join(random.choice(characters) for _ in range(length))

def write_random_strings_to_file(filename, num_strings=10):
    with open(filename, 'w') as file:
        for _ in range(num_strings):
            # Генерируем случайную строку
            random_string = generate_random_string()

            # Случайно выбираем число из набора
            random_number = random.choice([200, 300, 400, 500])

            # Добавляем число в конец строки
            random_string_with_number = f"{random_string}{random_number}"

            # Записываем строку в файл
            file.write(random_string_with_number + '\n')

# Пример вызова функции
write_random_strings_to_file('random_strings.txt', num_strings=15)

#1.2

def split_file_by_status(input_filename):
    # Открываем исходный файл для чтения
    with open(input_filename, 'r') as file:
        # Создаем словари для файлов в зависимости от статуса
        status_files = {
            200: open('status_200.txt', 'w'),
            300: open('status_300.txt', 'w'),
            400: open('status_400.txt', 'w'),
            500: open('status_500.txt', 'w')
        }

        # Читаем строки из исходного файла
        for line in file:
            # Убираем возможные пробелы и переносы строк
            line = line.strip()

            # Проверяем, на какой статус заканчивается строка и записываем в нужный файл
            if line.endswith('200'):
                status_files[200].write(line + '\n')
            elif line.endswith('300'):
                status_files[300].write(line + '\n')
            elif line.endswith('400'):
                status_files[400].write(line + '\n')
            elif line.endswith('500'):
                status_files[500].write(line + '\n')

    # Закрываем все открытые файлы
    for f in status_files.values():
        f.close()

# Пример вызова функции
split_file_by_status('random_strings.txt')
