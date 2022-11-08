from main_dishes import MainDishes


class Salmon(MainDishes):
    GRAMS = 22

    def __init__(self, name: str, price: float):
        super().__init__(name, price, grams=Salmon.GRAMS)
