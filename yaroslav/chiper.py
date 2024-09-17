from collections import defaultdict
import string

letter_frequency = {
    'E': 12.70,
    'T': 9.06,
    'A': 8.17,
    'O': 7.51,
    'I': 6.97,
    'N': 6.75,
    'S': 6.33,
    'H': 6.09,
    'R': 5.99,
    'D': 4.25,
    'L': 4.03,
    'C': 2.78,
    'U': 2.76,
    'M': 2.41,
    'W': 2.36,
    'F': 2.23,
    'G': 2.02,
    'Y': 1.97,
    'P': 1.93,
    'B': 1.49,
    'V': 0.98,
    'K': 0.77,
    'J': 0.15,
    'X': 0.15,
    'Q': 0.10,
    'Z': 0.07
}


text = """In the beginning, there was a man who knew nothing of the world around him. His eyes opened to the sky, and he wondered what lay beyond the stars. The winds whispered secrets, the rivers carried stories, and the mountains stood as ancient sentinels guarding the history of the earth. As the days passed, the man learned the ways of the world, how the sun rose in the east and set in the west, how the moon followed its path across the night sky, and how the seasons changed. The trees shed their leaves in autumn, the flowers bloomed in spring, and life continued in a cycle as old as time itself.

He watched the birds take flight, soaring above the land, free to explore the vast expanse of the horizon. He marveled at the creatures of the forest, each with its own unique rhythm and purpose. The wolves howled to the moon, the deer grazed in the meadow, and the streams flowed endlessly through the valleys. The man felt a connection to the world, as though he were a part of something greater than himself. He found solace in the quiet moments, when the wind brushed against his skin and the sun warmed his face. He listened to the sounds of the earth, the rustling of leaves, the chirping of insects, and the distant call of an owl.

Time moved forward, and the man grew older, but his wonder never faded. He continued to explore, to seek out new horizons, and to learn from the world around him. With each passing day, he understood a little more about the mysteries of life, but he also realized that some things would forever remain beyond his grasp. The stars, the sky, the universe — all of it stretched out before him, vast and infinite, and yet, he knew that he was but a small part of a much larger whole.
"""
text=text.lower()

# text = "qwezxchfghrkk"
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
    return ''.join(decoded_chars) 

import time
def decorator(fun): # 1 в функцию можно передавать другую функцию, 2 функция может возвращать другую функцию
    def inner(*args, **kwargs): # *args, **kwargs 
        begining = time.time()
        result = fun(*args, **kwargs)
        end = time.time()
        print(f"execution time: {end-begining}")
        return result
    return inner

cracker_letters_frequency = defaultdict(int)
@decorator
def cracker(text):
    real_len = 0
    for i in text:
        if i in string.ascii_letters:
            real_len+=1
            cracker_letters_frequency[i] += 1
    max = 0
    expected_e = ""
    for letter, frequency in cracker_letters_frequency.items():
        temp = frequency/real_len 
        cracker_letters_frequency[letter] = temp
        if max < temp:
            max = temp
            expected_e = letter
    shift = ord(expected_e) - ord("e")
    return shift, max


chiper = encode(text,1)

print(cracker(chiper))