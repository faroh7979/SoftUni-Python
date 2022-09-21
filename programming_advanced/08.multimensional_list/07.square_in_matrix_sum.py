matrix_rows, matrix_columns = [int(i) for i in input().split(', ')]

matrix = []
for row in range(matrix_rows):
    columns = [int(i) for i in input().split(", ")]
    matrix.append(columns)

best_score = 0
best_score_values = []
best_score_column_index = 0  # in case if equal should choose the very left sub matrix
for current_row in range(matrix_rows - 1):  # protection of index failure
    for current_column in range(matrix_columns - 1):  # protection of index failure
        # need it to iterate on 2X2 square sub matrix
        current_score = matrix[current_row][current_column] + matrix[current_row][current_column + 1] +\
                        matrix[current_row + 1][current_column] + matrix[current_row + 1][current_column + 1]

        if current_score > best_score:
            best_score = current_score
            best_score_values = list()
            best_score_values.append((matrix[current_row][current_column], matrix[current_row][current_column + 1]))
            best_score_values.append(
                                (matrix[current_row + 1][current_column], matrix[current_row + 1][current_column + 1]))
            best_score_column_index = current_column

        elif current_score == best_score:
            if current_column < best_score_column_index:  # this sub matrix is more left than previous one
                best_score_values = list()
                best_score_values.append((matrix[current_row][current_column], matrix[current_row][current_column + 1]))
                best_score_values.append(
                    (matrix[current_row + 1][current_column], matrix[current_row + 1][current_column + 1]))
                best_score_column_index = current_column

for element in best_score_values:
    print(" ".join(map(str, element)))
print(best_score)
