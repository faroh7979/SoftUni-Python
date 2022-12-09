from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAX_SPEED = 140
    SPEED_INCREASING = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        if self.speed + self.SPEED_INCREASING > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed += self.SPEED_INCREASING
