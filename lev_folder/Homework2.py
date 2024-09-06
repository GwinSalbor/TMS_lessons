#Задание 1

user_input = input("Введите сообщение: ")

if user_input.lower() == "hello":
    print("Hello!")
elif user_input.lower() == "как дела?":
    print("У меня все хорошо, спасибо!")
elif user_input.lower() == "пока":
    print("До свидания!")
elif user_input.lower() == "что нового?":
    print("Все по-прежнему, а у вас?")
else:
    print("Извините, я не понимаю.")


#Задание 2

def chat_bot():
    while True:
        user_input = input("Введите сообщение: ")

        if user_input.lower() == "hello":
            print("Hello!")
        elif user_input.lower() == "как дела?":
            print("У меня все хорошо, спасибо!")
        elif user_input.lower() == "пока":
            print("Пока!")
            break  # Выход из цикла при прощании
        elif user_input.lower() == "что нового?":
            print("Все по-прежнему, а у вас?")
        elif user_input.startswith("Привет"):
            print("Привет! Как я могу помочь?")
        elif user_input.endswith("Лев"):
            print("О, Лев, рады приветствовать вновь!")
        else:
            print("Извините, я не понимаю.")

chat_bot()


#Задание 3

#разделение по пробелам

string = input("ВВеди сюда строку: ")
array = string.split()
print("Вот эта же строка в массиве: ", array)

#разделение по запятой

string = input("ВВеди сюда строку: ")
array = string.split(',')
print("Вот эта же строка в массиве: ", array)

#Задание 4
list = ['Ivan', 'Ivanou']
string1 = 'Minsk'
string2 = 'Belarus'
print(f'Привет, {list[0]} {list[1]}! Добро пожаловать в {string1} {string2}!')

#Задание 5
Random_list = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
result_string = " ".join(Random_list)
print(result_string)

#Задание 6
list_numbers = [1, 2 , 3, 4, 5, 6, 7, 8, 9, 10]

list_numbers.insert(2, 198)

removed_element = list_numbers.pop(3)

print(list_numbers)
print(removed_element)

#Задание 7
list_of_values = []
for i in range(10):
    var1 = input('Введите значение: ')
    list_of_values +=  var1
print(list_of_values)
print(sorted(list_of_values))
