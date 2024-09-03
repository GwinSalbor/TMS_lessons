#Задание 3 Перевести строку в массив
def string_to_array(s):
    return s.split()

string1 = "Robin Singh"
array1 = string_to_array(string1)
print(array1)

string2 = "I love arrays they are my favorite"
array2 = string_to_array(string2)
print(array2)

#Задание 4
names = ['Ivan', 'Ivanou']
city = "Minsk"
country = "Belarus"

hello = ("Привет, {} {}! Добро пожаловать в {} {}".format(names[0], names[1], city, country))
print(hello)

#Задание 5
lst = ["I", "love", "arrays", "they", "are", "my", "favorite"]
string3 = ' '.join(lst)
print(string3)

#Задание 6
lst1 = ["a", "b", "c", "d", "i", "f", "g", "k", "l", "m"]
lst1.insert(2, "K")
print(lst1)



