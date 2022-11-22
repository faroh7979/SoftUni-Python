from abc import abstractmethod, ABC


class Duck(ABC):

    @abstractmethod
    def quack(self):
        pass


class Walkable(ABC):

    @abstractmethod
    def walk():
        pass


class Flyable(ABC):

    @abstractmethod
    def fly(self):
        pass


class RubberDuck(Duck):

    def quack():
        return "Squeek"


class RobotDuck(Duck, Flyable, Walkable):
    HEIGHT = 50

    def __init__(self):
        self.height = 50

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


duck = RobotDuck()
print(duck.fly())
print(duck.land())
print(duck.walk())
print(duck.quack())

