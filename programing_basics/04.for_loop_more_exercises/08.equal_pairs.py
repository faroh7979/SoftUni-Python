from sys import maxsize

total_pairs = int(input())
min_score = maxsize
max_score = -maxsize
max_dif = -maxsize

for pairs in range(total_pairs):
    first_number = int(input())
    second_number = int(input())
    if pairs > 0:
        for nested_pairs in range(total_pairs):
            difference = abs(total_current_score - first_number - second_number)
            if difference >= max_dif:
                max_dif = difference
    total_current_score = first_number + second_number

    if total_current_score <= min_score:
        min_score = total_current_score
    if total_current_score >= max_score:
        max_score = total_current_score

if min_score == max_score:
    print(f'Yes, value={min_score}')
else:
    difference = max_score - min_score
    print(f'No, maxdiff={max_dif}')
