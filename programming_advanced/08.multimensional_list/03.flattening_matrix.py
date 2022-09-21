matrix_rows = int(input())

original_matrix = []
for current_row in range(matrix_rows):
    current_column = [int(i) for i in input().split(', ')]
    original_matrix.append(current_column)

flattened_matrix = [i for sublist in original_matrix for i in sublist]

print(flattened_matrix)
