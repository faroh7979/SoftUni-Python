from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.ferrari = Vehicle(20.0, 754.54)

    def test_correct_initialisation(self):
        self.assertEqual(self.ferrari.DEFAULT_FUEL_CONSUMPTION, 1.25)
        self.assertEqual(self.ferrari.fuel, 20)
        self.assertEqual(self.ferrari.capacity, 20)
        self.assertEqual(self.ferrari.horse_power, 754.54)
        self.assertEqual(self.ferrari.fuel_consumption, 1.25)

    def test_drive_if_not_enough_fuel_should_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.ferrari.drive(50)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_if_enough_fuel_should_decrease_fuel(self):
        self.ferrari.drive(4)
        self.assertEqual(15, self.ferrari.fuel)

    def test_refuel_when_too_much_fuel_should_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.ferrari.refuel(50)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_when_the_fuel_is_not_too_much_should_increase_fuel_quantity(self):
        self.ferrari.fuel = 0
        self.ferrari.refuel(15)

        self.assertEqual(15, self.ferrari.fuel)

    def test_string_representation_correct_message(self):
        expected_result = "The vehicle has 754.54 horse power with 20.0 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_result, str(self.ferrari))


if __name__ == '__main__':
    main()
