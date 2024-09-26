class Food:
    def __init__(self, name: str, value: int, cost: float):
        self.name = name
        self.value = value
        self.cost = cost


class Job:
    def __init__(self, name, salary, bladder_decreases=1, hunger_decreases=1, social_decreases=1, fun_decreases=1, hygiene_decreases=1):
        self.name = name
        self.salary = salary
        self.bladder_decreases = bladder_decreases
        self.hunger_decreases = hunger_decreases
        self.social_decreases = social_decreases
        self.fun_decreases = fun_decreases
        self.hygiene_decreases = hygiene_decreases

    def work(self, sim, hours):
        for _ in range(hours):
            sim.bladder -= self.bladder_decreases 
            sim.hunger -= self.hunger_decreases
            sim.social -= self.social_decreases
            sim.hygiene -= self.hygiene_decreases
            sim.energy -= self.fun_decreases
            sim.money += self.salary


from enum import Enum

class SimStatus(Enum):
    Perfect = 1
    NotGood = 2
    AlmostDead = 3
    Dead = 4


class Sim:
    type = "human"
    population = 0

    def __init__(self, name, surname, age, sex, zodiac):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac
        self._time = 0
        self._bladder = 10
        self._hunger = 10
        self._social = 10
        self._hygiene = 10
        self._energy = 10
        self.money = 100

        self.status = SimStatus.Perfect
        Sim.population += 1

    @property
    def bladder(self):
        return self._bladder

    @bladder.setter
    def bladder(self, value):
         # можно вызывать только когда мы сделали все изменяемые параметры приватными "начинаются с _ "
        # для того чтобы не вызывать повторно вызов сеттера
        if self._bladder < value:
            # мы тут сравниваем что нынешнее значение у сима "self._bladder" меньше чем "value" новое значение
            # если нынешнее значение меньше, значит мы только что увеличили этот показатель, делаем вывод - сим сходил в туалет
            print("наконец я сходил в туалет")
        elif self._bladder > value and 0< value < 3:
            # если нынешнее значение больше чем value - значит показатель нужды уменьшился
            # делаем такую проверку для того чтобы не писать что мы хотим в туалет 
            # если вдруг показатель увеличился на значение при котором мы не вышли за порог в 3
            # AND если value < 3 значит новое значение меньше порога в 3 - выводим что сим хочет в туалет
            print("I want to pee or poo")
            self.status = SimStatus.AlmostDead # меняем статус
        
        elif self._bladder > value and  value <=1:
            print("I'm dead")
            self.status = SimStatus.Dead

        self.cost_of_living()
        self._bladder = value # задаем новое значение



    def cost_of_living(self):
        # меняем приватные переменные, для того чтобы избежать повторный вызов сеттера
        self._bladder -= 1 
        self._energy -= 1
        self._hygiene -= 1
        self._social -= 1
        self._hunger -= 1

Polina = Sim("Polina", "Asd", 18, "F", "qwe")


print("увеличили")
Polina.bladder += 1
print("уменьшили но больше 3")
Polina.bladder -= 8
print("уменьшили и значение меньше 3")
Polina.bladder -= 1
Polina.bladder -= 1
print("отрицательное")
Polina.bladder -= 1
Polina.bladder -= 1
Polina.bladder -= 1