matrix_size = 5
matrix = [[i for i in input().split()] for _ in range(matrix_size)]
total_commands = int(input())

player_position = tuple()
total_targets = 0
for row_index in range(matrix_size):
    for col_index in range(matrix_size):

        if matrix[row_index][col_index] == 'x':
            total_targets += 1

        elif matrix[row_index][col_index] == 'A':
            player_position = (row_index, col_index)
            matrix[row_index][col_index] = '.'

total_targets_begin = total_targets
player_row = player_position[0]
player_col = player_position[1]
hit_targets = []
all_targets_down = False
for _ in range(total_commands):
    command = input().split()

    if command[0] == 'shoot':
        direction = command[1]

        if direction == 'right':
            for current_col in range(player_col + 1, matrix_size):   # check for + 1 if a problem
                if matrix[player_row][current_col] == 'x':
                    total_targets -= 1
                    hit_targets.append([player_row, current_col])
                    matrix[player_row][current_col] = '.'
                    break

        elif direction == 'left':
            for current_col in range(player_col - 1, - 1, - 1):
                if matrix[player_row][current_col] == 'x':
                    total_targets -= 1
                    hit_targets.append([player_row, current_col])
                    matrix[player_row][current_col] = '.'
                    break

        elif direction == 'up':
            for current_row in range(player_row - 1, - 1, - 1):
                if matrix[current_row][player_col] == 'x':
                    total_targets -= 1
                    hit_targets.append([current_row, player_col])
                    matrix[current_row][player_col] = '.'
                    break

        elif direction == 'down':
            for current_row in range(player_row + 1, matrix_size):
                if matrix[current_row][player_col] == 'x':
                    total_targets -= 1
                    hit_targets.append([current_row, player_col])
                    matrix[current_row][player_col] = '.'
                    break

    elif command[0] == 'move':
        direction = command[1]
        steps = int(command[2])

        if direction == 'right':
            if player_col + steps < matrix_size:
                if matrix[player_row][player_col + steps] == '.':
                    player_row += steps

        elif direction == 'left':
            if player_col - steps >= 0:
                if matrix[player_row][player_col - steps] == '.':
                    player_col -= steps

        elif direction == 'up':
            if player_row - steps >= 0:
                if matrix[player_row - steps][player_col] == '.':
                    player_row -= steps

        elif direction == 'down':
            if player_row + steps < matrix_size:
                if matrix[player_row + steps][player_col] == '.':
                    player_row += steps

    if total_targets == 0:
        all_targets_down = True
        break

if all_targets_down:
    print(f"Training completed! All {total_targets_begin} targets hit.")
else:
    print(f"Training not completed! {total_targets} targets left.")

for element in hit_targets:
    print(element)
