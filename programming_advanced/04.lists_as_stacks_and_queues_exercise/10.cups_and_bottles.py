from collections import deque

cups_capacity = deque(map(int, input().split()))
filled_bottles = list(map(int, input().split()))

wasted_water = 0
filled_cups = 0

while cups_capacity and filled_bottles:
    current_cup_capacity = cups_capacity.popleft()

    for bottle_index in range(len(filled_bottles)):
        current_bottle = filled_bottles.pop()

        if current_bottle >= current_cup_capacity:
            filled_cups += 1
            wasted_water += (current_bottle - current_cup_capacity)
            break

        else:
            current_cup_capacity -= current_bottle

if cups_capacity:
    remaining_cups = list(map(str, cups_capacity))
    print(f'Cups: {" ".join(remaining_cups)}')

else:
    remaining_bottles = list(map(str, filled_bottles))
    print(f'Bottles: {" ".join(remaining_bottles)}')

print(f'Wasted litters of water: {wasted_water}')
