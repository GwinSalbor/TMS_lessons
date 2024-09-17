# задание 1, лекция 6 
# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mult(a, b):
#     return a * b
# def div(a, b):
#     if b == 0:
#         raise ValueError("division by 0 is impossible")
#     return a / b

# def calculate(a, b, action):
#     if action == "+":
#         return add(a, b)
#     elif action == "-":
#         return sub(a, b)
#     elif action == "*":
#         return mult(a, b)
#     elif action == "/":
#         return div(a, b)
#     else:
#         raise ValueError("unknown operation, indicate the arithmetic operation")

# print(calculate(11, 44, '+')) 
# print(calculate(22, 55, '-')) 
# print(calculate(33, 66, '*'))  
# print(calculate(77, 8, '/')) 

#задание 2, лекция 6 
# def calculate_statistic(*args, **kwargs):
#     numbers = args[0]
#     if not args:
#        raise ValueError("no numbers provided")
#     total_sum = sum(numbers)
#     count = len(numbers)
#     average = total_sum / count
#     maximum = max(numbers)
#     minimum = min(numbers)
    
#     format_result = kwargs.get('format', None)
    
#     if format_result == 'int':
#         average = round(average)
#         maximum = round(maximum)
#         minimum = round(minimum)
#     elif format_result == 'float':
#         average = round(average, 1)
#         maximum = round(maximum, 1)
#         minimum = round(minimum, 1)

#     return {
#         'average': average,
#         'maximum': maximum,
#         'minimum': minimum,
#         'sum': total_sum
#     }
# numbers=[1,22,333,4,56,789]
# print(calculate_statistic(numbers, format='int'))
# print(calculate_statistic(numbers, format='float'))

# задание 3, лекция 6

import random
import string
def generate_random_string(length=20):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))
def write_random_lines_to_file(filename, num_lines=10):
    numbers = [200, 300, 400, 500]
    with open(filename, 'w') as file:
        for _ in range(num_lines):
            random_string = generate_random_string()
            random_number = random.choice(numbers)
            line = f"{random_string}{random_number}\n"
            file.write(line)
write_random_lines_to_file('random_strings.txt', num_lines=10)

# задание 4, лекция 6 -  если можно ссылку на подобные задания (как 3 и 4), чтобы еще подобное порешать 
# import os
# def split_file_by_status(input_filename):
#     status_files = {
#         200: 'status_200.txt',
#         300: 'status_300.txt',
#         400: 'status_400.txt',
#         500: 'status_500.txt'
#     }
#     # Создаем словарь для хранения строк по статусам
#     status_lines = {200: [], 300: [], 400: [], 500: []}
#     with open(input_filename, 'r') as file:
#         for line in file:
#             # Оставляем только цифры в конце строки
#             status = int(line.strip()[-3:])
#             # Добавляем строку в соответствующий список
#             if status in status_lines:
#                 status_lines[status].append(line)
#     # Записываем строки в соответствующие файлы
#     for status, lines in status_lines.items():
#         with open(status_files[status], 'w') as file:
#             file.writelines(lines)
# split_file_by_status('random_strings.txt')

# задание 1, лекция 7
# name=input("write the name: ")
# var1 = lambda name: f"Hello, {name}"
# print (var1(name))

# задание 2, лекция 7
# list_of_names = [
#     "Dzina", "Masha", "Nastya", "Anton", "Anna",
#     "Andrey", "Arina", "Elena", "Roman","Gleb",
#     "Lev", "Nikolay", "Polina", "Yrua", "Anton"
# ]
# greet=lambda names:list(map(lambda name: f"Hello, {name}", names))
# names_new=greet(list_of_names)
# print (names_new)

# задание 3, лекция 7
# def pos_numbers (numbers):
#     return (num for num in numbers if num > 0)
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# positive_numbers = pos_numbers(numbers)
# positive_list=list (positive_numbers)
# print (positive_list)

# задание 4, лекция 7
# excluded_word = "the"
# sentence = "the quick brown fox jumps over the lazy dog"
# def lengths_of_words (sentence, excluded_word):
#     try:
#         words = sentence.split()  # разбитие строки на слова
#         filtr_words=[word for word in words if word != excluded_word] # фильтрация слов, исключая указанное слово
#         if not filtr_words: #проверка остались ли слова после фильтрации 
#             raise ValueError ("no words left after excluding")
#         lengths = [len(word) for word in filtr_words]
#         return lengths
#     except Exception as e:
#         print(f"an error occurred: {e}")        
# lengths = lengths_of_words (sentence, excluded_word)
# print(lengths)

# задание 5, лекция 7
# import string
# def encode(text, step):
#     code = ""
#     for var1 in text:
#         if var1 in string.ascii_lowercase:
#             number_symbol = ord(var1) + step
#             if number_symbol > ord('z'): # обработка переполнения для строчных букв
#                 number_symbol -= 26
#             elif number_symbol < ord('a'):
#                 number_symbol += 26
#             code += chr(number_symbol)
#         elif var1 in string.ascii_uppercase:
#             number_symbol = ord(var1) + step
#             if number_symbol > ord('Z'):  # обработка переполнения для заглавных букв
#                 number_symbol -= 26
#             elif number_symbol < ord('A'):
#                 number_symbol += 26
#             code += chr(number_symbol)
#         else:
#             code += var1
#     return code
# text = input("Enter the text to encode: ")
# step = int(input("Enter the shift step: "))
# encoded_text = encode(text, step)
# print("Encoded text:", encoded_text)
 
