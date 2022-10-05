def func_executor(*args):
    result = ''
    for element in args:
        result += f'{element[0].__name__} - {element[0](*element[1])}' + '\n'

    return result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
