santa_presents = int(input())
matrix_size = int(input())
matrix = [[i for i in input().split()] for _ in range(matrix_size)]

total_nice_kids = 0
santa_position = tuple()

for row_index in range(matrix_size):
    for col_index in range(matrix_size):

        if matrix[row_index][col_index] == 'S':
            santa_position = (row_index, col_index)
            matrix[row_index][col_index] = '-'

        elif matrix[row_index][col_index] == 'V':
            total_nice_kids += 1

nice_kids_begin = total_nice_kids
santa_row = santa_position[0]
santa_col = santa_position[1]

while True:
    direction = input()
    if direction == 'Christmas morning':
        break

    if direction == 'up':
        if santa_row - 1 >= 0:
            santa_row -= 1

    elif direction == 'down':
        if santa_row + 1 < matrix_size:
            santa_row += 1

    elif direction == 'left':
        if santa_col - 1 >= 0:
            santa_col -= 1

    elif direction == 'right':
        if santa_col + 1 < matrix_size:
            santa_col += 1

    if matrix[santa_row][santa_col] == 'V':
        santa_presents -= 1
        total_nice_kids -= 1
        matrix[santa_row][santa_col] = '-'

    elif matrix[santa_row][santa_col] == 'X':
        matrix[santa_row][santa_col] = '-'

    elif matrix[santa_row][santa_col] == 'C':

        # left side
        if matrix[santa_row][santa_col - 1] == 'X':
            santa_presents -= 1
            matrix[santa_row][santa_col - 1] = '-'
            if santa_presents == 0:
                break
        elif matrix[santa_row][santa_col - 1] == 'V':
            santa_presents -= 1
            total_nice_kids -= 1
            matrix[santa_row][santa_col - 1] = '-'
            if santa_presents == 0:
                break

        # right side
        if matrix[santa_row][santa_col + 1] == 'X':
            santa_presents -= 1
            matrix[santa_row][santa_col + 1] = '-'
            if santa_presents == 0:
                break
        elif matrix[santa_row][santa_col + 1] == 'V':
            santa_presents -= 1
            total_nice_kids -= 1
            matrix[santa_row][santa_col + 1] = '-'
            if santa_presents == 0:
                break

        # upside
        if matrix[santa_row - 1][santa_col] == 'X':
            santa_presents -= 1
            matrix[santa_row - 1][santa_col] = '-'
            if santa_presents == 0:
                break
        elif matrix[santa_row - 1][santa_col] == 'V':
            santa_presents -= 1
            total_nice_kids -= 1
            matrix[santa_row - 1][santa_col] = '-'
            if santa_presents == 0:
                break

        # downside
        if matrix[santa_row + 1][santa_col] == 'X':
            santa_presents -= 1
            matrix[santa_row + 1][santa_col] = '-'
            if santa_presents == 0:
                break
        elif matrix[santa_row + 1][santa_col] == 'V':
            santa_presents -= 1
            total_nice_kids -= 1
            matrix[santa_row + 1][santa_col] = '-'
            if santa_presents == 0:
                break

    if santa_presents == 0:
        break

if total_nice_kids > 0 and santa_presents == 0:
    print('Santa ran out of presents!')

matrix[santa_row][santa_col] = 'S'
for row in matrix:
    for column in row:
        print(column, end=' ')
    print()

if total_nice_kids == 0:
    print(f'Good job, Santa! {nice_kids_begin} happy nice kid/s.')

else:
    print(f'No presents for {total_nice_kids} nice kid/s.')
