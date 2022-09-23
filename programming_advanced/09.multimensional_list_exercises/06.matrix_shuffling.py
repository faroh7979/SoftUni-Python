rows, columns = map(int, input().split())

matrix = []
for row in range(rows):
    matrix.append([i for i in input().split()])

while True:
    command = input().split()
    command_length = len(command)
    # check validity of all given indexes
    if command[0] == 'swap':
        if command_length == 5:
            first, second, third, fourth = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            if 0 <= first < rows and 0 <= second < columns and \
                    0 <= third < rows and 0 <= fourth < columns:
                # swapping of the two values
                first_value = matrix[first][second]
                second_value = matrix[third][fourth]
                matrix[first][second], matrix[third][fourth] = second_value, first_value
                for element in matrix:
                    for sub_element in element:
                        print(sub_element, end=" ")
                    print()

            else:
                print('Invalid input!')

    elif command[0] == 'END':
        break

    else:
        print('Invalid input!')
