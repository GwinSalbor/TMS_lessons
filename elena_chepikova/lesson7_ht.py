# Task 1: Create lambda function (for single variable)

task1 = lambda name: print(f"Hello, {name}")
task1("Ross") # Result: Hello, Ross

# Task 2: Create lambda function (for variables list)
list_of_names = ["Joe", "Monica", "Chandler"]
task2 = list(map(lambda name: "Hello, " + name, list_of_names))
print(task2) # Result: ['Hello, Joe', 'Hello, Monica', 'Hello, Chandler']

# Task 3: Generator that returns new list with positive numbers only
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

# Positive numbers generator from the given list
def task3_gen():
    for number in numbers:
        if number > 0:
            yield number

# Positive numbers list creation using positive numbers generator results
positive_numbers = []
task3 = task3_gen()

for i in task3:
    positive_numbers.append(i)
print(positive_numbers) # Result: [34.6, 44.9, 68.3, 44.6, 12.7]

# Task 4: Numbers list that return words length in the given string, except "the" - make exception
sentence = " thequick brown fox jumps over the lazy dog"

def task4(text):
# Given text is split to a list containing separate words
    lst = text.split()
    result = []
    for word in lst:
        try:
            if word.lower() == "the":
                raise Exception("'the' article is excluded from the calculation results")
            else:
# Words' length is calculated for every word which is not 'the' and written to results list
                result.append(len(word))
        except Exception as e:
            print(e)
    return result

print(task4(sentence))
# Results:
# 'the' article is excluded from the calculation results
# [8, 5, 3, 5, 4, 4, 3]

# Task 5: Caesar Cipher
initial_text = "Hello, World!"
shift = 3

def encrypt_caesar(initial_text, shift):
    """
    This function converts the given text into an encrypted line using Caesar cipher logic and specified shift
    """
    encrypted_text = ''
    for char in initial_text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char
    return encrypted_text

encrypted_text = encrypt_caesar(initial_text, shift)
print("Encrypted result: " + encrypted_text) # Encrypted result: Khoor, Zruog!

def decrypt_caesar(encrypted_text, shift):
    """
    This function decrypts the result of encrypt_caesar function using the Caesar cipher with the specified shift.
    """
    return encrypt_caesar(encrypted_text, -shift)

decrypted_text = decrypt_caesar(encrypted_text, shift)
print("Decrypted result : " + decrypted_text) # Decrypted result : Hello, World!