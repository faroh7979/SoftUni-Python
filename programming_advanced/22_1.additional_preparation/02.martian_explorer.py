from collections import deque


def new_coordinates(current_position: tuple, direction_move: str):
    current_row, current_col = current_position
    move_row, move_col = 0, 0

    if direction_move == 'left':
        move_row = 0
        move_col = - 1

    elif direction_move == 'right':
        move_row = 0
        move_col = 1

    elif direction_move == 'up':
        move_row = - 1
        move_col = 0

    elif direction_move == 'down':
        move_row = 1
        move_col = 0

    new_row = current_row + move_row
    new_col = current_col + move_col

    if new_row == - 1:
        new_row = ROWS - 1

    elif new_row == ROWS:
        new_row = 0

    if new_col == - 1:
        new_col = COLS - 1

    elif new_col == COLS:
        new_col = 0

    return new_row, new_col


ROWS, COLS = 6, 6

matrix = [[i for i in input().split()]for _ in range(ROWS)]
directions_list = deque(input().split(', '))

deposit_to_be_found = ['water', 'metal', 'concrete']
rover_position = tuple()
for searched_row_index in range(ROWS):
    for searched_col_index in range(COLS):
        if matrix[searched_row_index][searched_col_index] == 'E':
            rover_position = (searched_row_index, searched_col_index)
            break

while directions_list:
    direction = directions_list.popleft()

    row, col = new_coordinates(rover_position, direction)

    rover_position = row, col
    current_position_symbol = matrix[row][col]

    

