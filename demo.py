solution = False
for x in range(-100, 100):

    if solution:
        break

    for y in range(-100, 100):
        if 2 * x - 3 * y == 8:
            if 3 * x - 4 * y == 14:
                solution = True
                print(f'Triangle = {x}\nSquare = {y}')
                break
