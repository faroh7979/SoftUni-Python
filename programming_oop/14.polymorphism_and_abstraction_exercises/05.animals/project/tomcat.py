from project.cat import Cat


class Tomcat(Cat):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender='Male')

    def return_sound(self):
        return "Hiss"
