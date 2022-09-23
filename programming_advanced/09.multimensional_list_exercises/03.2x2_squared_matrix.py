rows, columns = map(int, input().split())

matrix = []
for row in range(rows):
    matrix.append([i for i in input().split()])

total_identical_matrices = 0
for current_row in range(rows - 1):  # should do it because we searched for 2X2 squared matrix
    for current_column in range(columns - 1):
        first_square = matrix[current_row][current_column]
        second_square = matrix[current_row][current_column + 1]
        third_square = matrix[current_row + 1][current_column]
        fourth_square = matrix[current_row + 1][current_column + 1]

        # checking if all mini matrix elements are equal
        if first_square == second_square and second_square == third_square and third_square == fourth_square:
            total_identical_matrices += 1

print(total_identical_matrices)
