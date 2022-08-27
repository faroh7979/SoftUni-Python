first_num = int(input())
second_num = int(input())
total_digits = int(len(str(first_num)))
odds_sum = 0
evens_sum = 0
for nums in range(first_num, second_num + 1):
    nums = str(nums)
    for digit in range(total_digits):
        if (digit + 1) % 2 == 0:
            evens_sum += int(nums[digit])
        else:
            odds_sum += int(nums[digit])
    if odds_sum == evens_sum:
        print(int(nums), end=' ')
    odds_sum = 0
    evens_sum = 0
