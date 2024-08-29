"""
Задача *
надо создать функцию которая принимает строку,
разбивает ее на символы и возвращает частоту встечания каждого символа
"""

my_string = input('Enter a word: ')


def symbol_counter(symbol):

    symbol_count = {}

    for i in symbol:
        if i in symbol_count:
            symbol_count[i] += 1
        else:
            symbol_count[i] = 1

    return symbol_count


print(symbol_counter(my_string))
