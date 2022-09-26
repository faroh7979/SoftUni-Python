rows, columns = map(int, input().split())

matrix = []
player_position = []
bunnies_positions = []
for row in range(rows):
    column = [i for i in input()]
    matrix.append(column)
    if 'P' in column:  # checking for player position
        player_position.append(row)
        player_position.append(column.index('P'))

    if 'B' in column:  # checking for bunnies
        for cur_index in range(columns):  # will be the same as in current column
            if column[cur_index] == 'B':
                bunnies_positions.append([row, cur_index])

# should remove player from final matrix
player_starting_row, player_starting_column = player_position[0], player_position[1]
matrix[player_starting_row][player_starting_column] = '.'

bunny_temp_list = []
player_escaped = False
bunny_catch_player = False
directions = input()
for letter in directions:

    # Player movement
    if letter == 'L':
        player_position[1] -= 1  # column index
        if player_position[1] < 0:
            player_escaped = True
            player_position[1] += 1  # should print the very last position before escaping

        if not player_escaped:
            for bunny_current in bunnies_positions:
                if player_position == bunny_current:
                    bunny_catch_player = True

    elif letter == 'R':
        player_position[1] += 1  # column index
        if player_position[1] == columns:
            player_escaped = True
            player_position[1] -= 1  # should print the very last position before escaping

        if not player_escaped:
            for bunny_current in bunnies_positions:
                if player_position == bunny_current:
                    bunny_catch_player = True

    elif letter == 'U':
        player_position[0] -= 1  # column index
        if player_position[0] < 0:
            player_escaped = True
            player_position[0] += 1  # should print the very last position before escaping

        if not player_escaped:
            for bunny_current in bunnies_positions:
                if player_position == bunny_current:
                    bunny_catch_player = True

    elif letter == 'D':
        player_position[0] += 1  # column index
        if player_position[0] == columns:
            player_escaped = True
            player_position[0] -= 1  # should print the very last position before escaping

        if not player_escaped:
            for bunny_current in bunnies_positions:
                if player_position == bunny_current:
                    bunny_catch_player = True

    # bunny spreading
    for bunny in bunnies_positions:
        bunny_rows = bunny[0]
        bunny_columns = bunny[1]

        if bunny_rows > 0:
            new_bunny_rows = bunny_rows - 1
            bunny_temp_list.append([new_bunny_rows, bunny_columns])

        if bunny_rows < rows - 1:
            new_bunny_rows = bunny_rows + 1
            bunny_temp_list.append([new_bunny_rows, bunny_columns])

        if bunny_columns > 0:
            new_bunny_columns = bunny_columns - 1
            bunny_temp_list.append([bunny_rows, new_bunny_columns])

        if bunny_columns < columns - 1:
            new_bunny_columns = bunny_columns + 1
            bunny_temp_list.append([bunny_rows, new_bunny_columns])

    bunnies_positions.extend(bunny_temp_list)
    bunny_temp_list = []  # using for concatenating at the end

    if not player_escaped:
        for bunny_current in bunnies_positions:
            if player_position == bunny_current:
                bunny_catch_player = True
                break

    # checking for dying or escaping
    if bunny_catch_player or player_escaped:
        break

for element in bunnies_positions:
    bunny_row = element[0]
    bunny_column = element[1]

    matrix[bunny_row][bunny_column] = 'B'

for final_row in matrix:
    for final_column in final_row:
        print(final_column, end='')
    print()

if player_escaped:
    print(f"won: {player_position[0]} {player_position[1]}")

elif bunny_catch_player:
    print(f"dead: {player_position[0]} {player_position[1]}")
