
# class Vehicle:
#     def vehicle_method(self):
#         print("Vehicle class")
#     def drive(self):
#         print("brbrb")
# class Car(Vehicle):
#     def car_method(self):
#         print("Car class")
# class Toyota(Car):
#     def toyota_method(self):
#         print("Toyota class")


# car_a = Toyota()
# # car_a.drive()

# print(Toyota.__mro__)


# class O: ...
# class A(O):
#     def go(self):
#         pass
# class B(O): ...
# class C(O): ...
# class D(O): ...
# class E(O): ...
# class K1(A, B, C):
#     pass
# class K2(B, D):
#     def go(self):
#         pass
# class K3(C, D, E):
#     def go(self):
#         pass
# class K(K1, K2, K3): ...

# # print(K.__mro__)

# def print_mro(T):
#     print(*[c.__name__ for c in T.mro()], sep=' -> ')
# print_mro(K)


# class Sim:
#     population = 0
#     asd = 10

#     def __init__(self, name):
#         self.name = name
#         self.population += 10
#         Sim.population += 1

#     def introduce(self):
#         print(f"I'm {self.name}")

#     @classmethod
#     def get_population(cls):
#         print(f"Total sim class value: {cls.population} , {cls.asd}")
    

#     def get_population1(self):
#         print(f"Total sim object value: {self.population}")
    
    
#     def __add__(self,other):
#         return self.name + " " + other.name
#         # return Sim(self.name + " " + other.name)


#     @staticmethod
#     def is_adult(age):
#         return age >= 18



# person1 = Sim("sim1")
# person2 = Sim("sim2")
# p3 = person1 + person2

# print(p3)
# # person3 = Sim("sim3")


# Sim.get_population()
# print(person1.is_adult(19))
# person2.introduce()
# person1.get_population1()
# Sim.population +=10
# person2.population +=15

# Sim.get_population()
# person1.get_population1()
# person2.get_population1()


## ABC
from abc import ABC, abstractmethod

# Абстрактный класс Animal
class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Метод, который должен быть реализован в дочернем классе"""
        pass

    @abstractmethod
    def move(self):
        """Метод для передвижения"""
        pass


# Класс Dog, наследующий от Animal
class Dog(Animal):
    hunger = 10
    def sound(self):
        return "Гав-гав"

    def move(self):
        return "Бегает на четырех лапах"
    def asd(self):
        print("asd")

class mops(Dog):
    hunger = None
    clean = "yes"
    def asd(self):
        pass
    def sound(self):
        return "хрю хрю]"


d1 = Dog()
print(d1.hunger)  # Output: Гав-гав
# print(d1.move()) 
# print(d1.asd()) 
d2 = mops()
print(d2.hunger)  # Output: Гав-гав
print(d2.clean)

print(d1.clean) 
# # Класс Bird, наследующий от Animal
# class Bird(Animal):
#     # pass
#     def sound(self):
#         return "Чирик-чирик"

#     def move(self):
#         return "Летает"

# # Пример использования
# dog = Dog()
# print(dog.sound())  # Output: Гав-гав
# print(dog.move())   # Output: Бегает на четырех лапах

# bird = Bird()
# print(bird.sound()) # Output: Чирик-чирик
# print(bird.move())  # Output: Летает


#dataclass
# from dataclasses import dataclass

# @dataclass
# class Person:
#     """as"""
#     name: str
#     age: int
#     height: float = 1.75  # default

# __init__ 
# person1 = Person(name="Анна", age=25)
# person2 = Person(name="Иван", age=30, height=1.80)
# person3 = Person(name="Иван", age=30, height=1.80)

# # Автоматически сгенерированные методы
# # # __repr__
# # print(person1)  # Output: Person(name='Анна', age=25, height=1.75)
# # print(person2)  # Output: Person(name='Иван', age=30, height=1.8)

# # # Сравнение объектов
# # # __eq__
# # print(person1 == person2)  # Output: False
# # print(person3 == person2)
# # # Доступ к атрибутам
# # # getter
# # print(person1.name)  # Output: Анна
# # print(person2.height)  # Output: 1.8

# print(person3.name)
# person3.name = "qwe"
# print(person3.name)


# __init__ __new__ 
# __str__ __repr__
# __eq__


# class Point:

#     def __init__(self, x=0, y=0):
#         print("вызов __init__ для " + str(self))
#         self.x = x
#         self.y = y

# pt = Point(1, 2)
# print(pt)