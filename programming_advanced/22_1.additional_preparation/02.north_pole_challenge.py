rows, cols = [int(i) for i in input().split(', ')]
matrix = [[i for i in input().split()]for _ in range(rows)]

total_items = 0
start_row, start_col = 0, 0

items_dict = {
    'D': 0,
    'G': 0,
    'C': 0
}

for row_index in range(rows):
    for col_index in range(cols):
        if matrix[row_index][col_index] != '.':
            total_items += 1
            if matrix[row_index][col_index] == 'Y':
                total_items -= 1
                start_row, start_col = row_index, col_index
                matrix[row_index][col_index] = 'x'

while total_items:
    command_input = input()
    if command_input == 'End':
        break

    direction, steps = command_input.split('-')

    if direction == 'right':

        for _ in range(int(steps)):
            start_col += 1

            if start_col >= cols:
                start_col = 0

            current_position = matrix[start_row][start_col]
            matrix[start_row][start_col] = 'x'

            if current_position in items_dict:
                items_dict[current_position] += 1
                total_items -= 1

                if not total_items:
                    break

    elif direction == 'left':
        for _ in range(int(steps)):
            start_col -= 1

            if start_col < 0:
                start_col = cols - 1

            current_position = matrix[start_row][start_col]
            matrix[start_row][start_col] = 'x'

            if current_position in items_dict:
                items_dict[current_position] += 1
                total_items -= 1

                if not total_items:
                    break

    elif direction == 'up':
        for _ in range(int(steps)):
            start_row -= 1

            if start_row < 0:
                start_row = rows - 1

            current_position = matrix[start_row][start_col]
            matrix[start_row][start_col] = 'x'

            if current_position in items_dict:
                items_dict[current_position] += 1
                total_items -= 1

                if not total_items:
                    break

    elif direction == 'down':
        for _ in range(int(steps)):
            start_row += 1

            if start_row >= rows:
                start_row = 0

            current_position = matrix[start_row][start_col]
            matrix[start_row][start_col] = 'x'

            if current_position in items_dict:
                items_dict[current_position] += 1
                total_items -= 1

                if not total_items:
                    break

matrix[start_row][start_col] = 'Y'

if not total_items:
    print("Merry Christmas!")

print("You've collected:")

for key, value in items_dict.items():
    if key == 'D':
        print(f'- {value} Christmas decorations')
    elif key == 'G':
        print(f'- {value} Gifts')
    elif key == 'C':
        print(f'- {value} Cookies')

for final_row in matrix:
    print(" ".join(final_row))
