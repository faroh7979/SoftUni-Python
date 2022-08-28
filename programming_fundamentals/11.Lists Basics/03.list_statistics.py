number_of_integers = int(input())
positive_list = []
negative_list = []
negative_sum = 0
for _ in range(number_of_integers):
    current_num = int(input())
    if current_num >= 0:
        positive_list.append(current_num)
    else:
        negative_list.append(current_num)
positive_nums = positive_list.__len__()
for i in range(len(negative_list)):
    negative_sum += negative_list[i]

print(positive_list)
print(negative_list)
print(f'Count of positives: {positive_nums}')
print(f'Sum of negatives: {negative_sum}')
