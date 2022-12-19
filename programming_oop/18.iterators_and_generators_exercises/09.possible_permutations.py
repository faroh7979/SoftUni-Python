def possible_permutations(numbers: list):
    new_list = sorted(numbers)
    for num in range(0, 10 **len(numbers) - 1):
        if num in
