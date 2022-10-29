from player import Player


class Guild:
    all_players = []

    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player_ass: Player):

        if player_ass in self.players:
            return f"Player {player_ass.name} is already in the guild."

        elif player_ass in Guild.all_players:
            return f"Player {player_ass.name} is in another guild."

        else:
            Guild.all_players.append(player_ass)
            self.players.append(player_ass)
            player_ass.guild = self.name
            return f"Welcome player {player_ass.name} to the guild {self.name}"

    def kick_player(self, player_name: str):

        for checked_player in self.players:
            if checked_player.name == player_name:
                self.players.remove(checked_player)
                checked_player.guild = "Unaffiliated"
                break

        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        list_info_return = [f'Guild: {self.name}']

        for player_final in self.players:
            list_info_return.append(player_final.player_info())

        return '\n'.join(list_info_return)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
