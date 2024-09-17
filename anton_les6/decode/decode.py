import string

def encode(text: str):

    list_of_new_chrs = []

    for j in range(1, 26):

        for i in text:

            if i.isalpha():
                position_encode_ascii = ord(i) - j

                if position_encode_ascii <= start_of_ascii_lover_reg:
                    difference_of_position = start_of_ascii_lover_reg - position_encode_ascii
                    position_encode_ascii = ord("z") - difference_of_position

                i_new = chr(position_encode_ascii)
                list_of_new_chrs.append(i_new)

            else:
                list_of_new_chrs.append(i)
    
        encode_text = "".join(list_of_new_chrs)
        list_of_new_chrs = []
        print(f'\n{text} --> {encode_text} --> {j}')

start_of_ascii_lover_reg = 96

text = "spwwz, hzcwo! t'x dz slaaj!!@"
text_alphabet = string.ascii_lowercase

encode(text)