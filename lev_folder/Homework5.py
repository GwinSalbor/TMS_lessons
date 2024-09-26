class Food:
    def __init__(self, name, value, cost):
        self.name = name  # Название еды
        self.value = value  # Энергетическая ценность
        self.cost = cost  # Стоимость еды


class Job:
    def __init__(self, name, salary, bladder_decrease, hunger_decrease, energy_decrease, social_decrease, hygiene_decrease):
        self.name = name  # Название работы
        self.salary = salary  # Зарплата
        self.bladder_decrease = bladder_decrease  # Уменьшение мочевого пузыря
        self.hunger_decrease = hunger_decrease  # Уменьшение голода
        self.energy_decrease = energy_decrease  # Уменьшение энергии
        self.social_decrease = social_decrease  # Уменьшение общения
        self.hygiene_decrease = hygiene_decrease  # Уменьшение гигиены


class Sim:
    bladder = 10
    hunger = 10
    energy = 10
    social = 50
    hygiene = 10
    sim_type = "human"
    money = 100
    _time = 20

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
        if value > 24:
            value -= 24
            self.age += 1
        self._time = value

    def restore_bladder(self):
        self.bladder = 10
        self.cost_of_living()

    def restore_energy(self):
        self.energy = 10
        self.cost_of_living()

    def restore_hygiene(self):
        self.hygiene = 10
        self.cost_of_living()

    def restore_hunger(self, food: Food):
        if self.money >= food.cost:
            self.money -= food.cost
            self.hunger += food.value
            self.cost_of_living()
        else:
            print("Недостаточно денег для покупки еды.")

    def restore_social(self, other_sim):
        self.social += 1
        other_sim.social += 1
        self.cost_of_living()
        other_sim.cost_of_living()

    def cost_of_living(self):
        if self.bladder is not None and self.bladder < 10:
            self.bladder -= 1
        if self.hunger < 10:
            self.hunger -= 1
        if self.energy is not None and self.energy < 10:
            self.energy -= 1
        if self.social < 10:
            self.social -= 1
        if self.hygiene is not None and self.hygiene < 10:
            self.hygiene -= 1

    def work(self, job: Job):
        self.money += job.salary
        self.bladder -= job.bladder_decrease
        self.hunger -= job.hunger_decrease
        self.energy -= job.energy_decrease
        self.social -= job.social_decrease
        self.hygiene -= job.hygiene_decrease
        self.cost_of_living()


class Vampire(Sim):
    bladder = None
    energy = None
    hygiene = None

    def restore_hunger(self, other_sim: Sim):
        if other_sim.hunger > 0:
            self.hunger += 5  # Вампир восстанавливает 5 голода
            other_sim.hunger -= 5  # Уменьшаем голод другого сима
            self.cost_of_living()
            other_sim.cost_of_living()

    def restore_bladder(self):
        pass  # Ничего не делаем

    def restore_energy(self):
        pass  # Ничего не делаем

    def restore_hygiene(self):
        pass  # Ничего не делаем


class PlantSim(Sim):
    bladder = None

    def restore_hunger(self):
        self.hunger += 5  # Растение-сим восстанавливает 5 голода
        self.cost_of_living()


# Пример использования классов
food = Food(name="Пицца", value=5, cost=10)
job = Job(name="Работник", salary=50, bladder_decrease=1, hunger_decrease=2, energy_decrease=3, social_decrease=1, hygiene_decrease=1)

sim1 = Sim(name="Лев", surname="Мясников", age=29, sex="мужской", zodiac="Лев")
sim2 = Vampire(name="Алукард", surname="Драколович", age=500, sex="мужской", zodiac="Скорпион")
sim3 = PlantSim(name="Растение", surname="Зеленый", age=5, sex="женский", zodiac="Дева")

# Восстановление голода
sim1.restore_hunger(food)
print(f"Голод {sim1.name}: {sim1.hunger}, Деньги: {sim1.money}")

# Восстановление общения
sim1.restore_social(sim2)
print(f"Общение {sim1.name}: {sim1.social}, Общение {sim2.name}: {sim2.social}")

# Работа
sim1.work(job)
print(f"Деньги после работы {sim1.name}: {sim1.money}")

# Восстановление голода вампира
sim2.restore_hunger(sim1)
print(f"Голод вампира {sim2.name}: {sim2.hunger}, Голод {sim1.name}: {sim1.hunger}")

# Восстановление голода растение-сим
sim3.restore_hunger()
print(f"Голод {sim3.name}: {sim3.hunger}")

