from collections import deque

caffeine = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))
maximum_caffeine = 300

stamat_total_caffeine = 0
while caffeine and energy_drinks:
    current_caf = caffeine.pop()
    current_energy = energy_drinks.popleft()

    current_stamat_total = current_caf * current_energy

    if stamat_total_caffeine + current_stamat_total<= maximum_caffeine:
        stamat_total_caffeine += current_stamat_total

    else:
        energy_drinks.append(current_energy)
        stamat_total_caffeine -= 30
        if stamat_total_caffeine < 0:
            stamat_total_caffeine = 0

if energy_drinks:
    print(f'Drinks left: {", ".join(map(str, energy_drinks))}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_total_caffeine} mg caffeine.")
