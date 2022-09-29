matrix_size = int(input())
matrix = [[int(i) if i.isdigit() else i for i in input().split()] for _ in range(matrix_size)]

alice_position = tuple()
for row_index in range(matrix_size):
    for col_index in range(matrix_size):

        if matrix[row_index][col_index] == 'A':
            alice_position = (row_index, col_index)
            matrix[row_index][col_index] = '*'  # need to mark Alice path with asterix
            break  # need only her position

alice_row = alice_position[0]
alice_col = alice_position[1]
alice_is_lost = False
total_collected_tea = 0
while True:
    command = input()

    if command == 'up':
        alice_row -= 1

        if alice_row < 0:
            alice_is_lost = True
            break

        if matrix[alice_row][alice_col] == 'R':
            matrix[alice_row][alice_col] = '*'
            alice_is_lost = True
            break

        if type(matrix[alice_row][alice_col]) == int:
            total_collected_tea += matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = '*'

            if total_collected_tea >= 10:
                break

        else:
            matrix[alice_row][alice_col] = '*'

    elif command == 'down':
        alice_row += 1

        if alice_row >= matrix_size:
            alice_is_lost = True
            break

        if matrix[alice_row][alice_col] == 'R':
            matrix[alice_row][alice_col] = '*'
            alice_is_lost = True
            break

        if type(matrix[alice_row][alice_col]) == int:
            total_collected_tea += matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = '*'

            if total_collected_tea >= 10:
                break

        else:
            matrix[alice_row][alice_col] = '*'

    elif command == 'left':
        alice_col -= 1

        if alice_col < 0:
            alice_is_lost = True
            break

        if matrix[alice_row][alice_col] == 'R':
            matrix[alice_row][alice_col] = '*'
            alice_is_lost = True
            break

        if type(matrix[alice_row][alice_col]) == int:
            total_collected_tea += matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = '*'

            if total_collected_tea >= 10:
                break

        else:
            matrix[alice_row][alice_col] = '*'

    elif command == 'right':
        alice_col += 1

        if alice_col >= matrix_size:
            alice_is_lost = True
            break

        if matrix[alice_row][alice_col] == 'R':
            matrix[alice_row][alice_col] = '*'
            alice_is_lost = True
            break

        if type(matrix[alice_row][alice_col]) == int:
            total_collected_tea += matrix[alice_row][alice_col]
            matrix[alice_row][alice_col] = '*'

            if total_collected_tea >= 10:
                break

        else:
            matrix[alice_row][alice_col] = '*'

if alice_is_lost:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")

for element in matrix:
    for sub_element in element:
        print(sub_element, end=' ')
    print()
