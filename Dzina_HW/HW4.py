# #1-2



# 3
# "Robin Singh" ["Robin", "Singh"] 
# "I love arrays they are my favorite"  ['I', "love", "arrays", "they", "are", "my", "favorite"] 
variable=("Robin Singh")
print(variable.split())

variable1=("I love arrays they are my favorite")
print(variable1.split())



#4 
#  ["Ivan", "Ivanou"] и 2 строки: Minsk, Belarus
#  "Привет, Ivan Ivanou!  Добро пожаловать в Minsk Belarus"
name=["Ivan", "Ivanou"]
city="Minsk"
country="Belarus"
print(f"Привет, {name[0]} {name[1]}!  Добро пожаловать в {city} {country}!")
    


#5
# ['I', "love", "arrays", "they", "are", "my", "favorite"] сделать сроку
# "I love arrays they are my favorite"

variable1=['I', "love", "arrays", "they", "are", "my", "favorite"]
# string=""
# for i in variable1:
#     string +=i
#     string +=" "
# print(string)
print(" ".join(variable1))

#6
new_list=["juice", "fruits", "vegetables", "eggs", "milk", "chocolate", "oil", "bread", "meat", "water"]
new_list.insert(3, "salt")
print(new_list)
del new_list[2]
print(new_list)


#7
