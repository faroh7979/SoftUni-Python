def calculation(a, b, action):
    result = None
    if action == 'multiply':
        result = a * b
    elif action == 'divide':
        result = int(a / second_int)
    elif action == 'add':
        result = a + second_int
    elif action == 'subtract':
        result = a - second_int
    return result


operator = input()
first_int = int(input())
second_int = int(input())
print(calculation(first_int, second_int, operator))
