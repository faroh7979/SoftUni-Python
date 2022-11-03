from product import Product


class Food(Product):
    QUANTITY = 15

    def __init__(self, name: str):
        super(Food, self).__init__(name, quantity=Food.QUANTITY)

