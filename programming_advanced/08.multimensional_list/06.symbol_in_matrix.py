square_matrix_rows_and_columns = int(input())

matrix = []
for row in range(square_matrix_rows_and_columns):
    column = [i for i in input()]
    matrix.append(column)

special_symbol = input()
founded_special_symbol = False  # use it for flag on the main loop
coordinates = ()  # will use it if we found the special symbol there
for current_row in range(square_matrix_rows_and_columns):
    if founded_special_symbol:
        break

    for current_column in range(square_matrix_rows_and_columns):  # do it on this way because the matrix is square
        if matrix[current_row][current_column] == special_symbol:
            coordinates = (current_row, current_column)
            founded_special_symbol = True
            break

if founded_special_symbol:
    print(coordinates)
else:
    print(f'{special_symbol} does not occur in the matrix')
