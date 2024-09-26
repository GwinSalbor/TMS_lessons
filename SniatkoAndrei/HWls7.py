##1.1 Cоздай функцию lambda, которая принимает на вход имя и выводит его в формате "Hello, {name}"

func_l = lambda name: f"Hello, {name}"
print(func_l("Andrzej"))  # Выведет: Hello, Andrzej

##1.2 Cоздай функцию lambda, которая принимает на вход список имен и выводит их в формате "Hello, {name}" в другой список

func1_l = lambda names: list(map(lambda name: f"Hello, {name}", names))
names = ["Andrzej", "Hanna", "Iwona", "Szymon"]
funk_hi = func1_l(names)
print(funk_hi)  # Выведет: ['Hello, Andrzej', 'Hello, Hanna', 'Hello, Iwona', 'Hello, Szymon']

##1.3 Напишите генератор, который принимает список
    # numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    # и возвращает новый список только с положительными числами.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers = (num for num in numbers if num > 0)
# Для получения списка из генератора
positive_list = list(positive_numbers)
print(positive_list)

##1.4 Необходимо составить список чисел, которые указывают на длину слов в строке:
    #sentence = "the quick brown fox jumps over the lazy dog",
    #но только если слово не "the", с обработкой исключений.

sentence = "the quick brown fox jumps over the lazy dog"
def word_lengths(sentence):
    try:
        # Разбиваем строку на слова
        words = sentence.split()
        # Используем list comprehension для создания списка длин слов
        lengths = [len(word) for word in words if word.lower() != "the"]
        return lengths
    except Exception as e:
        print(f"Произошла ошибка: {e}")
# Вызываем функцию и выводим результат
lengths = word_lengths(sentence)
print(lengths)
