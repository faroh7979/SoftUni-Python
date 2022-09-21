rows, columns = [int(i) for i in input().split(', ')]

current_score = 0
matrix = []
for current_row in range(rows):
    current_column = [int(i) for i in input().split()]
    matrix.append(current_column)

for current_column_summing in range(columns):
    current_score = 0  # should be turned to 0 for every single column calculations

    for current_row_summing in range(rows):
        current_score += matrix[current_row_summing][current_column_summing]
    print(current_score)  # should be printed before go to the next one
