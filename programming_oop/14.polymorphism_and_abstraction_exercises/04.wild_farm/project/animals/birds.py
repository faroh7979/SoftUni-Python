from animal import Bird
from food import Vegetable
from food import Fruit
from food import Seed
from food import Meat


class Owl(Bird):
    FOOD_INCREASING = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ == 'Meat':
            self.food_eaten += food.quantity
            self.weight += food.quantity * Owl.FOOD_INCREASING

        else:
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"


class Hen(Bird):
    FOOD_INCREASING = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):

        self.food_eaten += food.quantity
        self.weight += food.quantity * Hen.FOOD_INCREASING
