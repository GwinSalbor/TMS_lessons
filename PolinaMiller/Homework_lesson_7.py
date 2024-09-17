# Задание 1. Lambda
#Определение лямбда-функции
greeting = lambda name: f"Hello, {name}"

#Применение
print(greeting("Polina"))

#Задание 2. Lambda
#Список имен
names = ["Polina","Nino","Irakli"] 

#Применение лямбда-функции в map
greeting_list = list(map(lambda name:f"Hello, {name}", names))

#Применение
print(greeting_list)

#Генератор. Задание 1
def positive_numbers_gen (numbers):
    for number in numbers:
        if number >0:
            yield number

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

#Создание генератора
positive_generator = positive_numbers_gen (numbers)

#Создание нового списка с положительными числами
positive_num_list = list(positive_generator)

#Вывод нового списка
print(positive_num_list)


#Задание Шифр Цезаря
def encode(text, shift):
    encoded_chars = [] 
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            # Определяем, базовый код для заглавных и строчных букв
            base = ord('A') if char.isupper() else ord('a')
            # Сдвигаем букву и добавляем её в список
            new_char = chr((ord(char) - base + shift) % 26 + base)
            encoded_chars.append(new_char)
        else:
            # Если это не буква, просто добавляем её как есть
            encoded_chars.append(char)
    return ''.join(encoded_chars)  # Преобразуем список букв в строку и возвращаем

def decode(text, shift):
    decoded_chars = [] 
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            # Определяем, базовый код для заглавных и строчных букв
            base = ord('A') if char.isupper() else ord('a')
            # Сдвигаем букву обратно и добавляем её в список
            new_char = chr((ord(char) - base - shift) % 26 + base)
            decoded_chars.append(new_char)
        else:
            # Если это не буква, просто добавляем её как есть
            decoded_chars.append(char)
    return ''.join(decoded_chars)  # Преобразуем список букв в строку и возвращаем

# Тестируем шифрование и расшифрование
text = "Hello, World!"
shift = 3

encoded_text = encode(text, shift)
print(f"Encoded: {encoded_text}")

decoded_text = decode(encoded_text, shift)
print(f"Decoded: {decoded_text}")
