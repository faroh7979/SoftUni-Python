rows, columns = map(int, input().split())
snake_string = input()

snake_final_dimensions = rows * columns  # how many symbols should be printed
snake_full_version = snake_string * snake_final_dimensions  # snake maximum version
snake_final_version = snake_full_version[:snake_final_dimensions]  # snake version according to dimension & full version

for row in range(rows):  # need of index to calculate the direction of movement
    current_string = ''
    if row % 2 == 0:  # right direction
        for column in range(columns):
            current_string += snake_final_version[(row * columns) + column]
        print(current_string)

    else:
        for column in range(columns - 1, -1, - 1):
            current_string += snake_final_version[(row * columns) + column]
        print(current_string)
