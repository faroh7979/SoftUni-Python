from math import ceil
nums = input()
num_list = list(map(int, nums.split(', ')))
max_num = max(num_list)
total_ranges = ceil(max_num / 10)

for list_num in range(1, total_ranges + 1):
    current_list = [nums for nums in num_list if nums <= 10 * list_num and nums > (list_num - 1) * 10]
    print(f"Group of {10 * list_num}'s: {current_list}")
