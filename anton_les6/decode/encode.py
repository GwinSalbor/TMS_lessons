import string

def encode(text: str, step: int):

    list_of_new_chrs = []

    for i in text:

        if i.isalpha():
            position_encode_ascii = ord(i) + step

            if position_encode_ascii >= end_of_ascii_lover_reg:
                difference_of_position = position_encode_ascii - end_of_ascii_lover_reg
                position_encode_ascii = ord("a") + difference_of_position

            i_new = chr(position_encode_ascii)
            list_of_new_chrs.append(i_new)
            print(f"{i}, {ord(i)} --> {i_new}, {position_encode_ascii}")

        else:
            print(f'{i} --> not a letter')
            list_of_new_chrs.append(i)

    encode_text = "".join(list_of_new_chrs)
    print(f'\n{text} --> {encode_text}')

end_of_ascii_lover_reg = 123

step = 11
text = "hello, world! i'm so happy!!@"
text_alphabet = string.ascii_lowercase

encode(text, step)