total_letters = int(input())
current_line = ''

for first_letter in range(97, 97 + total_letters):
    for second_letter in range(97, 97 + total_letters):
        for third_letter in range(97, 97 + total_letters):
            current_line = chr(first_letter) + chr(second_letter) + chr(third_letter)
            print(current_line)