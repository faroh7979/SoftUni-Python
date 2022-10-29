class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if ingredient not in self.ingredients:
            self.ingredients[ingredient] = 0

        self.ingredients[ingredient] += quantity
        self.price += (quantity * price_per_quantity)

    def remove_ingredient(self, remove_ingredient: str, remove_quantity: int, remove_price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

        if remove_ingredient not in self.ingredients:
            return f"Wrong ingredient selected! We do not use {remove_ingredient} in {self.name}!"

        if remove_quantity > self.ingredients[remove_ingredient]:
            return f"Please check again the desired quantity of {remove_ingredient}!"

        self.ingredients[remove_ingredient] -= remove_quantity
        self.price -= (remove_quantity * remove_price_per_quantity)

    def make_order(self):
        self.ordered = True

        ingredient_list = []
        for key, value in self.ingredients.items():
            ingredient_list.append(f'{key}: {value}')

        return f"You've ordered pizza {self.name} prepared with {', '.join(ingredient_list)} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
