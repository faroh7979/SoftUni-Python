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

        if player_position in bunnies_positions:
            bunny_catch_player = True

    elif letter == 'R':
        player_position[1] += 1  # column index
        if player_position[1] < 0:
            player_escaped = True
            player_position[1] -= 1  # should print the very last position before escaping

        if player_position in bunnies_positions:
            bunny_catch_player = True

    elif letter == 'U':
        player_position[0] -= 1  # column index
        if player_position[0] < 0:
            player_escaped = True
            player_position[0] += 1  # should print the very last position before escaping

        if player_position in bunnies_positions:
            bunny_catch_player = True

    elif letter == 'D':
        player_position[0] += 1  # column index
        if player_position[0] < 0:
            player_escaped = True
            player_position[0] -= 1  # should print the very last position before escaping

        if player_position in bunnies_positions:
            bunny_catch_player = True

    # bunny spreading
    for bunny in bunnies_positions:
        bunny_rows = bunny[0]
        bunny_columns = bunny[1]

        if bunny_rows > 0:
            new_bunny_rows = bunny_rows - 1
            bunnies_positions.append([new_bunny_rows, bunny_columns])

        if bunny_rows < rows - 2:
            new_bunny_rows = bunny_rows + 1
            bunnies_positions.append([new_bunny_rows, bunny_columns])

        if bunny_columns > 0:
            new_bunny_columns = bunny_columns - 1
            bunnies_positions.append([bunny_rows, new_bunny_columns])

        if bunny_columns < columns - 2:
            new_bunny_columns = bunny_columns + 1
            bunnies_positions.append([bunny_rows, new_bunny_columns])

    # checking for dying or escaping
    if bunny_catch_player or player_escaped:
        break

if player_escaped:
    print(f"won: {player_position[0]} {player_position[1]}")
if bunny_catch_player:
    print(f"dead: {player_position[0]} {player_position[1]}")
