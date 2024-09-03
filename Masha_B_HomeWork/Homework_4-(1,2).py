"""
Напишите небольшой чат бот, который будет принимать строку из консоли и в зависимости от того,
что написал пользователь, будет отвечать. Например: если в консоль ввели "Hello",
надо ответить "Hello", придумайте еще несколько фраз и сделайте условный оператор
if или elif для покрытия нескольких вариантов ввода. Подсказка, лучше привести строку
к нижнему регистру, чтобы при сравнении строк hello и Hello не отличались.
"""

my_string = input("Type something...").capitalize()

if my_string == "Hello":
    print("Hello")
elif my_string == "How are you?":
    print("I'm doing good and how are you?")
    response = input("Type something...").capitalize()
    print("Nice!")
elif my_string == "What is the weather?".capitalize():
    print('You can check it here - https://weather.com/')
else:
    print("Sorry, I don't understand that.")

phone = input("What's your phone number... +..?").capitalize()
if phone.startswith('+48'):
    print("Oh..you are from Poland that's cool")
else:
    print("Sooo, you're not from Poland, I see...")

