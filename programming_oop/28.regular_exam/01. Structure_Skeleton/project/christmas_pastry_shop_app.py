from project.delicacies.delicacy import Delicacy
from project.delicacies.stolen import Stolen
from project.delicacies.gingerbread import Gingerbread
from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth


class ChristmasPastryShopApp:
    VALID_DELICACY = [
        'Gingerbread',
        'Stolen'
    ]

    VALID_BOOTHS = [
        'Open Booth',
        'Private Booth'
    ]

    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):

        searched_delicacy_name = [d for d in self.delicacies if d.name == name]
        if searched_delicacy_name:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACY:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if type_delicacy == self.VALID_DELICACY[0]:
            self.delicacies.append(Gingerbread(name, price))
        else:
            self.delicacies.append(Stolen(name, price))

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):

        searched_booth_num = [b for b in self.booths if b.booth_number == booth_number]
        if searched_booth_num:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        if type_booth == self.VALID_BOOTHS[0]:
            self.booths.append(OpenBooth(booth_number, capacity))
        else:
            self.booths.append(PrivateBooth(booth_number, capacity))

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):

        searched_booth_l = [b for b in self.booths if not b.is_reserved and b.capacity >= number_of_people]

        if not searched_booth_l:
            raise Exception(f"No available booth for {number_of_people} people!")

        searched_booth = searched_booth_l[0]

        searched_booth.reserve(number_of_people)

        return f"Booth {searched_booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):

        searched_booth_l = [b for b in self.booths if b.booth_number == booth_number]

        if not searched_booth_l:
            raise Exception(f"Could not find booth {booth_number}!")

        searched_booth = searched_booth_l[0]

        searched_delicacy_l = [d for d in self.delicacies if d.name == delicacy_name]
        if not searched_delicacy_l:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        searched_delicacy = searched_delicacy_l[0]
        searched_booth.delicacy_orders.append(searched_delicacy)

        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):

        searched_booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        income = searched_booth.price_for_reservation + sum(d.price for d in searched_booth.delicacy_orders)
        self.income += income

        searched_booth.price_for_reservation = 0
        searched_booth.is_reserved = False
        searched_booth.delicacy_orders = []

        return f"Booth {booth_number}:\nBill: {income:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())
