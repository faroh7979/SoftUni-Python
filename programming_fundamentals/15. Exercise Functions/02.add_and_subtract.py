def sum_numbers(list_of_ints: list):
    sum_of_ints = sum(list_of_int)
    return sum_of_ints


def subtract(third_num: int):
    result = sum_numbers(list_of_int) - third_num
    return result


first_int = int(input())
second_int = int(input())
third_int = int(input())
list_of_int = [first_int, second_int]

print(subtract(third_int))
