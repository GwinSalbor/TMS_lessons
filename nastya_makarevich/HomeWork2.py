#Задание 3 Перевести строку в массив
def string_to_array(s):
    return s.split()

string1 = "Robin Singh"
array1 = string_to_array(string1)
print(array1)

string2 = "I love arrays they are my favorite"
array2 = string_to_array(string2)
print(array2)

#Задание 4
names = ['Ivan', 'Ivanou']
city = "Minsk"
country = "Belarus"

hello = ("Привет, {} {}! Добро пожаловать в {} {}.".format(names[0], names[1], city, country))
print(hello)

#Задание 5
lst = ["I", "love", "arrays", "they", "are", "my", "favorite"]
string3 = ' '.join(lst)
print(string3)

#Задание 6
lst1 = ["a", "b", "c", "d", "i", "f", "g", "k", "l", "m"]
lst1.insert(2, "K")
print(lst1)

#Задание7
lst_my = []
for i in range(10):
    lst_my.append(int(input(f'Введите 10 элементов {i + 1}: ')))
print(sorted(lst_my))

#Задание 1
def chat_bot():
    print('Привет! Я chatbot. Чем могу тебе помочь?')
    while True:
        user_input = input('Вы: ').strip().lower()

        if user_input == 'привет' or user_input == 'hello':
            print('Бот: Привет! Чем могу вам помочь?')
        elif user_input == 'как дела?':
            print('Бот: Всё в порядке, спасибо! Как могу помочь вам сегодня?')
        elif user_input == 'пока':
            print('Бот: Пока! Если у вас есть вопросы или что-то, чем я могу помочь, дайте знать!')
            break
        elif user_input == 'помоги':
            print('Бот: Чем я могу помочь?')
        elif user_input == 'что ты умеешь?':
            print('Бот: Я могу поболтать или помочь с информацией или советами.')
        else:
            print('Бот: Напишите, что вас интересует?')
chat_bot()

