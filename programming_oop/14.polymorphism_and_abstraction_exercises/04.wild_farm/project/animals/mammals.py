from animal import Mammal
from food import Food
from food import Fruit
from food import Seed
from food import Meat


class Mouse(Mammal):
    FOOD_INCREASING = 0.10

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ == 'Fruit' or food.__class__.__name__ == 'Vegetable':
            self.food_eaten += food.quantity
            self.weight += food.quantity * Mouse.FOOD_INCREASING

        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Dog(Mammal):
    FOOD_INCREASING = 0.40

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ == 'Meat':
            self.food_eaten += food.quantity
            self.weight += food.quantity * Dog.FOOD_INCREASING

        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Cat(Mammal):
    FOOD_INCREASING = 0.30

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ == 'Meat' or food.__class__.__name__ == 'Vegetable':
            self.food_eaten += food.quantity
            self.weight += food.quantity * Cat.FOOD_INCREASING

        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Tiger(Mammal):
    FOOD_INCREASING = 1.00

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ == 'Meat':
            self.food_eaten += food.quantity
            self.weight += food.quantity * Tiger.FOOD_INCREASING

        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
