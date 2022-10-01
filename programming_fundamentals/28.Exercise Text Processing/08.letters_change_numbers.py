game_string = input()
game_list = game_string.split()
total_sum = 0

for index, value in enumerate(game_list):
    first_letter = value[0]
    last_letter = value[-1]
    number = int(value[1:-1])
    if first_letter.isupper():
        current_sum = number / (ord(first_letter) - 64)
    else:
        current_sum = number * (ord(first_letter) - 96)
    if last_letter.isupper():
        second_sum = current_sum - (ord(last_letter) - 64)
        total_sum += second_sum
    else:
        second_sum = current_sum + (ord(last_letter) - 96)
        total_sum += second_sum
print(f'{total_sum:.2f}')
