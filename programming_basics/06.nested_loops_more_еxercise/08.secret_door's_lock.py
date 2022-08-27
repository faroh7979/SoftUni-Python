hundreds_ceil = int(input())
tens_ceil = int(input())
singles_ceil = int(input())
is_prime = True
for hundreds in range(1, hundreds_ceil + 1):
    if hundreds % 2 != 0:
        continue
    for tens in range(2, tens_ceil + 1):
        is_prime = True
        if tens != 2:
            for divider in range(2, tens):
                if tens % divider == 0:
                    is_prime = False
                    break
        if not is_prime:
            continue
        for singles in range(1, singles_ceil + 1):
            if singles % 2 != 0:
                continue
            print(f'{hundreds} {tens} {singles}')
