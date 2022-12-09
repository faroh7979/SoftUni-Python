from project.jockey import Jockey
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.horse_race import HorseRace


class HorseRaceApp:
    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):

        try:
            next(filter(lambda h: h.name == horse_name, self.horses))
            raise Exception(f'Horse {horse_name} has been already added!')

        except StopIteration:

            if horse_type == "Appaloosa":
                self.horses.append(Appaloosa(horse_name, horse_speed))
                return f"{horse_type} horse {horse_name} is added."

            elif horse_type == "Thoroughbred":
                self.horses.append(Thoroughbred(horse_name, horse_speed))
                return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):

        try:
            next(filter(lambda j: j.name == jockey_name, self.jockeys))

        except StopIteration:
            self.jockeys.append(Jockey(jockey_name, age))
            return f"Jockey {jockey_name} is added."

        raise Exception(f"Jockey {jockey_name} has been already added!")

    def create_horse_race(self, race_type: str):

        try:
            next(filter(lambda rt: rt.race_type == race_type, self.horse_races))

        except StopIteration:
            self.horse_races.append(HorseRace(race_type))
            return f"Race {race_type} is created."

        raise Exception(f"Race {race_type} has been already created!")

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):

        try:
            jockey = next(filter(lambda j: j.name == jockey_name, self.jockeys))
        except StopIteration:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        try:
            horse = list((filter(lambda h: h.__class__.__name__ == horse_type and not h.is_taken, self.horses)))[- 1]
        except IndexError:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):

        try:
            horse_race = next(filter(lambda hr: hr.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        searched_jockey_list = [j for j in self.jockeys if j.name == jockey_name]

        if not searched_jockey_list:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        searched_jockey = searched_jockey_list[0]

        if searched_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if searched_jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(searched_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):

        try:
            horse_race = next(filter(lambda hr: hr.race_type == race_type, self.horse_races))

        except StopIteration:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        jockeys_in_race = [j for j in horse_race.jockeys]
        current_max_speed = 0
        winner_jockey = None

        for j in jockeys_in_race:
            if j.horse.speed > current_max_speed:
                current_max_speed = j.horse.speed
                winner_jockey = j

        return f"The winner of the {race_type} race, with a speed of {winner_jockey.horse.speed}km/h is {winner_jockey.name}! Winner's horse: {winner_jockey.horse.name}."


horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))
