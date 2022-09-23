rows, columns = map(int, input().split())

for row in range(97, 97 + rows):  # working with ascii characters
    matrix_string = ''
    for column in range(row, row + columns):  # working with ascii characters once again
        matrix_string += f'{chr(row)}{chr(column)}{chr(row)} '

    print(matrix_string)
