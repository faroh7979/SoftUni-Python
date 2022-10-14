def triangle_printing(triangle_size: int):

    for all_num in range(1, triangle_size + 1):
        for current_row_num in range(1, all_num + 1):
            print(current_row_num, end=' ')
        print()

    for all_num_descending in range(triangle_size - 1, 0, - 1):
        for current_row_descending in range(1, all_num_descending + 1):
            print(current_row_descending, end=' ')
        print()
