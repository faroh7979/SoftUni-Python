squared_matrix_size = int(input())

matrix = []
for current_row in range(squared_matrix_size):
    current_column = [int(col) for col in input().split(', ')]
    matrix.append(current_column)

primary_diagonal_elements = []
for current_matrix_index in range(squared_matrix_size):
    primary_diagonal_elements.append(matrix[current_matrix_index][current_matrix_index])

secondary_diagonal_elements = []
current_column_index = squared_matrix_size  # use it for temp variable to help go through the columns
for current_matrix_row_index in range(squared_matrix_size):
    current_column_index -= 1  # dynamicly changed to have the needed column index
    secondary_diagonal_elements.append(matrix[current_matrix_row_index][current_column_index])

print(f'Primary diagonal: {", ".join(map(str, primary_diagonal_elements))}. Sum: {sum(primary_diagonal_elements)}')
print(f'Secondary diagonal: {", ".join(map(str, secondary_diagonal_elements))}. Sum: {sum(secondary_diagonal_elements)}')
