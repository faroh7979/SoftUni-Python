from formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    FIRST_SPONSORSHIP = {
        1: [1500000, 'Oracle'],
        2: [800000, 'Oracle']
    }

    SECOND_SPONSORSHIP = {
        1: [20000, 'Honda'],
        2: [20000, 'Honda'],
        3: [20000, 'Honda'],
        4: [20000, 'Honda'],
        5: [20000, 'Honda'],
        6: [20000, 'Honda'],
        7: [20000, 'Honda'],
        8: [20000, 'Honda'],
        9: [10000, 'Honda'],
        10: [10000, 'Honda']
    }

    def __init__(self, budget: int):
        super().__init__(budget)

    def expenses_per_race(self):
        return 250000

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        if race_pos in RedBullTeam.FIRST_SPONSORSHIP:
            revenue += RedBullTeam.FIRST_SPONSORSHIP[race_pos][0]

        if race_pos in RedBullTeam.SECOND_SPONSORSHIP:
            revenue += RedBullTeam.SECOND_SPONSORSHIP[race_pos][0]

            revenue -= self.expenses_per_race()

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
