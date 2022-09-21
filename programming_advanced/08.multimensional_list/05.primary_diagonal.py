matrix_rows = int(input())

total_primary_diagonals_sum = 0
matrix = []
for row in range(matrix_rows):
    column = [int(i) for i in input().split()]
    matrix.append(column)

current_diagonal_index = 0  # helpful variable for diagonal movement
for current_row in matrix:
    total_primary_diagonals_sum += current_row[current_diagonal_index]
    current_diagonal_index += 1  # on this way the move will be on diagonal

print(total_primary_diagonals_sum)
