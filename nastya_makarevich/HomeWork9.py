class Sim:
    type = "human"
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
        self.money = 100
        self._time = 0

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value >= 24:
            self.age += value // 24
            self._time = value % 24
        else:
            self._time = value


    def __str__(self):
        return f"""{self.name} Status: bladder: {self.bladder}, hunger: {self.hunger}, energy: {self.energy}, social: {self.social}, hygiene: {self.hygiene}, money: {self.money},  time: {self._time}, age: {self.age}"""

    def use_toilet(self):
        self.cost_of_living()
        self.bladder = 10
        self.time += 0.5
        print(f"You've used a toilet and restored your bladder level.")
        print(self.__str__())

    def sleep(self):
        self.cost_of_living()
        self.energy = 10
        self.time += 8
        print(f"You've had some sleep and restored your energy level.")
        print(self.__str__())

    def take_shower(self):
        self.cost_of_living()
        self.hygiene = 10
        self.time += 0.5
        print(f"You've taken a shower and restored your hygiene level.")
        print(self.__str__())


    def eat(self, food):
        if self.money - food.cost >= 0:
            self.cost_of_living()
            self.money -= food.cost
            if self.hunger + food.value <= 10:
                self.hunger += food.value + 1
            else:
                self.hunger = 10
            print(f"You've just eaten {food.name} and restored your hunger level to {self.hunger}")
            self.time += 0.5
            print(self.__str__())
        else:
            print(f"You do not have enough money to buy {food.name}. You may earn some money at work.")
            print(self.__str__())

    def interact(self, another_sim):
        self.cost_of_living()
        another_sim.cost_of_living()
        self.social = 10
        another_sim.social = 10
        self.time += 0.5
        another_sim._time += 0.5
        print(f"You've just made friends with {another_sim.name}. Your social level is restored. {another_sim.name} social level is: {another_sim.social}.")
        print(self.__str__())
        print(another_sim.__str__())

    def cost_of_living(self):
        self.bladder -= 1
        self.bladder = max(self.bladder, 0)
        self.energy -= 1
        self.energy = max(self.energy, 0)
        self.hygiene -= 1
        self.hygiene = max(self.hygiene, 0)
        self.social -= 1
        self.social = max(self.social, 0)
        self.hunger -= 1
        self.hunger = max(self.hunger, 0)

    def work(self, job):
        self.money += job.salary
        self.bladder -= job.bladder_decrease
        self.bladder = max(self.bladder, 0)
        self.energy -= job.energy_decrease
        self.energy = max(self.energy, 0)
        self.hygiene -= job.hygiene_decrease
        self.hygiene = max(self.hygiene, 0)
        self.hunger -= job.hunger_decrease
        self.hunger = max(self.hunger, 0)
        self.time += 8
        print(f"Hooray! You've done a great job and earned {job.salary}$. Now you have {self.money}$ on your bank account.")
        print(self.__str__())

class Vampire(Sim):
    type = "vampire"
    def __init__(self, name, surname, age, sex, zodiac):
        super().__init__(name, surname, age, sex, zodiac)
        self.bladder = None
        self.energy = None
        self.hygiene = None
    def use_toilet(self):
        print("Vampires do not use toilets!")
        print(self.__str__())

    def sleep(self):
        print("Vampires do not sleep!")
        print(self.__str__())

    def take_shower(self):
        print("Vampires do not need a shower!")
        print(self.__str__())

    def cost_of_living(self):
        self.social -= 1
        self.social = max(self.social, 0)
        self.hunger -= 1
        self.hunger = max(self.hunger, 0)

    def eat(self, food):
        print("Vampires do not eat Sim food!")
        print(self.__str__())

    def drink_blood(self, another_sim):
        self.cost_of_living()
        self.hunger = 10
        another_sim.energy -= 3
        another_sim.energy = max(another_sim.energy, 0)
        self.time += 0.5
        print(f"You've just drunk blood from {another_sim.name}. Your hunger level is restored. {another_sim.name} energy level is decreased to {another_sim.energy}.")
        print(self.__str__())
        print(another_sim.__str__())

    def work(self, job):
        self.money += job.salary
        self.hunger -= job.hunger_decrease
        self.hunger = max(self.hunger, 0)
        self.time += 8
        print(f"Hooray! You've done a great job and earned {job.salary}$. Now you have {self.money}$ on your bank account.")
        print(self.__str__())

class PlantSim(Sim):
    type = "plantsim"
    def __init__(self, name, surname, age, sex, zodiac):
        super().__init__(name, surname, age, sex, zodiac)
        self.bladder = None

    def use_toilet(self):
        print("PlantSims do not use toilets!")
        print(self.__str__())

    def cost_of_living(self):
        self.energy -= 1
        self.energy = max(self.energy, 0)
        self.hygiene -= 1
        self.hygiene = max(self.hygiene, 0)
        self.social -= 1
        self.social = max(self.social, 0)
        self.hunger -= 1
        self.hunger = max(self.hunger, 0)

    def eat(self, food=None):
        try:
            if food is None:
                self.cost_of_living()
                self.hunger = 10
                self.time += 2
                print(f"Your hunger level is restored.")
                print(self.__str__())
            else:
                print(self.__str__())
                raise ValueError("PlantSim does not need any food!")
        except ValueError as ve:
            print(f"ValueError: {ve}")

    def work(self, job):
        self.money += job.salary
        self.energy -= job.energy_decrease
        self.energy = max(self.energy, 0)
        self.hygiene -= job.hygiene_decrease
        self.hygiene = max(self.hygiene, 0)
        self.hunger -= job.hunger_decrease
        self.hunger = max(self.hunger, 0)
        self.time += 8
        print(f"Hooray! You've done a great job and earned {job.salary}$. Now you have {self.money}$ on your bank account.")
        print(self.__str__())

class Food:
    def __init__(self, name, cost, value):
        self.name = name
        self.cost = cost
        self.value = value

class Job:
    def __init__(self, name, salary, bladder_decrease, energy_decrease, hygiene_decrease, hunger_decrease):
        self.name = name
        self.salary = salary
        self.bladder_decrease = bladder_decrease
        self.energy_decrease = energy_decrease
        self.hygiene_decrease = hygiene_decrease
        self.hunger_decrease = hunger_decrease

# Add some food (some instances of Food class are created)
banana = Food("banana", 2, 2)
burger = Food("burger", 3, 7)
fries = Food("fries", 2, 3)
milkshake = Food("milkshake", 200, 1)
# Add some jobs (some instances of Job class are created)
teacher = Job("Teacher", 10, 2,8,2,5)
qa = Job("QA", 50, 2,5,1,8)
singer = Job("Singer", 5000, 1,2,5,1)
# Add Sim (Sim class instance)
rachel = Sim("Rachel", "Green", 24, "F", "Cancer")
# Add Vampire (Vampire class instance)
edward = Vampire("Edward", "Cullen", 123, "M", "Leo")
# Add PlantSim (PlantSim class instance)
groot = PlantSim("Groot", "Tree", 16, "M", "Libra")
# # Scenario 1: Test Sim class
print("1.1 Check Sim initial state:")
print(rachel)
print("1.2 Send Sim to work as a Teacher:")
rachel.work(teacher)
print("1.3 Send Sim to sleep:")
rachel.sleep()
print("1.4 Feed Sim with banana:")
rachel.eat(banana)
print("1.4 Feed Sim above max level:")
rachel.eat(burger)
print("1.5 Send Sim to use the restroom:")
rachel.use_toilet()
print("1.6 Send Sim to the shower:")
rachel.take_shower()
print("1.7 Make Sim interact with another Sim")
rachel.interact(edward)
print("1.8 Make Sim parameters below zero. Check age increased when time > 24:")
rachel.work(teacher)
print("1.9 Make Sim buy food they cannot afford:")
rachel.eat(milkshake)
# # Scenario 2: Test Vampire class
print("2.1 Check Vampire initial state:")
print(edward)
print("2.2 Send Vampire to sleep:")
edward.sleep()
print("2.3 Send Vampire to use the restroom:")
edward.use_toilet()
print("2.4 Send Vampire to the shower:")
edward.take_shower()
print("2.5 Feed Vampire Sim food:")
edward.eat(banana)
print("2.6 Make Vampire drink blood:")
edward.drink_blood(rachel)
print("2.7 Send Vampire to work:")
edward.work(singer)
# Scenario 3: Test PlantSim class
print("3.1 Check PlantSim initial state:")
print(groot)
print("3.2 Send PlantSim to use the restroom:")
groot.use_toilet()
print("3.3 Send PlantSim to work:")
groot.work(qa)
print("3.4 Check Sim food cannot be fed to PlantSim:")
groot.eat(banana)
print("3.5 Restore PlantSim hunger level:")
groot.eat()