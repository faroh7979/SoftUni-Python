from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float):
        pass

    @abstractmethod
    def refuel(self, fuel: float):
        pass


class Car(Vehicle):
    ADDITIONAL_FUEL_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: float):
        needed_fuel = distance * (self.fuel_consumption + Car.ADDITIONAL_FUEL_CONSUMPTION)

        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    ADDITIONAL_FUEL_CONSUMPTION = 1.6
    USEFUL_CAPACITY = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)

    def drive(self, distance: float):
        needed_fuel = distance * (self.fuel_consumption + Truck.ADDITIONAL_FUEL_CONSUMPTION)

        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel

    def refuel(self, fuel: float):
        self.fuel_quantity += Truck.USEFUL_CAPACITY * fuel


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
