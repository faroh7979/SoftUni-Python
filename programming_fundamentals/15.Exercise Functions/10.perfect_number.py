def is_perfect(num: int):
    divisors_list = []
    for current_divisor in range(1, num):
        if num % current_divisor == 0:
            divisors_list.append(current_divisor)
    if sum(divisors_list) == num:
        return True
    return False


client_num = int(input())
if is_perfect(client_num):
    print('We have a perfect number!')
else:
    print("It's not so perfect.")
