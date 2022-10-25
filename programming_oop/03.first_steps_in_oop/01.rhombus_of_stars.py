def print_single_row(spaces, current_size):
    print(' ' * (current_size - spaces), end='')
    for _ in range(1, spaces + 1):
        print('* ', end='')
    print()


size = int(input())


for row in range(1, size + 1):
    print_single_row(row, size)

for row in range(size - 1, - 1, - 1):
    print_single_row(row, size)
