#Задание 1
class Sim:
    # Переменные класса
    bladder = 10
    hunger = 10
    energy = 10
    social = 10
    hygiene = 10
    type = "human"
    money = 100
    _time = 0

    def __init__(self):
        pass

    def show_stats(self):
        print(f"Bladder: {self.bladder}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Social: {self.social}")
        print(f"Hygiene: {self.hygiene}")
        print(f"Type: {self.type}")
        print(f"Money: {self.money}")
        print(f"Time: {self._time}")

sim = Sim()
sim.show_stats()

#Задание 2
class Sim:
    def __init__(self, name, surname, age, sex, zodiac):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac
        self.bladder = 10
        self.hunger = 10
        self.energy = 10
        self.social = 10
        self.hygiene = 10
        self.type = "human"
        self.money = 100
        self._time = 0

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Zodiac: {self.zodiac}")
        print(f"Bladder: {self.bladder}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Social: {self.social}")
        print(f"Hygiene: {self.hygiene}")
        print(f"Type: {self.type}")
        print(f"Money: {self.money}")
        print(f"Time: {self._time}")

sim = Sim(name="Polina", surname="Miller", age=23, sex="Female", zodiac="Aries")
sim.show_stats()

#Задание 3
class Food:
    def __init__(self, cost, value):
        self.cost = cost  # Стоимость еды
        self.value = value  # Энергетическая ценность еды


class Sim:
    MAX_BODILY_NEEDS = 10
    
    def __init__(self, name, surname, age, sex, zodiac):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac
        self.bladder = 10
        self.hunger = 10
        self.energy = 10
        self.social = 10
        self.hygiene = 10
        self.type = "human"
        self.money = 100
        self._time = 0

    def restore_bladder(self):
        self.bladder = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s bladder is fully restored!")

    def restore_energy(self):
        self.energy = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s energy is fully restored!")

    def restore_hygiene(self):
        self.hygiene = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s hygiene is fully restored!")

    def restore_hunger(self, food):
        if self.money >= food.cost:
            self.hunger = min(self.MAX_BODILY_NEEDS, self.hunger + food.value)
            self.money -= food.cost
            print(f"{self.name} ate food and restored hunger to {self.hunger}!")
        else:
            print(f"{self.name} does not have enough money to buy the food.")

    def restore_social(self, other_sim):
        self.social = min(self.MAX_BODILY_NEEDS, self.social + 1)
        other_sim.social = min(self.MAX_BODILY_NEEDS, other_sim.social + 1)
        print(f"{self.name} and {other_sim.name} interacted! Their social levels are now {self.social} and {other_sim.social}.")

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Zodiac: {self.zodiac}")
        print(f"Bladder: {self.bladder}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Social: {self.social}")
        print(f"Hygiene: {self.hygiene}")
        print(f"Type: {self.type}")
        print(f"Money: {self.money}")
        print(f"Time: {self._time}")

sim1 = Sim(name="Lika", surname="Jonson", age=22, sex="Female", zodiac="Taurus")
sim2 = Sim(name="Polina", surname="Miller", age=23, sex="Female", zodiac="Aries")

sim1.restore_bladder()
sim1.restore_energy()
sim1.restore_hygiene()

food_item = Food(cost=20, value=5)

sim1.restore_hunger(food_item)

sim1.restore_social(sim2)

sim1.show_stats()
sim2.show_stats()


#Задание 4
class Food:
    def __init__(self, cost, value):
        self.cost = cost  # Стоимость еды
        self.value = value  # Энергетическая ценность


class Sim:
    MAX_BODILY_NEEDS = 10
    DECREASE_AMOUNT = 1  # Сколько понижать показатели

    def __init__(self, name, surname, age, sex, zodiac):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac
        self.bladder = 10
        self.hunger = 10
        self.energy = 10
        self.social = 10
        self.hygiene = 10
        self.type = "human"
        self.money = 100
        self._time = 0

    def cost_of_living(self):
        if self.bladder > 0:
            self.bladder = max(0, self.bladder - self.DECREASE_AMOUNT)
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - self.DECREASE_AMOUNT)
        if self.energy > 0:
            self.energy = max(0, self.energy - self.DECREASE_AMOUNT)
        if self.social > 0:
            self.social = max(0, self.social - self.DECREASE_AMOUNT)
        if self.hygiene > 0:
            self.hygiene = max(0, self.hygiene - self.DECREASE_AMOUNT)

    def restore_bladder(self):
        self.cost_of_living()
        self.bladder = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s bladder is fully restored!")

    def restore_energy(self):
        self.cost_of_living()
        self.energy = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s energy is fully restored!")

    def restore_hygiene(self):
        self.cost_of_living()
        self.hygiene = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s hygiene is fully restored!")

    def restore_hunger(self, food):
        self.cost_of_living()
        if self.money >= food.cost:
            self.hunger = min(self.MAX_BODILY_NEEDS, self.hunger + food.value)
            self.money -= food.cost
            print(f"{self.name} ate food and restored hunger to {self.hunger}!")
        else:
            print(f"{self.name} does not have enough money to buy the food.")

    def restore_social(self, other_sim):
        self.cost_of_living()
        self.social = min(self.MAX_BODILY_NEEDS, self.social + 1)
        other_sim.social = min(self.MAX_BODILY_NEEDS, other_sim.social + 1)
        print(f"{self.name} and {other_sim.name} interacted! Their social levels are now {self.social} and {other_sim.social}.")

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Zodiac: {self.zodiac}")
        print(f"Bladder: {self.bladder}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Social: {self.social}")
        print(f"Hygiene: {self.hygiene}")
        print(f"Type: {self.type}")
        print(f"Money: {self.money}")
        print(f"Time: {self._time}")

sim1 = Sim(name="Lika", surname="Jonson", age=22, sex="Female", zodiac="Taurus")
sim2 = Sim(name="Polina", surname="Miller", age=23, sex="Female", zodiac="Aries")

sim1.restore_bladder()
sim1.restore_energy()
sim1.restore_hygiene()

food_item = Food(cost=20, value=5)

sim1.restore_hunger(food_item)

sim1.restore_social(sim2)

sim1.show_stats()
sim2.show_stats()

#Задание 5
class Food:
    def __init__(self, cost, value):
        self.cost = cost  # Стоимость еды
        self.value = value  # Энергетическая ценность


class Job:
    def __init__(self, salary, decrease_amount):
        self.salary = salary  # Сколько денег приносит работа
        self.decrease_amount = decrease_amount  # На сколько понижает показатели потребностей


class Sim:
    MAX_BODILY_NEEDS = 10
    DECREASE_AMOUNT = 1  # Сколько понижать показатели

    def __init__(self, name, surname, age, sex, zodiac):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac
        self.bladder = 10
        self.hunger = 10
        self.energy = 10
        self.social = 10
        self.hygiene = 10
        self.type = "human"
        self.money = 100
        self._time = 0

    def cost_of_living(self):
        if self.bladder > 0:
            self.bladder = max(0, self.bladder - self.DECREASE_AMOUNT)
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - self.DECREASE_AMOUNT)
        if self.energy > 0:
            self.energy = max(0, self.energy - self.DECREASE_AMOUNT)
        if self.social > 0:
            self.social = max(0, self.social - self.DECREASE_AMOUNT)
        if self.hygiene > 0:
            self.hygiene = max(0, self.hygiene - self.DECREASE_AMOUNT)

    def restore_bladder(self):
        self.cost_of_living()
        self.bladder = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s bladder is fully restored!")

    def restore_energy(self):
        self.cost_of_living()
        self.energy = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s energy is fully restored!")

    def restore_hygiene(self):
        self.cost_of_living()
        self.hygiene = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s hygiene is fully restored!")

    def restore_hunger(self, food):
        self.cost_of_living()
        if self.money >= food.cost:
            self.hunger = min(self.MAX_BODILY_NEEDS, self.hunger + food.value)
            self.money -= food.cost
            print(f"{self.name} ate food and restored hunger to {self.hunger}!")
        else:
            print(f"{self.name} does not have enough money to buy the food.")

    def restore_social(self, other_sim):
        self.cost_of_living()
        self.social = min(self.MAX_BODILY_NEEDS, self.social + 1)
        other_sim.social = min(self.MAX_BODILY_NEEDS, other_sim.social + 1)
        print(f"{self.name} and {other_sim.name} interacted! Their social levels are now {self.social} and {other_sim.social}.")

    def work(self, job):
        self.cost_of_living()
        self.money += job.salary
        self.bladder = max(0, self.bladder - job.decrease_amount)
        self.hunger = max(0, self.hunger - job.decrease_amount)
        self.energy = max(0, self.energy - job.decrease_amount)
        self.social = max(0, self.social - job.decrease_amount)
        self.hygiene = max(0, self.hygiene - job.decrease_amount)
        print(f"{self.name} worked and earned {job.salary} money!")

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Zodiac: {self.zodiac}")
        print(f"Bladder: {self.bladder}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Social: {self.social}")
        print(f"Hygiene: {self.hygiene}")
        print(f"Type: {self.type}")
        print(f"Money: {self.money}")
        print(f"Time: {self._time}")

sim1 = Sim(name="Lika", surname="Jonson", age=22, sex="Female", zodiac="Taurus")
sim2 = Sim(name="Polina", surname="Miller", age=23, sex="Female", zodiac="Aries")

job = Job(salary=50, decrease_amount=2)

sim1.work(job)

sim1.restore_bladder()
sim1.restore_energy()
sim1.restore_hygiene()

food_item = Food(cost=20, value=5)

sim1.restore_hunger(food_item)

sim1.restore_social(sim2)

sim1.show_stats()
sim2.show_stats()

#Задание 6
class Food:
    def __init__(self, cost, value):
        self.cost = cost  # Стоимость еды
        self.value = value  # Энергетическая ценность


class Job:
    def __init__(self, salary, decrease_amount):
        self.salary = salary  # Сколько денег приносит работа
        self.decrease_amount = decrease_amount  # На сколько понижает показатели потребностей


class Sim:
    MAX_BODILY_NEEDS = 10
    DECREASE_AMOUNT = 1  # Сколько понижать показатели
    MAX_TIME = 24  # Максимальное значение времени

    def __init__(self, name, surname, age, sex, zodiac):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac
        self.bladder = 10
        self.hunger = 10
        self.energy = 10
        self.social = 10
        self.hygiene = 10
        self._money = 100
        self._time = 0

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value > self.MAX_TIME:
            self.age += value // self.MAX_TIME  # Увеличиваем возраст
            self._time = value % self.MAX_TIME  # Устанавливаем остаток от деления
        else:
            self._time = value

    def cost_of_living(self):
        if self.bladder > 0:
            self.bladder = max(0, self.bladder - self.DECREASE_AMOUNT)
        if self.hunger > 0:
            self.hunger = max(0, self.hunger - self.DECREASE_AMOUNT)
        if self.energy > 0:
            self.energy = max(0, self.energy - self.DECREASE_AMOUNT)
        if self.social > 0:
            self.social = max(0, self.social - self.DECREASE_AMOUNT)
        if self.hygiene > 0:
            self.hygiene = max(0, self.hygiene - self.DECREASE_AMOUNT)

    def restore_bladder(self):
        self.cost_of_living()
        self.bladder = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s bladder is fully restored!")

    def restore_energy(self):
        self.cost_of_living()
        self.energy = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s energy is fully restored!")

    def restore_hygiene(self):
        self.cost_of_living()
        self.hygiene = self.MAX_BODILY_NEEDS
        print(f"{self.name}'s hygiene is fully restored!")

    def restore_hunger(self, food):
        self.cost_of_living()
        if self._money >= food.cost:
            self.hunger = min(self.MAX_BODILY_NEEDS, self.hunger + food.value)
            self._money -= food.cost
            print(f"{self.name} ate food and restored hunger to {self.hunger}!")
        else:
            print(f"{self.name} does not have enough money to buy the food.")

    def restore_social(self, other_sim):
        self.cost_of_living()
        self.social = min(self.MAX_BODILY_NEEDS, self.social + 1)
        other_sim.social = min(self.MAX_BODILY_NEEDS, other_sim.social + 1)
        print(f"{self.name} and {other_sim.name} interacted! Their social levels are now {self.social} and {other_sim.social}.")

    def work(self, job):
        self.cost_of_living()
        self._money += job.salary
        self.bladder = max(0, self.bladder - job.decrease_amount)
        self.hunger = max(0, self.hunger - job.decrease_amount)
        self.energy = max(0, self.energy - job.decrease_amount)
        self.social = max(0, self.social - job.decrease_amount)
        self.hygiene = max(0, self.hygiene - job.decrease_amount)
        print(f"{self.name} worked and earned {job.salary} money!")

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")
        print(f"Age: {self.age}")
        print(f"Sex: {self.sex}")
        print(f"Zodiac: {self.zodiac}")
        print(f"Bladder: {self.bladder}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Social: {self.social}")
        print(f"Hygiene: {self.hygiene}")
        print(f"Type: {self.type}")
        print(f"Money: {self._money}")
        print(f"Time: {self.time}")

sim1 = Sim(name="Polina", surname="Miller", age=23, sex="Female", zodiac="Aries")

# Установка времени
sim1.time = 30  # Увеличит возраст на 1 и установит время на 6
sim1.show_stats()

job = Job(salary=50, decrease_amount=2)

sim1.work(job)

sim1.restore_bladder()
sim1.restore_energy()
sim1.restore_hygiene()

food_item = Food(cost=20, value=5)

sim1.restore_hunger(food_item)

sim1.show_stats()

#Задание 7
class Food:
    def __init__(self, name, value, cost):
        self.name = name    # Название еды
        self.value = value  # Энергетическая ценность еды
        self.cost = cost    # Стоимость еды

    def __str__(self):
        return f"{self.name}: Value = {self.value}, Cost = {self.cost}"

food_item = Food(name="Apple", value=5, cost=10)
print(food_item)  # Вывод: Apple: Value = 5, Cost = 10

#Задание 8
class Job:
    def __init__(self, name, salary, bladder_decreases, hunger_decreases, energy_decreases, social_decreases, hygiene_decreases):
        self.name = name  # Название работы
        self.salary = salary  # Зарплата
        self.bladder_decreases = bladder_decreases  
        self.hunger_decreases = hunger_decreases  
        self.energy_decreases = energy_decreases  
        self.social_decreases = social_decreases  
        self.hygiene_decreases = hygiene_decreases  

    def __str__(self):
        return (f"Job Name: {self.name}, Salary: {self.salary}, "
                f"Bladder Decreases: {self.bladder_decreases}, "
                f"Hunger Decreases: {self.hunger_decreases}, "
                f"Energy Decreases: {self.energy_decreases}, "
                f"Social Decreases: {self.social_decreases}, "
                f"Hygiene Decreases: {self.hygiene_decreases}")


job_item = Job(name="Engineer", salary=5000, bladder_decreases=1, hunger_decreases=2, energy_decreases=3, social_decreases=1, hygiene_decreases=2)
print(job_item)  

#Задание 9
class Sim:
    MAX_BODILY_NEEDS = 10
    DECREASE_AMOUNT = 1  # Сколько понижать показатели
    MAX_TIME = 24  # Максимальное значение времени

    def __init__(self, name, surname, age, sex, zodiac):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac
        self.bladder = 10
        self.hunger = 10
        self.energy = 10
        self.social = 10
        self.hygiene = 10
        self._money = 100
        self._time = 0


class Vampire(Sim):
    def __init__(self, name, surname, age, sex, zodiac):
        super().__init__(name, surname, age, sex, zodiac)
        self.bladder = None
        self.energy = None
        self.hygiene = None

    def restore_hunger(self, other_sim):
        if other_sim.hunger > 0:
            self.hunger = min(self.MAX_BODILY_NEEDS, self.hunger + other_sim.hunger)
            other_sim.hunger = max(0, other_sim.hunger - 5)  # Понижаем голод другого сима
            print(f"{self.name} fed on {other_sim.name}. Hunger is now {self.hunger}!")

    def restore_bladder(self):
        pass  

    def restore_energy(self):
        pass  

    def restore_hygiene(self):
        pass  


class PlantSim(Sim):
    def __init__(self, name, surname, age, sex, zodiac):
        super().__init__(name, surname, age, sex, zodiac)
        self.bladder = None

    def restore_hunger(self):
        self.hunger = self.MAX_BODILY_NEEDS
        print(f"{self.name} absorbed sunlight and restored hunger to {self.hunger}!")

    def restore_bladder(self):
        pass  

    def restore_energy(self):
        self.energy = self.MAX_BODILY_NEEDS
        print(f"{self.name} is energized!")

    def restore_hygiene(self):
        self.hygiene = self.MAX_BODILY_NEEDS
        print(f"{self.name} is clean now!")

vampire = Vampire(name="Dracula", surname="Count", age=200, sex="Male", zodiac="Scorpio")
