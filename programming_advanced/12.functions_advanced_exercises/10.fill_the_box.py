def fill_the_box(height, length, width, *args):
    volume = height * length * width
    free_volume = volume
    rested_cubes = 0
    the_cube_is_full = False

    for cube in args:
        if cube == 'Finish':
            break

        if not the_cube_is_full:
            if free_volume >= cube:
                free_volume -= cube
            else:
                the_cube_is_full = True
                cube -= free_volume
                rested_cubes += cube

        else:
            rested_cubes += cube

    if the_cube_is_full:
        return f'No more free space! You have {rested_cubes} more cubes.'
    else:
        return f'There is free space in the box. You could put {free_volume} more cubes.'


print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
