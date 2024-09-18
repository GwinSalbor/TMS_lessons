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

        # print (f"The character '{var1}' is at position {ord(var1)}")
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

# for i in string.ascii_lowercase
# string.ascii_lowercase

# text = "Hello, World!"

# for char in text:
#     print(f"The character '{char}' is at position {ord(char)}")
          
# char2 = char + 1
# print(char2)
    
    # """
    # 1) iterate over text - пройтись по каждой букве текста
    # 2) функцией ord узнать ее место
    # 3) добавить шаг к позици буквы
    # 3.1) конец алфавита 
    # 3.2) мпец-символ
    # 4) получить букву по позиции
    # 5) собрать и вернуть текст
    # """


# def caesar_cipher(text, shift):
#     result = ""
    
#     # Проходим по каждому символу в тексте
#     for char in text:
#         # Если символ - буква
#         if char.isalpha():
#             # Определяем базу (для прописных или строчных букв)
#             base = ord('A') if char.isupper() else ord('a')
            
#             # Смещаем символ с учетом базы и кругооборота через весь алфавит (26 букв)
#             result += chr((ord(char) - base + shift) % 26 + base)
#         else:
#             # Если это не буква (например, пробел или знак препинания), добавляем символ без изменений
#             result += char
    
#     return result

# # Пример использования
# text = "Привет, Мир!"
# shift = 3

# # Шифрование
# encrypted_text = caesar_cipher(text, shift)
# print("Зашифрованный текст:", encrypted_text)

# # Дешифрование (сдвиг на обратное количество символов)
# decrypted_text = caesar_cipher(encrypted_text, -shift)
# print("Расшифрованный текст:", decrypted_text)

text = "привет мир"
index = text.find("мир")
print(index)

x = [1, 2, 3, 4, 5, 6]
for i in range(len(x)):
    print(i)

captains = ['Vorobey', 'Bones', 'Costa']
for i in captains:
    print(i)