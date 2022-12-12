from project.client import Client
from project.meals.meal import Meal
from project.meals.dessert import Dessert
from project.meals.starter import Starter
from project.meals.main_dish import MainDish


class FoodOrdersApp:

    VALID_MEALS = [
        "Starter",
        "MainDish",
        "Dessert"
    ]

    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt_id = 0

    def register_client(self, client_phone_number: str):
        client = [c for c in self.clients_list if c.phone_number == client_phone_number]

        if client:
            raise Exception(f"The client has already been registered!")

        self.clients_list.append(Client(client_phone_number))
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):

        for meal in meals:
            if meal.__class__.__name__ in self.VALID_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        final_menu = []
        for meal in self.menu:
            final_menu.append(meal.details())

        return f"\n".join(final_menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):  # in doubt at all
        if len(self.menu) < 5:
            raise Exception(f"The menu is not ready!")

        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        current_menu = self.menu.copy()
        current_bill = 0
        current_cart = []
        for meal, quantity in meal_names_and_quantities.items():
            if len(self.menu) < 5:
                raise Exception(f"The menu is not ready!")

            try:
                searched_meal = next(filter(lambda m: m.name == meal, self.menu))
            except StopIteration:
                raise Exception(f"{meal} is not on the menu!")

            if searched_meal.quantity < quantity:
                raise Exception(f"Not enough quantity of {searched_meal.__class__.__name__}: {searched_meal.name}!")

            current_cart.append(searched_meal)
            current_bill += searched_meal.price * quantity
            searched_meal.quantity -= quantity
            if searched_meal.quantity == 0:
                self.menu.remove(searched_meal)

        client.shopping_cart.extend(current_cart)
        client.bill += current_bill
        self.menu = current_menu
        meal_names = [m.name for m in client.shopping_cart]
        return f"Client {client_phone_number} successfully ordered {', '.join(meal_names)} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):  # in doubt about returning to the menu
        searched_client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))

        if not searched_client.shopping_cart:
            raise Exception(f"There are no ordered meals!")

        searched_client.bill = 0

        for meal in searched_client.shoping_cart:
            if meal not in self.menu:
                self.menu[meal] = 0
            self.menu[meal] += meal.quantity
        searched_client.shopping_cart = []
        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        searched_client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if not searched_client.shopping_cart:
            raise Exception(f"There are no ordered meals!")

        self.receipt_id += 1
        client_bill = searched_client.bill
        searched_client.bill = 0
        searched_client.shopping_cart = []

        return f"Receipt #{self.receipt_id} with total amount of {client_bill:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."


food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app)
