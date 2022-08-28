fires = input().split('#')
total_water = int(input())
effort = 0
put_it_out_cells = []
total_fire = 0
for current_fire in fires:
    fires_kinds = current_fire.split(' = ')
    type_of_fire = fires_kinds[0]
    value_of_cell = int(fires_kinds[1])
    if type_of_fire == 'High':
        if value_of_cell < 81 or value_of_cell > 125:
            continue
    elif type_of_fire == 'Medium':
        if value_of_cell < 51 or value_of_cell > 80:
            continue
    elif type_of_fire == 'Low':
        if value_of_cell < 1 or value_of_cell > 50:
            continue
    if total_water < value_of_cell:
        continue
    total_water -= value_of_cell
    effort += value_of_cell * 0.25
    total_fire += value_of_cell
    put_it_out_cells.append(value_of_cell)
    if total_water == 0:
        break
print('Cells:')
for current_int in put_it_out_cells:
    print(f' - {int(current_int)}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
