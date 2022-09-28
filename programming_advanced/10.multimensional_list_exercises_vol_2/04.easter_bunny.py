from sys import maxsize

matrix_size = int(input())
matrix = [[int(i) if i.isdigit() else i for i in input().split()] for _ in range(matrix_size)]
best_direction = ''
directions_tuple = (
    (1, 0),
    (- 1, 0),
    (0, 1),
    (0, - 1)
)

bunny_position = []
for row in range(matrix_size):
    for col in range(matrix_size):
        if matrix[row][col] == 'B':
            bunny_position.append(row)
            bunny_position.append(col)

best_score = - maxsize
best_direction = ''
best_route = []
for direction in directions_tuple:
    current_score = 0
    current_row = bunny_position[0]
    current_column = bunny_position[1]
    current_route = []

    while True:
        current_row += direction[0]
        current_column += direction[1]

        # Checking for invalid index and traps
        if 0 > current_row or current_row >= matrix_size\
                or 0 > current_column or current_column >= matrix_size:
            break

        if matrix[current_row][current_column] == 'X':
            break

        else:
            if type(matrix[current_row][current_column]) == int:

                current_score += matrix[current_row][current_column]
                current_route.append([current_row, current_column])

            else:
                break

        if current_score > best_score:
            best_score = current_score
            best_direction = direction
            best_route = current_route

if best_direction == (1, 0):
    best_direction = 'down'

elif best_direction == (- 1, 0):
    best_direction = 'up'

elif best_direction == (0, 1):
    best_direction = 'right'

elif best_direction == (0, - 1):
    best_direction = 'left'

print(best_direction)
for element in best_route:
    print(element)
print(best_score)
