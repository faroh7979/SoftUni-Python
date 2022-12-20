from project.supply.supply import Supply
from project.supply.food import Food
from project.supply.drink import Drink
from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *player: Player):

        added_players = []
        for p in player:
            if p not in self.players:
                self.players.append(p)
                added_players.append(p.name)

        if added_players:
            return f"Successfully added: {', '.join(added_players)}"

    def add_supply(self, *supply: Supply):

        for s in supply:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):

        valid_sustains = [
            'Food',
            'Drink'
        ]
        searched_player_list = [p for p in self.players if p.name == player_name]
        if searched_player_list:
            searched_player = searched_player_list[0]

            if sustenance_type in valid_sustains:
                searched_supply_list = [s for s in self.supplies if s.__class__.__name__ == sustenance_type]

                if not searched_supply_list:
                    raise Exception(f"There are no {sustenance_type} supplies left!")

                if searched_player.stamina == 100:
                    return f"{player_name} have enough stamina."

                searched_supply = searched_supply_list[-1]
                searched_player.stamina = min(100, searched_player.stamina + searched_supply.energy)

                final_index = 0
                for idx in range(len(self.supplies)):
                    if self.supplies[idx] == searched_supply:
                        final_index = idx

                self.supplies.pop(final_index)
                return f"{player_name} sustained successfully with {searched_supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player_one = next(filter(lambda p: p.name == first_player_name, self.players))
        player_two = next(filter(lambda p: p.name == second_player_name, self.players))

        if player_one.stamina == 0:
            if player_two.stamina == 0:
                return f"Player {player_one.name} does not have enough stamina.\nPlayer {player_two.name} does not have enough stamina."
            return f"Player {player_one.name} does not have enough stamina."
        if player_two.stamina == 0:
            return f"Player {player_two.name} does not have enough stamina."

        if player_one.stamina < player_two.stamina:
            player_two.stamina -= player_one.stamina / 2
            if player_two.stamina <= 0:
                player_two.stamina = 0
                return f"Winner: {player_one.name}"

            player_one.stamina -= player_two.stamina / 2
            if player_one.stamina <= 0:
                player_one.stamina = 0
                return f"Winner: {player_two.name}"

        else:
            player_one.stamina -= player_two.stamina / 2
            if player_one.stamina <= 0:
                player_one.stamina = 0
                return f"Winner: {player_two.name}"

            player_two.stamina -= player_one.stamina / 2
            if player_two.stamina <= 0:
                player_two.stamina = 0
                return f"Winner: {player_one.name}"

        if player_one.stamina > player_two.stamina:
            return f"Winner: {player_one.name}"
        else:
            return f"Winner: {player_two.name}"

    def next_day(self):

        for player in self.players:
            reduce = player.age * 2
            if player.stamina - reduce < 0:
                player.stamina = 0
            else:
                player.stamina -= reduce

            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        final_return = []

        for player in self.players:
            final_return.append(str(player))

        for supply in self.supplies:
            final_return.append(supply.details())

        return f"\n".join(final_return)


controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)
