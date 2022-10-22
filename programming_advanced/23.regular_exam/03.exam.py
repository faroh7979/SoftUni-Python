def forecast(*args):
    final_dict = {}
    final_string = ''

    for element in args:
        location = element[0]
        weather = element[1]

        if weather == 'Sunny':
            final_dict[location] = '1Sunny'

        elif weather == 'Cloudy':
            final_dict[location] = '2Cloudy'

        elif weather == 'Rainy':
            final_dict[location] = '3Rainy'

    final_dict = dict(sorted(final_dict.items(), key=lambda x: (x[1], x[0])))

    for key, value in final_dict.items():
        final_string += f'{key} - {value[1:]}\n'

    return final_string

