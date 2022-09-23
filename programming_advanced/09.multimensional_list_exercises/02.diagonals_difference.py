squared_matrix_dimensions = int(input())

matrix = []
for row in range(squared_matrix_dimensions):
    column = [int(i) for i in input().split()]
    matrix.append(column)

primary_diagonal_sum = 0
for current_index in range(squared_matrix_dimensions):
    primary_diagonal_sum += matrix[current_index][current_index]

secondary_diagonal_sum = 0
secondary_diagonal_column = squared_matrix_dimensions  # variable for go through the matrix in secondary diagonal
for current_row_index in range(squared_matrix_dimensions):
    secondary_diagonal_column -= 1  # dynamic variable similar to this for the row but with backspin
    secondary_diagonal_sum += matrix[current_row_index][secondary_diagonal_column]

difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(difference)
