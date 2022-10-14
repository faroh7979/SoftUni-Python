def divide(first_num, second_num):
    if second_num == 0:
        return 'You cannot divide by 0'

    return f'{(first_num/second_num):.2f}'


def multiply(first_num, second_num):
    return f'{(first_num*second_num):.2f}'


def subtract(first_num, second_num):
    return f'{(first_num-second_num):.2f}'


def adding(first_num, second_num):
    return f'{(first_num+second_num):.2f}'


def raising(first_num, second_num):
    return f'{(first_num**second_num):.2f}'


def calculations(user_input):
    details = user_input.split()
    num_one = float(details[0])
    sign = details[1]
    second_num = int(details[2])

    if sign == '/':
        print(divide(num_one, second_num))

    elif sign == '*':
        print(multiply(num_one, second_num))

    elif sign == '-':
        print(subtract(num_one, second_num))

    elif sign == '+':
        print(adding(num_one, second_num))

    elif sign == '^':
        print(raising(num_one, second_num))



