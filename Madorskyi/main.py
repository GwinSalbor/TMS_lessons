def encode(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decode(text, shift):
    return encode(text, -shift)


encoded_text = encode("Hello, World!", 3)
print("Encoded:", encoded_text)

decoded_text = decode(encoded_text, 3)
print("Decoded:", decoded_text)

print()

encoded_text = encode("this is a test string", 5)
print("Encoded:", encoded_text)

decoded_text = decode(encoded_text, 5)
print("Decoded:", decoded_text)