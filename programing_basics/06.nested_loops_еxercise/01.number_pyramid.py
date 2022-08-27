total_nums = int(input())
counter = 1
all_is_printed = False
for rows in range(1, total_nums + 1):
    for columns in range(1, rows + 1):
        print(counter, end=' ')
        counter += 1
        if counter > total_nums:
            all_is_printed = True
            break
    if all_is_printed:
        break
    print()
