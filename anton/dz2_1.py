flag = True

while flag:

    text_console = input()

    lower_text_console = text_console.lower()

    if lower_text_console == 'hello':
        print('--> Hello, man')
    elif 'my name is' in lower_text_console:
        a = text_console.split(' ')
        print(f'--> Nice to meet you {a[-1]}')
    elif lower_text_console == 'bye':
        print('--> Bye-bye!')
        flag = False
    else:
        print('--> Text me something else')