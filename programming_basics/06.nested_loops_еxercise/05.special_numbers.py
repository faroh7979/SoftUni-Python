customer_number = int(input())
start_range = 1111
end_range = 9999
is_special = True
for numbers in range(start_range, end_range + 1):
    for digits, values in enumerate(str(numbers)):
        is_special = True
        if int(values) == 0:
            is_special = False
            break
        elif customer_number % int(values) != 0:
            is_special = False
            break
    if is_special:
        print(numbers, end=' ')
