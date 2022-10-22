ROWS = int(input())
COLS = ROWS
car_number = input()

kilometers_passed = 0
tunel_coordinates = []
finish_coordinates = []
matrix = []

car_row = 0
car_col = 0
for current_row in range(ROWS):
    current_col = input().split()
    matrix.append(current_col)
    if 'T' in current_col:
        for current_index in range(COLS):
            if current_col[current_index] == 'T':
                tunel_coordinates.append([current_row, current_index])
    if 'F' in current_col:
        current_index = current_col.index('F')
        finish_coordinates.append([current_row, current_index])

cross_finish_line = False
direction = input()
while direction != 'End':

    if direction == 'up':
        car_row -= 1

    elif direction == 'down':
        car_row += 1

    elif direction == 'right':
        car_col += 1

    elif direction == 'left':
        car_col -= 1

    current_position = matrix[car_row][car_col]

    if current_position == 'T':
        for elements in tunel_coordinates:
            tunel_row, tunel_col = elements
            matrix[tunel_row][tunel_col] = '.'
            if tunel_row != car_row or tunel_col != car_col:
                car_row = tunel_row
                car_col = tunel_col
        kilometers_passed += 20

    elif current_position == 'F':

        kilometers_passed += 10
        cross_finish_line = True
        break

    matrix[car_row][car_col] = 'C'

    kilometers_passed += 10

    matrix[car_row][car_col] = '.'

    direction = input()

matrix[car_row][car_col] = 'C'
if cross_finish_line:
    print(f'Racing car {car_number} finished the stage!')
else:
    print(f'Racing car {car_number} DNF.')

print(f'Distance covered {kilometers_passed} km.')
for row in matrix:
    print(''.join(row))
