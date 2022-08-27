total_moves = int(input())
total_score = 0
first_range = 0
second_range = 0
third_range = 0
fourth_range = 0
fifth_range = 0
invalid_range = 0

for moves in range(total_moves):
    current_number = int(input())
    if current_number < 0 or current_number > 50:
        invalid_range += 1
        total_score /= 2
    elif current_number < 10:
        first_range += 1
        total_score += current_number * 0.2
    elif current_number < 20:
        second_range += 1
        total_score += current_number * 0.3
    elif current_number < 30:
        third_range += 1
        total_score += current_number * 0.4
    elif current_number < 40:
        fourth_range += 1
        total_score += 50
    else:
        fifth_range += 1
        total_score += 100
first_percentage = first_range / total_moves * 100
second_percentage = second_range / total_moves * 100
third_percentage = third_range / total_moves * 100
fourth_percentage = fourth_range / total_moves * 100
fifth_percentage = fifth_range / total_moves * 100
invalid_percentage = invalid_range / total_moves * 100

print(f'{total_score:.2f}')
print(f'From 0 to 9: {first_percentage:.2f}%')
print(f'From 10 to 19: {second_percentage:.2f}%')
print(f'From 20 to 29: {third_percentage:.2f}%')
print(f'From 30 to 39: {fourth_percentage:.2f}%')
print(f'From 40 to 50: {fifth_percentage:.2f}%')
print(f'Invalid numbers: {invalid_percentage:.2f}%')
