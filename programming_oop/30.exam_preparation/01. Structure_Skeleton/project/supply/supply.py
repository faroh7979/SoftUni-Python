from abc import ABC, abstractmethod


class Supply(ABC):
    INITIAL_ENERGY = 0

    def __init__(self, name: str, energy: int = INITIAL_ENERGY):
        self.name = name
        self.energy = energy

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Name cannot be an empty string.")

        self.__name = value

    @property
    def energy(self):
        return self.__energy

    @energy.setter
    def energy(self, value):
        if value < 0:
            raise ValueError(f"Energy cannot be less than zero.")

        self.__energy = value

    @abstractmethod
    def details(self):
        pass
