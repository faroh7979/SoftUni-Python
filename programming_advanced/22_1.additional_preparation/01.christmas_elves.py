from collections import deque

elves = deque([int(i) for i in input().split()])
energy = [int(i) for i in input().split()]
total_toys = 0
total_used_energy = 0

current_craft_times = 0
while elves and energy:
    current_craft_times += 1
    current_elf = elves.popleft()
    current_energy = energy.pop()

    if current_elf < 5:  # Careful if this case is counting for the crafted
        continue

    elif current_craft_times % 15 == 0:
        current_energy *= 2
        if current_energy <= current_elf:
            current_elf -= current_energy
            total_used_energy += current_energy
            current_elf += 1

        else:
            current_elf *= 2
            current_energy = int(current_energy / 2)
            energy.append(current_energy)
        elves.append(current_elf)

    elif current_craft_times % 3 == 0:
        current_energy *= 2
        if current_energy <= current_elf:
            total_toys += 2
            current_elf -= current_energy
            total_used_energy += current_energy
            current_elf += 1

        else:
            current_elf *= 2
            current_energy = int(current_energy / 2)
            energy.append(current_energy)
        elves.append(current_elf)

    elif current_craft_times % 5 == 0:
        if current_energy <= current_elf:
            current_elf -= current_energy
            total_used_energy += current_energy
        else:
            current_elf *= 2
            current_energy = int(current_energy / 2)
            energy.append(current_energy)
        elves.append(current_elf)

    else:
        if current_energy <= current_elf:
            current_elf -= current_energy
            total_used_energy += current_energy
            total_toys += 1
            current_elf += 1
        else:
            current_elf *= 2
            energy.append(current_energy)
        elves.append(current_elf)


print(f'Toys: {total_toys}')
print(f'Energy: {total_used_energy}')

if elves:
    print(f'Elves left: {", ".join(map(str, elves))}')
elif energy:
    print(f'Boxes left: {", ".join(map(str, energy))}')