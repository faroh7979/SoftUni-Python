portions = input()
beggars = int(input())
portion_list = portions.split(', ')
sum_list = []
current_beggar_sum = 0

for current_beggar in range(beggars):
    for current_index in range(current_beggar, len(portion_list), beggars):
        current_beggar_sum += int(portion_list[current_index])
    sum_list.append(current_beggar_sum)
    current_beggar_sum = 0
print(sum_list)
