#region 1 

def chat_bot():
    print(
        "Привет! Я чат-бот. Вы можете поздороваться со мной, спросить как у меня дела, узнать мое имя или попрощаться. Для выхода введите 'exit' или 'выход'.")

    while True:
        user_input = input("Введите сообщение: ").strip().lower()

        if user_input in ["hello", "привет"]:
            if user_input == "hello":
                print("Hello!")
            else:
                print("Привет!")
        elif user_input in ["how are you?", "как дела?"]:
            if user_input == "how are you?":
                print("I'm a bot, so I don't have feelings, but thanks for asking!")
            else:
                print("Я бот, поэтому у меня нет чувств, но спасибо за вопрос!")
        elif user_input in ["what's your name?", "как тебя зовут?"]:
            if user_input == "what's your name?":
                print("I'm a simple chat bot created to assist you.")
            else:
                print("Я простой чат-бот, созданный чтобы помочь вам.")
        elif user_input in ["bye", "пока"]:
            if user_input == "bye":
                print("Goodbye! Have a great day!")
            else:
                print("До свидания! Хорошего дня!")
            break
        elif user_input in ["exit", "выход"]:
            if user_input == "exit":
                print("Exiting the chat. Goodbye!")
            else:
                print("Выход из чата. До свидания!")
            break
        else:
            if any(char in user_input for char in "abcdefghijklmnopqrstuvwxyz"):
                print("I'm sorry, I don't understand that.")
            else:
                print("Извините, я не понимаю это.")


if __name__ == "__main__":
    chat_bot()

#endregion]=

#region 2

str1 = "Robin Singh"
str_to_list1 = list(str1)

str2 = "I love arraty they are my favorite"
str_to_list2 = list(str2)

#endregion

#region 3

current_list = ['Ivan', 'Ivanov']
str_first = 'Belarus'
str_second = 'Minsk'

print(f'Привет {current_list[0]} {current_list[1]}! Добро пожаловать в {str_second} {str_first}!')
#endregion

#region 4

current_list = ['I', 'love', 'array', 'they', 'are','my', 'favorite']
list_to_string =' '.join(current_list)

print(list_to_string)
#endregione

#region 5

current_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

current_list.insert(3, 'K')

del current_list[3]

#endregion

#region 6

current_list = []

for _ in range(1, 11):
    current_list.append(input(f'Введите число: '))

print(current_list)
#endregion

#region 7

numbers = [1, 5, 2, 9, 2, 9, 1]

for number in numbers:
    if numbers.count(number) == 1:
        print(number)
        break

#endregion
