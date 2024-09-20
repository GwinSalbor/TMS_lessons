from typing import Generator
# 1. lambda функция

hello = lambda name: f"Hello, {name}"
print(hello("lev"))

# 2. Cоздать lambda функцию, которая принимает на вход список имен и выодит их в формате "Hello, {name}" в другой список
names = ["Дима", "Лев", "Ярослав", "Анна"]
hello_names = list(map(lambda name: f"Hello, {name}", names))

print(hello_names)

#3. Напишите генератор, который принимает список и возвращает новый список только с положительными числами


def positive_numbers() -> Generator[float, None, None]:
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    for num in numbers:
        if num > 0:
            yield num
positive_numbers_generator = list(positive_numbers())
print(positive_numbers_generator)

#4. Необходимо составить список чисел которые указывают на длину слов в строке: sentence = " thequick brown fox jumps over the lazy dog", но только если слово не "the" с обработкой исключений

def word_lengths(sentence):
    try:
        # Проверяем, что строка не пустая
        if not sentence:
            raise ValueError("Строка не должна быть пустой.")
        
        # Разбиваем строку на слова
        words = sentence.split()
        
        # Составляем список длины слов, исключая "the"
        lengths = []
        for word in words:
             if word.lower() != "the":
                 lengths.append(len(word))
        
        return lengths
    
    except ValueError as e:
        print(f"Ошибка: {e}")
        return []

sentence = "the quick brown fox jumps over the lazy dog"
lengths = word_lengths(sentence)
print(lengths)

#5. Шифр Цезаря

import string
text = "hello world"
def encode(text, step):
    code = ""
    for var1 in text:
        number_symbol = ord(var1)
        number_symbol +=  step
        chr(number_symbol)
        code += chr(number_symbol)

    return code

        
def decode(text, step):

    code = ""
    for var1 in text:
        number_symbol = ord(var1)
        number_symbol -=  step
        chr(number_symbol)
        code += chr(number_symbol)

    return code

print(encode(text, 1))
var2 = encode("Hello, guys", 5)
print(var2)
var_decode = decode(var2, 5)
print(var_decode)