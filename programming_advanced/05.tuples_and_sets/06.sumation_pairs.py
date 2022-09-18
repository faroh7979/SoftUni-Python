sequence_of_numbers = list(map(int, input().split()))
target_number = int(input())
used_in_winning_pairs = []
winning_pairs = []

for current_index in range(len(sequence_of_numbers)):
    if current_index in used_in_winning_pairs:  # in case that this value has been already used
        continue

    first_num = sequence_of_numbers[current_index]

    for index_second_num in range(current_index + 1, len(sequence_of_numbers)):
        if index_second_num in used_in_winning_pairs:  # again in case that this value has been already used
            continue

        second_num = sequence_of_numbers[index_second_num]

        if first_num + second_num == target_number:  # winning pair
            winning_pairs.append(f'{first_num} + {second_num} = {target_number}')
            used_in_winning_pairs.append(current_index)
            used_in_winning_pairs.append(index_second_num)
            break

print("\n".join(winning_pairs))
