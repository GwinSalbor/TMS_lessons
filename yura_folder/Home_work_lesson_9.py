class Sim:
    # Атрибуты класса с начальными значениями
    bladder = 10  # Уровень мочевого пузыря
    hunger = 10   # Уровень голода
    energy = 10   # Уровень энергии
    social = 10   # Уровень социального взаимодействия
    hygiene = 10  # Уровень гигиены
    sim_type = "human"  # Тип сима
    money = 100  # Количество денег
    _time = 0    # Время (в часах)

    def __init__(self, name, surname, age, sex, zodiac):
        # Инициализация полей экземпляра с именем, фамилией и прочими характеристиками
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac

    @property
    def time(self):
        # Геттер для получения текущего времени
        return self._time

    @time.setter
    def time(self, value):
        # Сеттер для установки времени с валидацией
        if value > 24:  # Если время больше 24 часов
            value -= 24  # Уменьшаем на 24 часа
            self.age += 1  # Увеличиваем возраст на 1 год
        self._time = value  # Устанавливаем новое значение времени

    def restore_bladder(self):
        # Восстанавливаем уровень мочевого пузыря до максимума
        self.bladder = 10
        # Уменьшаем другие показатели, исключая мочевой пузырь
        self.cost_of_living(exclude=["bladder"])

    def restore_energy(self):
        # Восстанавливаем уровень энергии до максимума
        self.energy = 10
        # Уменьшаем другие показатели, исключая энергию
        self.cost_of_living(exclude=["energy"])

    def restore_hygiene(self):
        # Восстанавливаем уровень гигиены до максимума
        self.hygiene = 10
        # Уменьшаем другие показатели, исключая гигиену
        self.cost_of_living(exclude=["hygiene"])

    def restore_hunger(self, food):
        # Восстанавливаем уровень голода, добавляя значение еды
        self.hunger += food.value
        # Уменьшаем количество денег на стоимость еды
        self.money -= food.cost
        # Уменьшаем другие показатели, исключая голод
        self.cost_of_living(exclude=["hunger"])

    def restore_social(self, other_sim):
        # Увеличиваем уровень социального взаимодействия для текущего сима
        self.social += 1
        # Увеличиваем уровень социального взаимодействия для другого сима
        other_sim.social += 1
        # Уменьшаем другие показатели для обоих симов, исключая социальный
        self.cost_of_living(exclude=["social"])
        other_sim.cost_of_living(exclude=["social"])

    def cost_of_living(self, exclude=None):
        # Уменьшаем все показатели сима, кроме указанных в исключениях
        if exclude is None:
            exclude = []  # Если исключений нет, создаем пустой список
        for attr in ['bladder', 'hunger', 'energy', 'social', 'hygiene']:
            if attr not in exclude:  # Проверяем, что атрибут не в исключениях
                current_value = getattr(self, attr)  # Получаем текущее значение атрибута
                if current_value > 0:  # Если значение больше 0
                    setattr(self, attr, max(0, current_value - 1))  # Уменьшаем значение на 1, не позволяя ему опуститься ниже 0

    def work(self, job):
        # Увеличиваем количество денег сима на зарплату от работы
        self.money += job.salary
        # Уменьшаем показатели сима в зависимости от работы
        self.cost_of_living(exclude=job.decrease_params)

class Food:
    def __init__(self, name, value, cost):
        # Инициализация полей еды
        self.name = name  # Имя еды
        self.value = value  # Значение, на которое увеличится голод
        self.cost = cost  # Стоимость еды

class Job:
    def __init__(self, name, salary, bladder_decrease, hunger_decrease, energy_decrease, social_decrease, hygiene_decrease):
        # Инициализация полей работы
        self.name = name  # Имя работы
        self.salary = salary  # Зарплата
        self.decrease_params = []  # Список параметров, которые будут понижаться
        self.bladder_decrease = bladder_decrease  # Уменьшение мочевого пузыря
        self.hunger_decrease = hunger_decrease  # Уменьшение голода
        self.energy_decrease = energy_decrease  # Уменьшение энергии
        self.social_decrease = social_decrease  # Уменьшение социального взаимодействия
        self.hygiene_decrease = hygiene_decrease  # Уменьшение гигиены

        # Добавляем параметры, которые будут понижаться в список
        if bladder_decrease: self.decrease_params.append("bladder")
        if hunger_decrease: self.decrease_params.append("hunger")
        if energy_decrease: self.decrease_params.append("energy")
        if social_decrease: self.decrease_params.append("social")
        if hygiene_decrease: self.decrease_params.append("hygiene")

class Vampire(Sim):
    # Вампир: переопределение некоторых атрибутов
    bladder = None  # Мочевой пузырь вампира не нужен
    energy = None   # Энергия вампира не нужна
    hygiene = None  # Гигиена вампира не нужна

    def restore_hunger(self, other_sim):
        # Вампир восстанавливает голод за счет другого сима
        self.hunger += other_sim.hunger // 2  # Вампир поглощает половину голода
        other_sim.hunger = max(0, other_sim.hunger - other_sim.hunger // 2)  # Уменьшаем голод у другого сима
        # Уменьшаем другие показатели, исключая голод
        self.cost_of_living(exclude=["hunger"])

    def restore_bladder(self):
        pass

    def restore_energy(self):
        # Вампир не восстанавливает энергию
        pass

    def restore_hygiene(self):
        # Вампир не восстанавливает гигиену
        pass

class PlantSim(Sim):
    bladder = None  

    def restore_hunger(self):
        # Восстанавливает голод до максимума
        self.hunger = 10

    def restore_bladder(self):
        pass

    def restore_energy(self):
        pass

    def restore_hygiene(self):
        pass