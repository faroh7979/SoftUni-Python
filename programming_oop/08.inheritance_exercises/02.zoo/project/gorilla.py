from project.mammal import Mammal


class Gorilla(Mammal):
    def __init__(self, name: str):
        super(Mammal, self).__init__(name)

