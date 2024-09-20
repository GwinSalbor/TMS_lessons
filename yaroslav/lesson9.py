# class Sim:
#     type = "sim"
#     sleep = 10
#     hunger = 10

#     def __init__(self, name: str, surname: str, age: int, sex: int, zodiac_sign):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.sex = sex
#         self.zodiac_sign = zodiac_sign
#         self.budget = 10
#         self._qwe = 10
#         self.__asd = 20
        
#     def action(self):
#         self.hunger -= 1
#         self.sleep -= 0.5
#         print("I did something")
    
#     def eat(self, food):
#         self.hunger += food.value
#         if self.hunger > 10:
#             print("I can not eat any more")
#             self.hunger = 10

#     def _give_money(self):
#         self.budget += 5000
#     def __give_money(self):
#         self.budget += 5000

#     def __repr__(self):
#         self.budget += 5000

#     @staticmethod
#     def hello(name):
#         return f"Hello {name}"

#     def go_sleep(self, time):
#         self.sleep += time
#         if self.sleep > 10:
#             print("I can not sleep any more")
#             self.sleep = 10
        
#     def status(self):
#         if self.sleep <3 or self.hunger < 3:
#             return "Bad"
#         elif self.sleep < 6 or self.hunger < 6:
#             return "Im fine" 
#         else:
#             return "Im Perfect)))"
    
#     def __str__(self) -> str:
#         return f"""{self.name}  sleep: {self.sleep}, hunger: {self.hunger} total: {self.status()}"""


# class Food:
#     def __init__(self, name, value) -> None:
#         self.name = name
#         self.value = value

# apple = Food("Apple", 1)
# pizza = Food("pizza", 5)
# chicken = Food("chicken", 4)
# anton = Sim("Anton", "Ant", 18, "M", "Virgo")
# masha = Sim("Masha", "qwe", 18, "F", "Water")
# anton.action()

# print(masha.hello(anton.name))


# class Car:
#     def __init__(self):
#         self.name = "corolla"
#         self.__make = "toyota"
#         self._model = 1999
    
#     def get(self):
#         return self._model
    
#     def setter(self, val):
#         self._model = val




# class Person:
#     def __init__(self, name):
#         self._name = name  # Protected variable (by convention, _ indicates it's internal)

#     # Getter method
#     def get_name(self):
#         return self._name

#     # Setter method
#     def set_name(self, name):
#         self._name = name


# class Person:
#     def __init__(self, name):
#         self._name = name

#     # Getter method
#     @property
#     def name(self):
#         return self._name

#     # Setter method
#     @name.setter
#     def name(self, name):
#         self._name = name

# Oleg = Person("Oleg")
# print(Oleg._Person__name)
# print(Oleg.get_name())
# Oleg.set_name("Vasya")
# print(Oleg.get_name())

# a = Person("Oleg")
# print(a.name)
# a.name = "Vasya"
# print(a.name)


# class Person:
#     def drive(self):
#         print("qweasd")

# class Car:
#     def __init__(self, name, fuel, fuel_amount):
#         self.name = name
#         self.fuel = fuel
#         self.fuel_amount = fuel_amount
    
#     def drive1(self):
#         self.fuel_amount -=10
#         print("br-br-br-br-br")

#     @staticmethod
#     def stop():
#         print("I'm stoped")

# class Tayota(Car):
#     def __init__(self,name, fuel, fuel_amount, volume):
#         super().__init__(name, fuel, fuel_amount)
#         self.volume = volume
    
#     @staticmethod
#     def stop():
#         print("i can not stop")


# class SuperCar(Tayota):
#     pass
# car_obj = Tayota(name = "Corola", fuel = "AI95", fuel_amount = 60, volume = 200)

# print(car_obj.fuel_amount)
# car_obj.drive()
# car_obj.stop()
# print(car_obj.fuel_amount)

from abc import ABC

class MyABC(ABC):
    pass

class Car:
    def drive(self):
        pass

    @staticmethod
    def stop():
        print("stop")

    def stats(self):
        print(self.fuel_amount)

class Skoda(Car):
    def __init__(self, name, fuel_amount):
        self.name = name
        self.fuel_amount = fuel_amount

    def drive(self):
        self.fuel_amount -= 5
        print("brbrb")

s = Skoda("t", 50)

s.drive()
s.stats()

