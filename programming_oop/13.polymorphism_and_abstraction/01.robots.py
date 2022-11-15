class Robot:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def robot_sensors_amount():
        return 1


class MedicalRobot(Robot):
    @staticmethod
    def robot_sensors_amount():
        return 6


class ChefRobot(Robot):
    @staticmethod
    def robot_sensors_amount():
        return 4


class WarRobot(Robot):
    @staticmethod
    def robot_sensors_amount():
        return 12


def print_number_of_robot_sensors(robot):
    print(robot.robot_sensors_amount())


basic_robot = Robot('Robo')
da_vinci = MedicalRobot('Da Vinci')
moley = ChefRobot('Moley')
griffin = WarRobot('Griffin')

print(basic_robot.robot_sensors_amount())
print(da_vinci.robot_sensors_amount())
print(moley.robot_sensors_amount())
print(griffin.robot_sensors_amount())
