total_names = int(input())

odds_results = set()
even_results = set()

for current_row in range(1, total_names + 1):  # Should use the current_iterations, starting from 1
    current_name = input()
    ascii_sum = 0
    ascii_result = 0

    for symbol in current_name:
        ascii_sum += ord(symbol)
        ascii_result = int(ascii_sum / current_row)

    if ascii_result % 2 == 0:
        even_results.add(ascii_result)
    else:
        odds_results.add(ascii_result)

even_results_sum = sum(even_results)
odds_results_sum = sum(odds_results)

if even_results_sum == odds_results_sum:
    union_set = even_results.union(odds_results)
    print(f'{", ".join(map(str, union_set))}')

elif even_results_sum < odds_results_sum:
    symmetric_set = odds_results.difference(even_results)
    print(f'{", ".join(map(str, symmetric_set))}')

elif even_results_sum > odds_results_sum:
    symmetric_diff_set = even_results.symmetric_difference(odds_results)
    print(f'{", ". join(map(str, symmetric_diff_set))}')
