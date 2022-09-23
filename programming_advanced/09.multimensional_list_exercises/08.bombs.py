squared_matrix_dimensions = int(input())

matrix = []
for row in range(squared_matrix_dimensions):
    matrix.append([int(i) for i in input().split()])

bombs_coordinated = input().split()
for element in bombs_coordinated:
    current_row, current_column = map(int, element.split(','))
    element_damage = matrix[current_row][current_column]
    matrix[current_row][current_column] = 0  # should be set to 0 after detonation

    # checking for possible victims on the top row
    if current_row == 0:

        # checking for possible victims on the top left column
        if current_column == 0:
            if matrix[current_row][current_column + 1] > 0:
                matrix[current_row][current_column + 1] -= element_damage

            if matrix[current_row + 1][current_column] > 0:
                matrix[current_row + 1][current_column] -= element_damage

            if matrix[current_row + 1][current_column + 1] > 0:
                matrix[current_row + 1][current_column + 1] -= element_damage

        # checking for possible victims on the top right column
        elif current_column == squared_matrix_dimensions - 1:
            if matrix[current_row][current_column - 1] > 0:
                matrix[current_row][current_column - 1] -= element_damage

            if matrix[current_row + 1][current_column] > 0:
                matrix[current_row + 1][current_column] -= element_damage

            if matrix[current_row + 1][current_column - 1] > 0:
                matrix[current_row + 1][current_column - 1] -= element_damage

        # checking for possible victims on the top middle cells
        else:
            if matrix[current_row][current_column + 1] > 0:
                matrix[current_row][current_column + 1] -= element_damage

            if matrix[current_row + 1][current_column] > 0:
                matrix[current_row + 1][current_column] -= element_damage

            if matrix[current_row + 1][current_column + 1] > 0:
                matrix[current_row + 1][current_column + 1] -= element_damage

            if matrix[current_row][current_column - 1] > 0:
                matrix[current_row][current_column - 1] -= element_damage

            if matrix[current_row + 1][current_column - 1] > 0:
                matrix[current_row + 1][current_column - 1] -= element_damage

    # checking for possible victims on the bottom row
    elif current_row == squared_matrix_dimensions - 1:
        # checking for possible victims on the bottom left column
        if current_column == 0:
            if matrix[current_row][current_column + 1] > 0:
                matrix[current_row][current_column + 1] -= element_damage

            if matrix[current_row - 1][current_column] > 0:
                matrix[current_row - 1][current_column] -= element_damage

            if matrix[current_row - 1][current_column + 1] > 0:
                matrix[current_row - 1][current_column + 1] -= element_damage

        # checking for possible victims on the bottom right column
        elif current_column == squared_matrix_dimensions - 1:
            if matrix[current_row][current_column - 1] > 0:
                matrix[current_row][current_column - 1] -= element_damage

            if matrix[current_row - 1][current_column] > 0:
                matrix[current_row - 1][current_column] -= element_damage

            if matrix[current_row - 1][current_column - 1] > 0:
                matrix[current_row - 1][current_column - 1] -= element_damage

        # checking for possible victims on the bottom middle cells
        else:
            if matrix[current_row][current_column + 1] > 0:
                matrix[current_row][current_column + 1] -= element_damage

            if matrix[current_row - 1][current_column] > 0:
                matrix[current_row - 1][current_column] -= element_damage

            if matrix[current_row - 1][current_column + 1] > 0:
                matrix[current_row - 1][current_column + 1] -= element_damage

            if matrix[current_row][current_column - 1] > 0:
                matrix[current_row][current_column - 1] -= element_damage

            if matrix[current_row - 1][current_column - 1] > 0:
                matrix[current_row - 1][current_column - 1] -= element_damage

    # checking middle rows
    else:
        if current_column == 0:
            # checking left columns
            if matrix[current_row][current_column + 1] > 0:
                matrix[current_row][current_column + 1] -= element_damage

            if matrix[current_row - 1][current_column] > 0:
                matrix[current_row - 1][current_column] -= element_damage

            if matrix[current_row - 1][current_column + 1] > 0:
                matrix[current_row - 1][current_column + 1] -= element_damage

            if matrix[current_row + 1][current_column] > 0:
                matrix[current_row + 1][current_column] -= element_damage

            if matrix[current_row + 1][current_column + 1] > 0:
                matrix[current_row + 1][current_column + 1] -= element_damage

        elif current_column == squared_matrix_dimensions - 1:
            # checking right columns
            if matrix[current_row - 1][current_column] > 0:
                matrix[current_row - 1][current_column] -= element_damage

            if matrix[current_row][current_column - 1] > 0:
                matrix[current_row][current_column - 1] -= element_damage

            if matrix[current_row - 1][current_column - 1] > 0:
                matrix[current_row - 1][current_column - 1] -= element_damage

            if matrix[current_row + 1][current_column] > 0:
                matrix[current_row + 1][current_column] -= element_damage

            if matrix[current_row - 1][current_column - 1] > 0:
                matrix[current_row - 1][current_column - 1] -= element_damage

        else:
            # checking middle columns in middle rows
            if matrix[current_row][current_column + 1] > 0:
                matrix[current_row][current_column + 1] -= element_damage

            if matrix[current_row - 1][current_column] > 0:
                matrix[current_row - 1][current_column] -= element_damage

            if matrix[current_row - 1][current_column + 1] > 0:
                matrix[current_row - 1][current_column + 1] -= element_damage

            if matrix[current_row][current_column - 1] > 0:
                matrix[current_row][current_column - 1] -= element_damage

            if matrix[current_row - 1][current_column - 1] > 0:
                matrix[current_row - 1][current_column - 1] -= element_damage

            if matrix[current_row + 1][current_column] > 0:
                matrix[current_row + 1][current_column] -= element_damage

            if matrix[current_row + 1][current_column + 1] > 0:
                matrix[current_row + 1][current_column + 1] -= element_damage

            if matrix[current_row + 1][current_column - 1] > 0:
                matrix[current_row + 1][current_column - 1] -= element_damage

active_cells = []
final_string = ''
for end_row in matrix:
    for end_column in end_row:
        final_string += f'{end_column} '
        if end_column > 0:
            active_cells.append(end_column)
    final_string += f'\n'

print(f'Alive cells: {len(active_cells)}')
print(f'Sum: {sum(active_cells)}')
print(final_string)
