class Sim:
    bladder = 10
    hunger = 10
    energy = 10
    social = 10
    hygiene = 10
    type = "human"
    money = 100
    _time = 0

    def __init__(self, name, surname, age, sex, zodiac):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value >= 24:
            self._time = value - 24
            self.age += 1
        else:
            self._time = value

    def cost_of_living(self, exception=None):
        """Уменьшает все потребности кроме той, которая указана в исключении"""
        needs = ['bladder', 'hunger', 'energy', 'social', 'hygiene']
        for need in needs:
            if need != exception:
                setattr(self, need, max(0, getattr(self, need) - 1))

    def restore_bladder(self):
        self.bladder = 10
        self.cost_of_living(exception='bladder')

    def restore_energy(self):
        self.energy = 10
        self.cost_of_living(exception='energy')

    def restore_hygiene(self):
        self.hygiene = 10
        self.cost_of_living(exception='hygiene')

    def restore_hunger(self, food):
        if self.money >= food.cost:
            self.hunger = min(10, self.hunger + food.value)
            self.money -= food.cost
            self.cost_of_living(exception='hunger')
        else:
            print(f"Недостаточно денег для покупки еды {food.name}")

    def restore_social(self, other_sim):
        self.social = min(10, self.social + 2)
        other_sim.social = min(10, other_sim.social + 2)
        self.cost_of_living(exception='social')

    def work(self, job):
        self.money += job.salary
        self.bladder -= job.bladder_decreases
        self.hunger -= job.hunger_decreases
        self.energy -= job.energy_decreases
        self.social -= job.social_decreases
        self.hygiene -= job.hygiene_decreases

        # Убедимся, что показатели не опускаются ниже 0
        self.bladder = max(0, self.bladder)
        self.hunger = max(0, self.hunger)
        self.energy = max(0, self.energy)
        self.social = max(0, self.social)
        self.hygiene = max(0, self.hygiene)


class Food:
    def __init__(self, name, value, cost):
        self.name = name
        self.value = value  # На сколько увеличится голод
        self.cost = cost  # Сколько стоит


class Job:
    def __init__(self, name, salary, bladder_decreases, hunger_decreases, energy_decreases, social_decreases, hygiene_decreases):
        self.name = name
        self.salary = salary
        self.bladder_decreases = bladder_decreases
        self.hunger_decreases = hunger_decreases
        self.energy_decreases = energy_decreases
        self.social_decreases = social_decreases
        self.hygiene_decreases = hygiene_decreases

class Vampire(Sim):
    bladder = None
    energy = None
    hygiene = None

    def restore_hunger(self, other_sim):
        self.hunger = min(10, self.hunger + 3)
        other_sim.hunger = max(0, other_sim.hunger - 3)
        other_sim.energy = max(0, other_sim.energy - 2)
        other_sim.hygiene = max(0, other_sim.hygiene - 2)
        self.cost_of_living(exception='hunger')

    def restore_bladder(self):
        pass

    def restore_energy(self):
        pass

    def restore_hygiene(self):
        pass


class PlantSim(Sim):
    bladder = None

    def restore_hunger(self):
        self.hunger = 10
        self.cost_of_living(exception='hunger')