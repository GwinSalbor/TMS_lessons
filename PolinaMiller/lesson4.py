# Задание 1
def chat_bot():
    # Приветственное сообщение
    print("Привет! Я chatbot. Напиши мне что-нибудь.")

    while True:
        # Получаем ввод от пользователя
        user_input = input("Ты: ").strip().lower()  # Приводим ввод к нижнему регистру и убираем лишние пробелы

        # Проверка на разные фразы и ответ
        if user_input == "привет" or user_input == "hello":
            print("Бот: Привет! Как я могу помочь?")
        elif user_input == "как дела?":
            print("Бот: У меня всё отлично, спасибо! А у тебя?")
        elif user_input == "пока":
            print("Бот: Пока-пока! Хорошего дня!")
            break  # Завершаем работу бота
        elif user_input == "помоги":
            print("Бот: Чем я могу помочь? Расскажи мне.")
        elif user_input == "что ты умеешь?":
            print("Бот: Я могу приветствовать тебя, спрашивать, как у тебя дела, и помогать с вопросами.")
        else:
            print("Бот: Извини, я не понимаю твоего запроса. Попробуй ещё раз.")

# Запуск чат-бота
chat_bot()

# Задание 2
def chatbot():
    # Приветственное сообщение
    print("Привет! Я чат-бот. Напиши мне что-нибудь.")

    while True:
        # Получаем ввод от пользователя
        user_input = input("Ты: ").strip().lower()  # Приводим ввод к нижнему регистру и убираем лишние пробелы

        # Проверка на разные фразы и ответ
        if user_input.startswith("привет") or user_input.startswith("hello"):
            print("Бот: Привет! Как я могу помочь?")
        elif user_input.startswith("как дела"):
            print("Бот: У меня всё хорошо, спасибо! А у тебя?")
        elif user_input.startswith("пока"):
            print("Бот: Пока! Хорошего дня!")
            break  # Завершаем работу бота
        elif user_input.startswith("помоги"):
            print("Бот: Чем я могу помочь? Расскажи мне.")
        elif user_input.startswith("что ты умеешь"):
            print("Бот: Я могу приветствовать тебя, спрашивать, как у тебя дела, и помогать с вопросами.")
        elif user_input.startswith("расскажи о"):
            topic = user_input[len("расскажи о"):].strip()  # Извлекаем тему после "расскажи о"
            print(f"Бот: Рассказываю о {topic}. Это интересная тема!")
        elif user_input.startswith("скажи мне"):
            command = user_input[len("скажи мне"):].strip()  # Извлекаем команду после "скажи мне"
            print(f"Бот: Ты сказал мне: {command}")
        else:
            print("Бот: Извини, я не понимаю твоего запроса. Попробуй ещё раз.")

# Запускаем чат-бота
chatbot()

#Задание 3
def string_to_array(s):
    # Разбиваем строку на слова
    return s.split()

# Преобразуем строку "Robin Singh" в массив
string1 = "Robin Singh"
array1 = string_to_array(string1)
print(array1)  # Вывод: ['Robin', 'Singh']

# Преобразуем строку "I love arrays they are my favorite" в массив
string2 = "I love arrays they are my favorite"
array2 = string_to_array(string2)
print(array2)  # Вывод: ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']

# Задание 4
# Данные
names = ['Ivan', 'Ivanou']
city = "Minsk"
country = "Belarus"

# Форматирование строки с использованием метода format
greeting = "Привет, {} {}! Добро пожаловать в {}, {}".format(names[0], names[1], city, country)

print(greeting)

#Задание 5
# Данные
words = ["I", "love", "arrays", "they", "are", "my", "favorite"]

# Преобразование списка в строку с пробелами между словами
sentence = " ".join(words)

print(sentence)


# Задание 6
# Создание списка из 10 элементов
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Вставка нового значения на 3-ю позицию (индекс 2)
new_value = 'New'
my_list.insert(2, new_value)

print("Список после вставки нового значения:", my_list)

# Удаление элемента из списка под индексом 5
index_to_remove = 5
if 0 <= index_to_remove < len(my_list):
    del my_list[index_to_remove]
    print("Список после удаления элемента:", my_list)
else:
    print("Индекс вне диапазона списка.")


# Задание 7
def main():
    # Создание пустого списка
    user_list = []

    # Ввод 10 элементов от пользователя
    print("Введите 10 элементов для списка:")
    for i in range(10):
        element = input(f"Введите элемент {i+1}: ")
        user_list.append(element)

    # Сортировка списка
    user_list.sort()

    # Вывод отсортированного списка
    print("Отсортированный список:")
    print(user_list)

# Запуск программы
main()

# Задание 1*
def find_unique_number(numbers):
    unique_number = 0
    for number in numbers:
        unique_number ^= number
    return unique_number

# Пример массива чисел
numbers = [1, 5, 2, 9, 2, 9, 1]

# Находим и выводим уникальное число
unique_number = find_unique_number(numbers)
print("Уникальное число:", unique_number)


