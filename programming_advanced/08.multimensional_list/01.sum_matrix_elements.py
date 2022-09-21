matrix_dimensions = input()
matrix_rows, matrix_columns = list(map(int, matrix_dimensions.split(', ')))
final_matrix = []
final_result = 0

for current_row in range(matrix_rows):
    current_column = list(map(int, input().split(', ')))
    final_matrix.append(current_column)  # the matrix is ready, but need to make another loop for summing it

    for element in current_column:
        final_result += element

print(final_result)
print(final_matrix)
