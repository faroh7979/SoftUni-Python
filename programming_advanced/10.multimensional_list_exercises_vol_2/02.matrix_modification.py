squared_matrix_dimensions = int(input())

matrix = [[int(i) for i in input().split()] for i in range(squared_matrix_dimensions)]

while True:
    command_input = input()
    if command_input == 'END':
        break

    command = command_input.split()

    command_type = command[0]
    row = int(command[1])
    column = int(command[2])
    extra_number = int(command[3])

    if 0 <= row < squared_matrix_dimensions and 0 <= column < squared_matrix_dimensions:  # checking for valid index
        if command_type == 'Add':
            matrix[row][column] += extra_number

        elif command_type == 'Subtract':
            matrix[row][column] -= extra_number

    else:
        print('Invalid coordinates')

for element in matrix:
    for sub_element in element:
        print(sub_element, end=' ')
    print()
