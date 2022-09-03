def factorial_division(first: int, second: int):
    result = 1
    for current_multiplier in range(first, second, - 1):
        result *= current_multiplier
    return f'{result:.2f}'


first_input = int(input())
second_input = int(input())
print(factorial_division(first_input, second_input))
