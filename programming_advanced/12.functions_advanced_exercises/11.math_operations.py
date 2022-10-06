def math_operations(*args, a: 0, s: 0, d: 0, m: 0):
    final_dict = {}
    for current_index, value in enumerate(args):
        if current_index == 0 or current_index % 4 == 0:  # first element
            a += value
        elif current_index == 1 or current_index % 5 == 0:  # second element
            s -= value
        elif current_index % 2 == 0:  # third element
            if value == 0:
                continue
            else:
                d /= value
        elif current_index % 3 == 0:  # fourth element
            m *= value

    final_dict['a'] = a
    final_dict['s'] = s
    final_dict['d'] = d
    final_dict['m'] = m

    final_dict = dict(sorted(final_dict.items(), key=lambda x: (-x[1], x[0])))
    final_string = ''

    for key, value in final_dict.items():
        final_string += f'{key}: {value:.1f}\n'

    return final_string


print(math_operations(6.0, a=0, s=0, d=5, m=0))
