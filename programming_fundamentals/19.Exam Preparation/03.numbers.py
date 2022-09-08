numbers = input()
numbers_list = list(map(int, numbers.split()))
average_nums = sum(numbers_list) / len(numbers_list)
nums_above_50 = [num for num in numbers_list if num > average_nums]
nums_above_50.sort(reverse=True)
final_list = []

if len(nums_above_50) > 4:
    for numbers in range(5):
        final_list.append(nums_above_50[numbers])
    print(* final_list)
elif len(nums_above_50) > 0:
    print(* nums_above_50)
else:
    print('No')
