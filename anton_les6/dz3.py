"""
Создайте функцию которая будет генерировать случайные строки с помощью функции рандом 
random.choice() - и модуля string который я описал в подсказках 
создайте функцию которая будет записывать строки в файл
в цикле for сгенерируйте несколько строк и запишите их в файл, в случайном порядке 
добавляйте к строке в конце числа 200, 300, 400, 500
Усложнение: 
1) сделайте так, чтобы можно было задавать вероятности с которыми в конце строки будет значение  200, 300, 400, 500
2) добавьте в начало каждой строки дату и время используя модуль datetime с прошлого урока
"""

import random, string, datetime

def generate_str_in_file(list_of_allphabet: list):
    """
    Функция на вход принимает лист определенных символов,
    генерирует рандомной длины слова из рандомных значений из этого листа,
    составляет из них рандомное количество строк, добавляя при этом в
    начале строки дату и время создания, в конце строки рандомный статус:
    200, 300, 400, 500. После выполнения всех действий, функция ничего не 
    возвращает, но записывает сгенерированные строки в файл hello.txt
    """

    random_count_of_string = random.randint(2, 5)

    list_of_random_string = []
    list_of_big_string = []
    exit_list = []

    for k in range(random_count_of_string):
        small_random_int = random.randint(3, 5)

        for i in range(small_random_int):
            big_random_int = random.randint(5, 15)

            for j in range(big_random_int):
                random_letters = random.choice(list_of_allphabet)
                list_of_random_string.append(random_letters)

            big_string = ''.join(list_of_random_string)
            list_of_random_string = []
            list_of_big_string.append(big_string)

        value_random_int = random.randint(2, 5)

        match value_random_int:
            case 2:
                list_of_big_string.append('200')
            case 3:
                list_of_big_string.append('300')
            case 4:
                list_of_big_string.append('400')
            case 5:
                list_of_big_string.append('500')

        dt = str(datetime.datetime.now())

        list_of_big_string.insert(0, str(dt[:-7]))

        exit_list.append(' '.join(list_of_big_string))
        list_of_big_string = []

    with open("hello.txt", "w") as my_file:
        my_file.write('\n'.join(exit_list))


list_of_allphabet = string.ascii_letters
generate_str_in_file(list_of_allphabet)
