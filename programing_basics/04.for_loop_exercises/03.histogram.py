count_of_numbers = int(input())
first_range = 0
second_range = 0
third_range = 0
fourth_range = 0
fifth_range = 0

for i in range(count_of_numbers):
    current_number = int(input())
    if current_number < 200:
        first_range += 1
    elif 200 <= current_number <= 399:
        second_range += 1
    elif 400 <= current_number <= 599:
        third_range += 1
    elif 600 <= current_number <= 799:
        fourth_range += 1
    elif current_number >= 800:
        fifth_range += 1
percentage_first_range_of_total = first_range / count_of_numbers * 100
percentage_second_range_of_total = second_range / count_of_numbers * 100
percentage_third_range_of_total = third_range / count_of_numbers * 100
percentage_fourth_range_of_total = fourth_range / count_of_numbers * 100
percentage_fifth_range_of_total = fifth_range / count_of_numbers * 100

print(f'{percentage_first_range_of_total:.2f}%')
print(f'{percentage_second_range_of_total:.2f}%')
print(f'{percentage_third_range_of_total:.2f}%')
print(f'{percentage_fourth_range_of_total:.2f}%')
print(f'{percentage_fifth_range_of_total:.2f}%')
