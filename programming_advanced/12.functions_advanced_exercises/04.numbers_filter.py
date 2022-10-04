def even_odd_filter(**kwargs):
    nums_dict = {}

    for key, value in kwargs.items():
        if key == 'odd':
            nums_dict[key] = [i for i in value if i % 2 != 0]
        elif key == 'even':
            nums_dict[key] = [i for i in value if i % 2 == 0]

    return dict(sorted(nums_dict.items(), key=lambda x: -len(x[1])))


