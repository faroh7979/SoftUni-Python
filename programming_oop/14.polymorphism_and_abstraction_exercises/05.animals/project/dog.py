from project.animal import Animal


class Dog(Animal):
    def __init__(self, name: str, age: int, gender: str):
        super().__init__(name, age, gender)

    def return_sound(self):
        return "Woof!"
