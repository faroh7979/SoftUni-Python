class ValueCannotBeNegative(Exception):
    """Value con not be negative"""


num_list = [int(input()), int(input()), int(input()), int(input()), int(input())]
for num in num_list:
    if num < 0:
        raise ValueCannotBeNegative

