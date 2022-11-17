from red_bull_team import RedBullTeam
from mercedes_team import MercedesTeam


class F1SeasonApp:
    F1_TEAMS = {
        "Red Bull": RedBullTeam,
        "Mercedes": MercedesTeam
    }

    def __init__(self):
        self.red_bull_team = None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):

        if team_name not in F1SeasonApp.F1_TEAMS:
            raise ValueError("Invalid team name!")

        if team_name == 'Red Bull':
            self.red_bull_team = RedBullTeam(budget)

        else:
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_position: int, mercedes_position: int):

        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        list_for_return = [f'Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_position)}.',
                           f'Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_position)}.',
                           f'{"Red Bull" if red_bull_position < mercedes_position else "Mercedes"} is ahead at the {race_name} race.'
                           ]

        return " ".join(list_for_return)


f1_season = F1SeasonApp()

print(f1_season.register_team_for_season("Red Bull", 2000000))
print(f1_season.register_team_for_season("Mercedes", 2500000))
print(f1_season.new_race_results("Nurburgring", 1, 7))
print(f1_season.new_race_results("Silverstone", 10, 1))
