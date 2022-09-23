squared_matrix_dimensions = int(input())
command_list = input().split()

matrix = []
player_current_position = []
matrix_coal_locations = 0
for row in range(squared_matrix_dimensions):
    current_column = [i for i in input().split()]
    matrix.append(current_column)

    if 'c' in current_column:  # should be known total coals in map
        coal_current_matches = current_column.count('c')
        matrix_coal_locations += coal_current_matches

    if 's' in current_column:  # should be known starting position of the player
        current_column_position = current_column.index('s')
        player_current_position.append(row)
        player_current_position.append(current_column_position)

collected_coal = 0
collected_all_coals = False
game_over = False
player_row_position = player_current_position[0]
player_column_position = player_current_position[1]

for current_command in command_list:
    if current_command == 'left':
        if player_column_position - 1 < 0:  # invalid movement
            continue

        player_column_position -= 1  # set the new position

        if matrix[player_row_position][player_column_position] == 'c':
            collected_coal += 1
            if collected_coal == matrix_coal_locations:
                collected_all_coals = True
                break

            else:
                matrix[player_row_position][player_column_position] = '*'  # should set this field to default

        elif matrix[player_row_position][player_column_position] == 'e':
            game_over = True
            break

    elif current_command == 'right':
        if player_column_position + 1 > squared_matrix_dimensions - 1:  # invalid movement
            continue

        player_column_position += 1  # set the new position

        if matrix[player_row_position][player_column_position] == 'c':
            collected_coal += 1
            if collected_coal == matrix_coal_locations:
                collected_all_coals = True
                break

            else:
                matrix[player_row_position][player_column_position] = '*'  # should set this field to default

        elif matrix[player_row_position][player_column_position] == 'e':
            game_over = True
            break

    elif current_command == 'up':
        if player_row_position - 1 < 0:  # invalid movement
            continue

        player_row_position -= 1  # set the new position

        if matrix[player_row_position][player_column_position] == 'c':
            collected_coal += 1
            if collected_coal == matrix_coal_locations:
                collected_all_coals = True
                break

            else:
                matrix[player_row_position][player_column_position] = '*'  # should set this field to default

        elif matrix[player_row_position][player_column_position] == 'e':
            game_over = True
            break

    elif current_command == 'down':
        if player_row_position + 1 > squared_matrix_dimensions - 1:  # invalid movement
            continue

        player_row_position += 1  # set the new position

        if matrix[player_row_position][player_column_position] == 'c':
            collected_coal += 1
            if collected_coal == matrix_coal_locations:
                collected_all_coals = True
                break

            else:
                matrix[player_row_position][player_column_position] = '*'  # should set this field to default

        elif matrix[player_row_position][player_column_position] == 'e':
            game_over = True
            break

if collected_all_coals:
    print(f"You collected all coal! ({player_row_position}, {player_column_position})")

elif game_over:
    print(f"Game over! ({player_row_position}, {player_column_position})")

else:
    print(f"{matrix_coal_locations - collected_coal} pieces of coal left. ({player_row_position}, {player_column_position})")
