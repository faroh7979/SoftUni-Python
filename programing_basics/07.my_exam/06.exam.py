total_locations = int(input())
total_gold_incomes_on_this_location = 0
for current_location in range(total_locations):
    current_expected_income = float(input())
    total_days_on_this_location = int(input())
    total_gold_incomes_on_this_location = 0
    for day in range(total_days_on_this_location):
        current_gold_income = float(input())
        total_gold_incomes_on_this_location += current_gold_income
    average_gold_per_day = total_gold_incomes_on_this_location / total_days_on_this_location
    if average_gold_per_day >= current_expected_income:
        print(f'Good job! Average gold per day: {average_gold_per_day:.2f}.')
    else:
        needed_more_gold = current_expected_income - average_gold_per_day
        print(f'You need {needed_more_gold:.2f} gold.')
