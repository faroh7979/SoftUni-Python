from collections import deque

bee_values = deque(map(int, input().split()))
nectar_values = deque(map(int, input().split()))
mathematical_symbols = deque(input().split())

total_honey_made = 0

while bee_values and nectar_values:
    current_bee = bee_values.popleft()
    current_nectar = nectar_values.pop()

    if current_nectar >= current_bee:  # if match
        current_symbol = mathematical_symbols.popleft()

        if current_symbol == '+':
            total_honey_made += abs((current_bee + current_nectar))

        elif current_symbol == '-':
            total_honey_made += abs((current_bee - current_nectar))

        elif current_symbol == '*':
            total_honey_made += abs((current_bee * current_nectar))

        elif current_symbol == '/':
            total_honey_made = total_honey_made + abs((current_bee / current_nectar))

    else:
        bee_values.appendleft(current_bee)  # should try again for another match

print(f"Total honey made: {total_honey_made}")

if bee_values:
    print(f'Bees left: {", ".join(map(str, bee_values))}')

if nectar_values:
    print(f'Nectar left: {", ".join(map(str, nectar_values))}')
