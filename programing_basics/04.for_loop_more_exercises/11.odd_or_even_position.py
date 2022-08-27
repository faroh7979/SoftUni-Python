from sys import maxsize

total_nums = int(input())
odds_sum = 0
odds_min = maxsize
odds_max = -maxsize
odds_count = 0
even_sum = 0
even_min = maxsize
even_max = -maxsize
even_count = 0
for nums in range(1, total_nums + 1):
    current_number = float(input())
    if nums % 2 != 0:
        odds_sum += current_number
        odds_count += 1
        if current_number < odds_min:
            odds_min = current_number
        if current_number > odds_max:
            odds_max = current_number
    else:
        even_sum += current_number
        even_count += 1
        if current_number < even_min:
            even_min = current_number
        if current_number > even_max:
            even_max = current_number
if odds_count == 0:
    print(f'OddSum={odds_sum:.2f},')
    print(f'OddMin=No,')
    print(f'OddMax=No,')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
elif even_count == 0:
    print(f'OddSum={odds_sum:.2f},')
    print(f'OddMin={odds_min:.2f},')
    print(f'OddMax={odds_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'OddSum={odds_sum:.2f},')
    print(f'OddMin={odds_min:.2f},')
    print(f'OddMax={odds_max:.2f},')
    print(f'EvenSum={even_sum:.2f},')
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')
