int_var = 1
str_var = "antoha"
float_var = 0.323232
bool_var = True
list_var = [1, 2, 3]
set_var = (1, 2, 3)
dict_var = {"a": 1, "b": 2, "c": 3}

apple = 3
orange = 2
kiwi = 5
peach = 2
apple_coast = 5.99
orange_coast = 4.49
kiwi_coast = 7.99
peach_coast = 6.49
sum_buy = (
    apple * apple_coast
    + orange * orange_coast
    + kiwi * kiwi_coast
    + peach * peach_coast
)

a = 5
b = a + 3
c = a + b

apple_str = "apple"
orange_str = "orange"
kiwi_str = "kiwi"
peach_str = "peach"

print("1. Пункт первый домашнего задания")
print(f"Тип переменной int_var --> {type(int_var)}")
print(f"Тип переменной str_var --> {type(str_var)}")
print(f"Тип переменной float_var --> {type(float_var)}")
print(f"Тип переменной bool_var --> {type(bool_var)}")
print(f"Тип переменной list_var --> {type(list_var)}")
print(f"Тип переменной set_var --> {type(set_var)}")
print(f"Тип переменной dict_var --> {type(dict_var)}")
print()
print("2. Пункт второй домашнего задания")
print(f"Результат сложения переменных int и float --> {int_var + float_var}")
print(f"Результат разницы переменных int и float --> {int_var - float_var}")
print(f"Результат умножнния переменных int и float --> {int_var * float_var}")
print(f"Результат деления переменных int и float --> {int_var / float_var}")
print(f"Результат возведения переменную int в степень переменной float --> {int_var ** float_var}")
print()
print("3. Пункт третий домашнего задания")
print(f"Я купил {apple} яблока по стоимости {apple_coast} за одно")
print(f"{orange} апельсина по стоимости {orange_coast} за один")
print(f"{kiwi} киви по стоимости {kiwi_coast} за одно")
print(f"{peach} персика по стоимости {peach_coast} за один")
print(f"Общая сумма покупок вышла {round(sum_buy, 2)}")
# вопрос, почему в последнем принте выдает консоль много цифр после запятой, пришлось использовать функцию round()
print()
print("4. Пункт четвертый домашнего задания")
print(f"Первая переменная a = {a}, вторая b = {b}, третья переменная c = {c}")
print()
print("5. Пункт пятый домашнего задания")
print(f"I have a: {apple_str}, {orange_str}, {kiwi_str}, {peach_str}")
