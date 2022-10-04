def integers_func(*args):
    positive_nums = []
    negative_nums = []

    for digit in args:
        if int(digit) < 0:
            negative_nums.append(int(digit))
        else:
            positive_nums.append(int(digit))

    positive_nums_sum = sum(positive_nums)
    negative_nums_sum = sum(negative_nums)

    if positive_nums_sum < abs(negative_nums_sum):
        return f'{negative_nums_sum}\n{positive_nums_sum}\nThe negatives are stronger than the positives'
    else:
        return f'{negative_nums_sum}\n{positive_nums_sum}\nThe positives are stronger than the negatives'


print(integers_func(*input().split()))
