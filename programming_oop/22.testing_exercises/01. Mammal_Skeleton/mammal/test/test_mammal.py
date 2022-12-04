from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal('Nori', 'Dog', 'Bough')

    def test_correct_initialisation(self):
        self.assertEqual('Nori', self.mammal.name)
        self.assertEqual('Dog', self.mammal.type)
        self.assertEqual('Bough', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Nori makes Bough", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual("Nori is of type Dog", self.mammal.info())


if __name__ == "__,main__":
    main()
