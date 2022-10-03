def sorting_cheeses(**kwargs):
    resulted = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    cheese_str = ''

    for key, value in resulted:
        sorted_result = sorted(value, reverse=True)
        cheese_str += key + '\n'
        cheese_str += '\n'.join(map(str, sorted_result)) + '\n'

    return cheese_str


