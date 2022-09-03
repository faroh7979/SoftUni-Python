def min_num(client: list):
    minimum = min(client)
    return f'The minimum number is {minimum}'


def max_num(client: list):
    maximum = max(client)
    return f'The maximum number is {maximum}'


def sum_num(client: list):
    total = sum(client)
    return f'The sum number is: {total}'


client_nums = list(map(int, input().split()))
print(min_num(client_nums))
print(max_num(client_nums))
print(sum_num(client_nums))
