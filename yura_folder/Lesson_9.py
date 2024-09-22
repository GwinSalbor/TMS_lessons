class Human():
    name = "name"

    def __init__(self, name, age, id, surname) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.surname = surname

yura = Human("Yura", 18, 123, "korneev")

print(yura.__dict__)