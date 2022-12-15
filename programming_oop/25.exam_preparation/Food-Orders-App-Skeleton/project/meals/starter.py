from project.meals.meal import Meal


class Starter(Meal):
    DEFAULT_QUANTITY = 60

    def __init__(self, name: str, price: float, quantity: int = DEFAULT_QUANTITY):
        super(Starter, self).__init__(name, price, quantity)

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"
