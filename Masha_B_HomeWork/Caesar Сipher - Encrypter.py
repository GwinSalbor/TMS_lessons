def caesar_cipher(my_string, position):
    full_string = "abcdefghijklmnopqrstuvwxyz"
    summary = ''
    for i in my_string:
        if i in full_string:
            new_position = (full_string.index(i) + position) % 26
            summary += full_string[new_position]
        else:
            summary += i

    return summary


my_string = input("Enter a string: ")
position = int(input("Enter a position: "))
print(caesar_cipher(my_string, position))


