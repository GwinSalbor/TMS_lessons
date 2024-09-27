class Sim:
    def __init__(self, name, surname, age, sex, zodiac, sim_type='Human', money=1000, _time=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.zodiac = zodiac
        self.sim_type = sim_type
        self.money = money
        self.time = _time
        self.hunger = 10
        self.bladder = 10
        self.social = 10
        self.hygiene = 10
        self.energy = 10
        self.total_worked_hours = 0
        self.current_job = None
        self.alive = True

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, new_time):
        if new_time >= 24:
            self._time = new_time - 24
            self.age += 1
            print(f"{self.name} has aged! Now {self.name}'s age is {self.age}.")
        else:
            self._time = new_time

    def show_needs(self):
        print(
            f"{self.name}'s current needs: Energy: {self.energy}, Hunger: {self.hunger}, Bladder: {self.bladder}, Social: {self.social}, Hygiene: {self.hygiene}")

    def adjust_need(self, need, amount):
        if getattr(self, need) <= 0 and self.alive:
            print(f"{self.name} has already died and cannot perform any actions.")
            return

        new_value = getattr(self, need) + amount
        if new_value > 10:
            new_value = 10
        elif new_value <= 0:
            new_value = 0
            self.trigger_death(need)
        setattr(self, need, new_value)

    def trigger_death(self, cause):
        self.alive = False
        if cause == 'hunger':
            print(f"{self.name} died from starving.")
        elif cause == 'energy':
            print(f"{self.name} passed out and died.")
        elif cause == 'social':
            print(f"{self.name} died from loneliness.")
        elif cause == 'hygiene':
            print(f"{self.name} died from dirt and bacteria.")
        elif cause == 'bladder':
            print(f"{self.name} peed and died from embarrassment.")
        print(f"{self.name} {self.surname} is dead and cannot perform any actions.")

    def decrease_all_but(self, excluded_attr):
        for need in ['hunger', 'bladder', 'energy', 'social', 'hygiene']:
            if need != excluded_attr:
                self.adjust_need(need, -1)

    def use_bathroom(self):
        if self.alive:
            self.adjust_need('bladder', 10 - self.bladder)  # Fully refill bladder
            self.decrease_all_but('bladder')
            print(f"{self.name} is using the bathroom. Bladder level: {self.bladder}")
            self.show_needs()

    def sleep(self):
        if self.alive:
            self.adjust_need('energy', 10 - self.energy)  # Fully refill energy
            self.decrease_all_but('energy')
            print(f"{self.name} is sleeping. Energy level: {self.energy}")
            self.show_needs()

    def take_shower(self):
        if self.alive:
            self.adjust_need('hygiene', 10 - self.hygiene)  # Fully refill hygiene
            self.decrease_all_but('hygiene')
            print(f"{self.name} is taking a shower. Hygiene level: {self.hygiene}")
            self.show_needs()

    def socialize(self, another_sim):
        if self.alive:
            self.adjust_need('social', 5)
            another_sim.adjust_need('social', +5)
            self.decrease_all_but('social')
            print(f"{self.name} is socializing with {another_sim.name}. Social level: {self.social}")
            print(f"{another_sim.name}'s social level at {another_sim.social}")
            self.show_needs()

    def eat(self, food):
        if self.alive:
            if self.money >= food.cost:
                self.money -= food.cost
                self.adjust_need('hunger', food.value)
                self.decrease_all_but('hunger')
                print(f"{self.name} ate {food.name}. Hunger level: {self.hunger}. Money left: ${self.money}")
                self.show_needs()
            else:
                print(f"{self.name} cannot afford {food.name}. Money left: ${self.money}")

    def work(self, job, hours):
        if self.alive:
            salary = job.salary * hours
            self.money += salary
            self.adjust_need('hunger', -1 * hours)
            self.adjust_need('hygiene', -1 * hours)
            self.adjust_need('energy', -1 * hours)
            self.adjust_need('social', -1 * hours)
            self.adjust_need('bladder', -1 * hours)
            print(f"{self.name} worked as a {job.name} for {hours} hours and earned ${salary}. Wallet: ${self.money}")
            self.show_needs()
            self.total_worked_hours += hours

            if self.total_worked_hours >= 20 and job.promotion:
                self.promote(job)

    def promote(self, job):
        print(f"{self.name} has been promoted from {self.current_job.name} to {self.current_job.promotion}!")
        self.current_job = Job(self.current_job.promotion, self.current_job.pay_raise, None, None)
        self.total_worked_hours = 0


class Food:
    def __init__(self, name, value, cost):
        self.name = name
        self.value = value
        self.cost = cost


class Job:
    def __init__(self, name, salary, promotion, pay_raise):
        self.name = name
        self.salary = salary
        self.promotion = promotion
        self.pay_raise = pay_raise


class Vampire(Sim):
    def __init__(self, name, surname, age, sex, zodiac, money=1000, _time=0):
        super().__init__(name, surname, age, sex, zodiac, sim_type='Vampire', money=money, _time=_time)
        self.bladder = None
        self.energy = None
        self.hygiene = None

    def eat(self, other_sim):
        if isinstance(other_sim, Sim):
            print(f"{self.name} just bit {other_sim.name}!")
            self.hunger += 5
            if self.hunger > 10:
                self.hunger = 10
            other_sim.hunger -= 5
            if other_sim.hunger < 0:
                other_sim.hunger = 0
            other_sim.energy -= 5
            if other_sim.energy < 0:
                other_sim.energy = 0
            other_sim.hygiene -= 5
            if other_sim.hygiene < 0:
                other_sim.hygiene = 0
            other_sim.social -= 5
            if other_sim.social < 0:
                other_sim.social = 0
            print(f"{other_sim.name} is now weak after being bitten.")


class PlantSim(Sim):
    def __init__(self, name, surname, age, sex, zodiac, money=1000, _time=0):
        super().__init__(name, surname, age, sex, zodiac, sim_type='PlantSim', money=money, _time=_time)
        self.bladder = None

    def eat(self, **kwargs):
        print(f"{self.name} is never hungry - don't forget to give them water.")
        self.hunger += 5
        if self.hunger > 10:
            self.hunger = 10
        self.decrease_all_but('hunger')


class Mermaid(Sim):
    def __init__(self, name, surname, age, sex, zodiac, money=1000, _time=0):
        # Ensure that the mermaid is always female
        if sex != 'Female':
            raise ValueError("Mermaids can only be female.")
        super().__init__(name, surname, age, sex, zodiac, sim_type='Mermaid', money=money, _time=_time)

    def eat(self, other_sim):
        if isinstance(other_sim, Sim) and other_sim.sex == 'Male':
            print(f"{self.name} is eating {other_sim.name}.")
            self.hunger = 10
            other_sim.hunger = 0
            other_sim.energy = 0
            other_sim.social = 0
            other_sim.hygiene = 0
            other_sim.bladder = 0
            print(f"{other_sim.name} has died!")
            other_sim.show_needs()
        else:
            print(f"{self.name} can only eat male Sims.")

    def sing(self):
        print(f"{self.name} is singing a beautiful MERMAID song.")
        self.social += 5
        if self.social > 10:
            self.social = 10
        print(f"{self.name}'s social need is now at {self.social}.")
        self.show_needs()


macaroni = Food("Mac&Cheese", 8, 400)
cookies = Food("Granny Raymond's Holiday Cookies", 7, 200)
salad = Food("Autumn Salad", 5, 100)

culinary_job = Job("Dishwasher", 126,"Drive Through Clerk", 230)
criminal_job = Job("Pickpocket", 140, "Bagman", 240)
science_job = Job("Test Subject", 155, "Lab Assistant", 230)
business_job = Job("Mailroom Clerk", 120, "Executive Assistant", 220)
entertainment_job = Job("Waiter/Waitress", 100, "Extra", 200)
law_enforcement_job = Job("Security Guard", 240, "Cadet", 350)
medicine_job = Job("Medical Technician", 200, "Paramedic", 300)
military_job = Job("Recruit", 250, "Elite Forces", 350)

sim = Sim('Bella', 'Goth', 34, 'Female', 'Virgo')
sim1 = Sim('Don', 'Lotario', 32, 'Male', 'Leo')
plant = PlantSim("Erika", 'Jones', 'Elder', 'Female', 'Aries', 1111, 0)
vampire = Vampire('Andrew', 'De Viccount', '987', 'Male', 'Pisces', 100000000, 0)
mermaid = Mermaid('Aisha', 'Seamorse', 23, 'Female', 'Aquarius', 0, 0)

