"""
Создайте программу, которая читает содержимое текстового файла который вы сгенерировали
в задании выше и разбивает его на несколько файлов для статусов 200, 300, 400, 500
- соответственно, в зависимости от того какой статус находится в конце строки.
"""


def reading_and_splitting(my_file):
    with open(my_file, 'r') as f:
        for i in f:
            if '200' in i:
                with open('200.txt', 'a') as file_200:
                    file_200.write(i)
            elif '300' in i:
                with open('300.txt', 'a') as file_300:
                    file_300.write(i)
            elif '400' in i:
                with open('400.txt', 'a') as file_400:
                    file_400.write(i)
            if '500' in i:
                with open('500.txt', 'a') as file_500:
                    file_500.write(i)


reading_and_splitting('test.txt')
