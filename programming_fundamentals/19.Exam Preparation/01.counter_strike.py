initial_energy = int(input())
command = input()
count_of_wins = 0
not_enough_energy = False

while command != 'End of battle':
    distance = int(command)
    if initial_energy >= distance:
        count_of_wins += 1
        initial_energy -= distance
        if count_of_wins % 3 == 0:
            initial_energy += count_of_wins
    else:
        not_enough_energy = True
        break
    command = input()
if not_enough_energy:
    print(f'Not enough energy! Game ends with {count_of_wins} won battles and {initial_energy} energy')
else:
    print(f'Won battles: {count_of_wins}. Energy left: {initial_energy}')
