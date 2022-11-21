from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self):
        pass

    @staticmethod
    @abstractmethod
    def return_sound():
        pass


class Cat(Animal):

    def return_sound():
        return "Meow"


class Dog (Animal):

    def return_sound():
        return "Woof - Woof"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.return_sound())


animals = [Cat, Dog]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
