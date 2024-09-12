"""
Создайте программу, которая читает содержимое текстового файла 
который вы сгенерировали в задании выше и разбивает его на несколько 
файлов для статусов 200, 300, 400, 500 - соответственно, в зависимости 
от того какой статус находится в конце строки.
"""

with open("hello.txt", "r") as my_file:

    for i in my_file:
        str_without_n = i.replace('\n', '')
        mylist = str_without_n.split(' ')
        match mylist[-1]:
            case '200':
                with open("status/status200.txt", "a") as file_status:
                    file_status.write(str_without_n + '\n')

            case '300':
                with open("status/status300.txt", "a") as file_status:
                    file_status.write(str_without_n + '\n')

            case '400':
                with open("status/status400.txt", "a") as file_status:
                    file_status.write(str_without_n + '\n')

            case '500':
                with open("status/status500.txt", "a") as file_status:
                    file_status.write(str_without_n + '\n')




