first_num = int(input())
second_num = int(input())

for barcodes in range(first_num, second_num + 1):
    there_is_even = False
    in_range = True
    for index, digit in enumerate(str(barcodes)):
        digit = int(digit)
        index = int(index)
        first_num_as_string = str(first_num)
        first_num_digit = int(first_num_as_string[index])
        second_num_as_string = str(second_num)
        second_num_digit = int(second_num_as_string[index])
        if digit == 0:
            there_is_even = True
            break
        elif digit % 2 == 0:
            there_is_even = True
            break
        if first_num_digit > digit or second_num_digit < digit:
            in_range = False
            break
    if not there_is_even and in_range:
        print(barcodes, end=' ')
