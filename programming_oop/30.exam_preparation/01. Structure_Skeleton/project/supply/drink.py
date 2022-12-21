from project.supply.supply import Supply


class Drink(Supply):
    INITIAL_ENERGY = 15

    def __init__(self, name: str, energy: int = INITIAL_ENERGY):
        super().__init__(name, energy)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
