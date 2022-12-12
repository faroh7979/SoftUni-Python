def squares(total_nums: int):
    num = 1

    while num <= total_nums:
        yield num**2
        num += 1


print(list(squares(5)))
