def ceaser_decrypter(my_string, position):
        full_string = "abcdefghijklmnopqrstuvwxyz"
        summary = ''

        for i in my_string:
            if i in full_string:
                new_position = (full_string.index(i) - position) % 26
                summary += full_string[new_position]
            else:
                summary += i

        return summary


revert_my_word = ceaser_decrypter('ocujc',2)
print(revert_my_word)
