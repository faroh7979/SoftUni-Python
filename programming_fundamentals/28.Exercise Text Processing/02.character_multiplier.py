single_command_line = input()
single_command_line_list = single_command_line.split()
first_word = single_command_line_list[0]
second_word = single_command_line_list[1]
difference = len(first_word) - len(second_word)
total_sum = 0

if difference == 0:
    for current_index in range(len(first_word)):
        total_sum += ord(first_word[current_index]) * ord(second_word[current_index])
elif difference > 0:
    for second_current_index in range(len(second_word)):
        total_sum += ord(first_word[second_current_index]) * ord(second_word[second_current_index])
    for second_last_index in range(len(first_word) - abs(difference), len(first_word)):
        total_sum += ord(first_word[second_last_index])
elif difference < 0:
    for third_current_index in range(len(first_word)):
        total_sum += ord(first_word[third_current_index]) * ord(second_word[third_current_index])
    for third_last_index in range(len(second_word) - abs(difference), len(second_word)):
        total_sum += ord(second_word[third_last_index])
print(total_sum)
