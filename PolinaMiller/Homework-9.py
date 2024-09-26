class Food:
    def __init__(self, name, value, cost):
        self.name = name
        self.value = value
        self.cost = cost


class Job:
    def __init__(self, name, salary, bladder_decreases, hunger_decreases, social_decreases, fun_decreases, hygiene_decreases):
        self.name = name
        self.salary = salary
        self.bladder_decreases = bladder_decreases
        self.hunger_decreases = hunger_decreases
        self.social_decreases = social_decreases
        self.fun_decreases = fun_decreases
        self.hygiene_decreases = hygiene_decreases


class Sim:
    bladder = 10
    hunger = 10
    social = 10
    hygiene = 10
    energy = 10
    type = "human"
    money = 100

    def __init__(self, name, surname, age, sex, zodiac):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac
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

    def replenish_bladder(self):
        self.bladder = 10
        self.cost_of_living()

    def replenish_energy(self):
        self.energy = 10
        self.cost_of_living()

    def replenish_hygiene(self):
        self.hygiene = 10
        self.cost_of_living()

    def restore_hunger(self, food: Food):
        if self.money >= food.cost:
            self.hunger += food.value
            self.hunger = min(self.hunger, 10)
            self.money -= food.cost
            self.cost_of_living()
        else:
            print("Недостаточно денег для покупки еды.")

    def socialize(self, other_sim):
        self.social += 1
        other_sim.social += 1
        self.cost_of_living()
        other_sim.cost_of_living()

    def cost_of_living(self):
        if self.hunger < 10:
            self.bladder -= 1
            self.energy -= 1
            self.hygiene -= 1
            self.social -= 1
        self.bladder = max(self.bladder, 0)
        self.energy = max(self.energy, 0)
        self.hygiene = max(self.hygiene, 0)
        self.social = max(self.social, 0)

    def work(self, job: Job):
        self.bladder -= job.bladder_decreases
        self.hunger -= job.hunger_decreases
        self.social -= job.social_decreases
        self.hygiene -= job.hygiene_decreases
        self.energy -= job.fun_decreases
        self.bladder = max(self.bladder, 0)
        self.hunger = max(self.hunger, 0)
        self.social = max(self.social, 0)
        self.hygiene = max(self.hygiene, 0)
        self.energy = max(self.energy, 0)
        self.money += job.salary


class Vampire(Sim):
    bladder = None
    energy = None
    hygiene = None

    def replenish_hunger(self, other_sim: Sim):
        if other_sim.hunger > 0:
            hunger_to_transfer = min(2, other_sim.hunger)  # Максимум 2 голода можно забрать
            other_sim.hunger -= hunger_to_transfer
            self.hunger += hunger_to_transfer
            self.hunger = min(self.hunger, 10)
            self.cost_of_living()
            other_sim.cost_of_living()
        else:
            print(f"{other_sim.name} is too hungry to feed from!")

    def replenish_bladder(self):
        pass  

    def replenish_energy(self):
        pass  

    def replenish_hygiene(self):
        pass  


class PlantSim(Sim):
    bladder = None

    def replenish_hunger(self):
        self.hunger = 10  # Полное восстановление голода
        self.cost_of_living()

    def replenish_bladder(self):
        pass  

    def replenish_energy(self):
        self.energy = 10  # Полное восстановление энергии
        self.cost_of_living()

    def replenish_hygiene(self):
        self.hygiene
