import sys

rows, columns = map(int, input().split())

matrix = []
for row in range(rows):
    matrix.append([int(i) for i in input().split()])

best_matrix = ''
best_score = - sys.maxsize
for current_row in range(rows - 2):  # should do it because we searched for 3X3 squared matrix
    for current_column in range(columns - 2):

        first_element = matrix[current_row][current_column]
        second_element = matrix[current_row][current_column + 1]
        third_element = matrix[current_row][current_column + 2]
        fourth_element = matrix[current_row + 1][current_column]
        fifth_element = matrix[current_row + 1][current_column + 1]
        sixth_element = matrix[current_row + 1][current_column + 2]
        seventh_element = matrix[current_row + 2][current_column]
        eighth_element = matrix[current_row + 2][current_column + 1]
        ninth_element = matrix[current_row + 2][current_column + 2]
        current_score = first_element + second_element + third_element + fourth_element + fifth_element +\
            sixth_element + seventh_element + eighth_element + ninth_element

        if current_score > best_score:
            best_score = current_score
            best_matrix = f'{first_element} {second_element} {third_element}\n{fourth_element} {fifth_element} {sixth_element}\n{seventh_element} {eighth_element} {ninth_element}'

print(f'Sum = {best_score}')
print(best_matrix)
