sequence_integers = input()
sequence_integers_list = list(map(int, sequence_integers.split()))
sum_of_removed = 0

while True:
    if len(sequence_integers_list) == 0:
        break
    current_index = int(input())
    if current_index < 0:
        value_of_removed = sequence_integers_list[0]
        sequence_integers_list.pop(0)
        last_element = sequence_integers_list[-1]
        sequence_integers_list.insert(0, last_element)
        sum_of_removed += value_of_removed
        sequence_integers_list =\
            [less + value_of_removed if less <= value_of_removed else less - value_of_removed for less in sequence_integers_list]
    elif current_index >= len(sequence_integers_list):
        value_of_removed = sequence_integers_list[-1]
        sequence_integers_list.pop(-1)
        first_element = sequence_integers_list[0]
        sequence_integers_list.append(first_element)
        sum_of_removed += value_of_removed
        sequence_integers_list =\
            [less + value_of_removed if less <= value_of_removed else less - value_of_removed for less in sequence_integers_list]
    else:
        value_of_removed = sequence_integers_list[current_index]
        sequence_integers_list.pop(current_index)
        sum_of_removed += value_of_removed
        sequence_integers_list =\
            [less + value_of_removed if less <= value_of_removed else less - value_of_removed for less in sequence_integers_list]
print(sum_of_removed)
