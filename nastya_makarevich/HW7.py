#lambda task1
p1 = lambda name: print(f'Hello, {name}.')
p1('Nastya')

#lambda task2
list_of_names = ["Sacha", "Marina", "Ivanna"]
p2 = list(map(lambda name: 'Hello, ' + name, list_of_names))
print(p2)

#generator task1
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
def p3_gen():
    for number in numbers:
        if number > 0:
            yield number
positive_numbers = []

p3 = p3_gen()
for i in p3:
    positive_numbers.append(i)
print(positive_numbers)

#generator task2
sentence = 'theguick brown fox jamps over the lazy dog'
def p4(text):

    lst = text.split()
    result = []
    for word in lst:
        try:
            if word.lower() == "the":
                raise Exception("'the' исключается из результата расчета ")
            else:
                result.append(len(word))
        except Exception as a:
            print(a)
    return result
print(p4(sentence))

# code and decode Шифр Цезаря

text = "Hello, World!"
shift = 4

def encrypt_caesar(text, shift):

    encrypted_text = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

encrypted_text = encrypt_caesar(text, shift)
print("Encrypted result: " + encrypted_text)

def decrypt_caesar(encrypted_text, shift):
    return encrypt_caesar(encrypted_text, -shift)

decrypted_text = decrypt_caesar(encrypted_text, shift)
print("Decrypted result : " + decrypted_text)
