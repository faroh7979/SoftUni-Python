def get_primes(numbers: list):
    while numbers:

        current_num = numbers.pop(0)
        is_prime = True

        if current_num > 1:
            for divider in range(2, current_num):
                if current_num % divider == 0:
                    is_prime = False
                    break

        else:
            is_prime = False

        if is_prime:
            yield current_num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))
