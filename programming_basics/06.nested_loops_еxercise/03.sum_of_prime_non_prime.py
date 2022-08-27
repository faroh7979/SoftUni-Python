customer_num = input()
prime_nums_sum = 0
non_prime_nums_sum = 0
is_prime = True
while customer_num != 'stop':
    customer_num = int(customer_num)
    if customer_num < 0:
        print(f'Number is negative.')
        customer_num = input()
        continue
    if customer_num > 1:
        for checks in range(2, customer_num):
            if customer_num % checks == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums_sum += customer_num
        else:
            non_prime_nums_sum += customer_num
    else:
        non_prime_nums_sum += customer_num
    is_prime = True
    customer_num = input()
print(f'Sum of all prime numbers is: {prime_nums_sum}')
print(f'Sum of all non prime numbers is: {non_prime_nums_sum}')
