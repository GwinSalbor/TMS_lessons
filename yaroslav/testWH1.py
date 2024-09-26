class Food:
    def __init__(self, name: str, value: int, cost: float):
        self.name = name
        self.value = value
        self.cost = cost


def sim_status(fun):
    def inner(self, value):
        if getattr(self, "_" + fun.__name__) < value and value>7:
            print(fun.__name__ + " fully restored")
            self.status = SimStatus.Perfect
        elif getattr(self, "_" + fun.__name__) < value and 3< value < 7:
            print(fun.__name__ + " restored")
            self.status = SimStatus.NotGood
        elif getattr(self, "_" + fun.__name__) > value and  0< value < 3:
            print(f"{fun.__name__} indicator is too low, please restore id")
            self.status = SimStatus.AlmostDead
        elif getattr(self, "_" + fun.__name__) > value and  value <=1:
            print(f"{fun.__name__} indicator is too low")
            print("im dying")
            self.status = SimStatus.Dead
        print(value)
        if value < 0:
            value = 0
        if value > 10:
            value = 10

        return fun(self, value)
    return inner


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
    @sim_status
    def bladder(self, value):
        self.cost_of_living()
        self._bladder = value

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    @sim_status
    def hunger(self, value):
        self.cost_of_living()
        self._hunger = value
    
    @property
    def social(self):
        return self._social

    @social.setter
    @sim_status
    def social(self, value):
        self.cost_of_living()
        self._social = value

    @property
    def hygiene(self):
        return self._hygiene

    @hygiene.setter
    @sim_status
    def hygiene(self, value):
        self.cost_of_living()
        self._hygiene = value
    
    @property
    def energy(self):
        return self._energy

    @energy.setter
    @sim_status
    def energy(self, value):
        self.cost_of_living()
        self._energy = value
    
        
    def cost_of_living(self):
        # меняем приватные переменные, для того чтобы избежать повторный вызов сеттера
        self._bladder -= 1 
        self._energy -= 1
        self._hygiene -= 1
        self._social -= 1
        self._hunger -= 1

Polina = Sim("Polina", "Asd", 18, "F", "qwe")


Polina.bladder += 1
Polina.bladder -= 5
Polina.bladder += 1
Polina.bladder += 1
Polina.bladder += 100
Polina.bladder -= 3
Polina.bladder -= 3
Polina.bladder -= 3
Polina.bladder -= 3

Polina.hunger += 1
Polina.hunger -= 3
Polina.hunger -= 3
Polina.hunger -= 3

# Polina.social += 1
# Polina.social -= 3
# Polina.social -= 3
# Polina.social -= 3

# Polina.hygiene += 1
# Polina.hygiene -= 3
# Polina.hygiene -= 3
# Polina.hygiene -= 3

# Polina.energy += 1
# Polina.energy -= 3
# Polina.energy -= 3
# Polina.energy -= 3
