from unittest import TestCase, main


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0
    
    @property
    def make(self):
        return self.__make
    
    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption
    
    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity
    
    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount
    
    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


class TestCar(TestCase):

    def setUp(self):
        self.car = Car('Ferrari', 'F-120', 20, 75)

    def test_correct_initialisation(self):
        self.assertEqual("Ferrari", self.car.make)
        self.assertEqual("F-120", self.car.model)
        self.assertEqual(20, self.car.fuel_consumption)
        self.assertEqual(75, self.car.fuel_capacity)

    def test_make_props_with_no_str_should_return_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_with_a_proper_value_should_return_value(self):
        self.car.make = 'Dodge'

        self.assertEqual('Dodge', self.car.make)

    def test_model_props_with_no_str_should_return_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_with_a_proper_value_should_return_value(self):
        self.car.make = 'Viper'

        self.assertEqual('Viper', self.car.make)

    def test_fuel_consumption_with_zero_or_less_should_return_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_valid_value_should_return_it(self):
        self.car.fuel_consumption = 32

        self.assertEqual(32, self.car.fuel_consumption)

    def test_fuel_capacity_with_zero_or_less_should_return_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_valid_value_should_return_it(self):
        self.car.fuel_capacity = 123

        self.assertEqual(123, self.car.fuel_capacity)

    def test_fuel_amount_with_less_than_zero_should_return_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = - 1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_valid_value_should_return_it(self):
        self.car.fuel_amount = 7

        self.assertEqual(7, self.car.fuel_amount)

    def test_refuel_with_zero_or_less_quantity_should_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.refuel(- 1)

        self. assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_amount_which_will_overflow_the_capacity(self):
        self.car.refuel(234)

        self.assertEqual(self.car.fuel_capacity, self.car.fuel_amount)

    def test_refuel_with_valid_value_should_increase_fuel_amount(self):
        self.car.refuel(33)

        self.assertEqual(33, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel_should_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.drive(231300)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel_should_decrease_fuel_amount(self):
        self.car.fuel_amount = 100
        self.car.drive(100)

        self.assertEqual(80, self.car.fuel_amount)


if __name__ == '__main__':
    main()