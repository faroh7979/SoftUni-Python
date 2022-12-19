from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):

    def setUp(self):
        self.my_d = ToyStore()

    def test_correct_initialisation(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.my_d.toy_shelf)

    def test_shelf_not_in_toy(self):

        with self.assertRaises(Exception) as ex:
            self.my_d.add_toy('R', "D")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_if_toy_is_on_this_shelf(self):
        self.my_d.toy_shelf['A'] = 'D'

        with self.assertRaises(Exception) as ex:
            self.my_d.add_toy('A', 'D')

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_shelf_is_not_none(self):
        self.my_d.toy_shelf['A'] = 'D'

        with self.assertRaises(Exception) as ex:
            self.my_d.add_toy('A', 'S')

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_correct_add_toy(self):
        self.my_d.toy_shelf = {
            "A": 'None',
            "B": 'None',
            "C": None,
            "D": 'None',
            "E": 'None',
            "F": 'None',
            "G": 'None',
        }
        expected = self.my_d.add_toy('C', 'Liverpool')

        self.assertEqual("Toy:Liverpool placed successfully!", expected)
        self.assertEqual({
            "A": 'None',
            "B": 'None',
            "C": 'Liverpool',
            "D": 'None',
            "E": 'None',
            "F": 'None',
            "G": 'None',
        }, self.my_d.toy_shelf)

    def test_remove_toy_no_this_shelf(self):
        self.my_d.toy_shelf = {
            "A": 'None',
            "B": 'None',
            "C": None,
            "D": 'None',
            "E": 'None',
            "F": 'None',
            "G": 'None',
        }

        with self.assertRaises(Exception) as ex:
            self.my_d.remove_toy('Q', 'Liverpool')

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_toy_name_does_not_match(self):
        self.my_d.toy_shelf = {
            "A": 'None',
            "B": 'None',
            "C": 'Liverpool',
            "D": 'None',
            "E": 'None',
            "F": 'None',
            "G": 'None', }

        with self.assertRaises(Exception) as ex:
            self.my_d.remove_toy('C', "Arsenal")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_successful_removing(self):
        self.my_d.toy_shelf = {
            "A": 'None',
            "B": 'Arsenal',
            "C": 'Liverpool',
            "D": 'None',
            "E": 'None',
            "F": 'None',
            "G": 'None',
        }

        expected = self.my_d.remove_toy('B', 'Arsenal')

        self.assertEqual(expected, "Remove toy:Arsenal successfully!")
        self.assertEqual({
            "A": 'None',
            "B": None,
            "C": 'Liverpool',
            "D": 'None',
            "E": 'None',
            "F": 'None',
            "G": 'None',
        }, self.my_d.toy_shelf)


if __name__ == '__main__':
    main()