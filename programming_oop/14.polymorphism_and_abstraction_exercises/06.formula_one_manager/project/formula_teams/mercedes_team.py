from formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    FIRST_SPONSORSHIP = {
        1: [1000000, 'Petronas'],
        2: [500000, 'Petronas'],
        3: [500000, 'Petronas']
    }

    SECOND_SPONSORSHIP = {
        1: [100000, 'TeamViewer'],
        2: [100000, 'TeamViewer'],
        3: [100000, 'TeamViewer'],
        4: [100000, 'TeamViewer'],
        5: [100000, 'TeamViewer'],
        6: [50000, 'TeamViewer'],
        7: [50000, 'TeamViewer']
    }

    def __init__(self, budget: int):
        super().__init__(budget)

    def expenses_per_race(self):
        return 200000

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0

        if race_pos in MercedesTeam.FIRST_SPONSORSHIP:
            revenue += MercedesTeam.FIRST_SPONSORSHIP[race_pos][0]

        if race_pos in MercedesTeam.SECOND_SPONSORSHIP:
            revenue += MercedesTeam.SECOND_SPONSORSHIP[race_pos][0]

            revenue -= self.expenses_per_race()

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
