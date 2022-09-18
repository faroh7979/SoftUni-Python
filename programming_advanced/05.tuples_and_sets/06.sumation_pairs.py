sequence_of_numbers = list(map(int, input().split()))
target_number = int(input())
second_list = sequence_of_numbers[1:]
final_list = []
winning_pairs = False

for current_index in range(len(sequence_of_numbers)):
    first_num = sequence_of_numbers[current_index]

    for second_index in range(len(second_list)):
        second_num = second_list[second_index]

        if first_num + second_num == target_number:
            final_list.append(f'{first_num} + {second_num} = {target_number}')
            sequence_of_numbers.remove(second_num)
            second_list.remove(first_num)
            second_list.remove(second_num)
            break

    sequence_of_numbers.remove(first_num)
    if not sequence_of_numbers:
        break

print("\n".join(final_list))
