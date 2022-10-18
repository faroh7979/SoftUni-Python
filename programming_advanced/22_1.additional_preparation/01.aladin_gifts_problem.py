from collections import deque


def present_checker(score):

    if score < 100:  # nothing to craft
        pass

    elif score <= presents_dictionary['Gemstone']['max_amount']:
        presents_dictionary['Gemstone']['crafted_times'] += 1

    elif score <= presents_dictionary['Porcelain Sculpture']['max_amount']:
        presents_dictionary['Porcelain Sculpture']['crafted_times'] += 1

    elif score <= presents_dictionary['Gold']['max_amount']:
        presents_dictionary['Gold']['crafted_times'] += 1

    elif score <= presents_dictionary['Diamond Jewellery']['max_amount']:
        presents_dictionary['Diamond Jewellery']['crafted_times'] += 1

    elif score > 500:  # nothing to craft
        pass

    return presents_dictionary


materials = [int(i) for i in input().split()]
magic_levels = deque(int(i) for i in input().split())
presents_dictionary = {
    'Gemstone':
        {
            'max_amount': 199,
            'crafted_times': 0},
    'Porcelain Sculpture':
        {
            'max_amount': 299,
            'crafted_times': 0},
    'Gold':
        {
            'max_amount': 399,
            'crafted_times': 0},
    'Diamond Jewellery':
        {
            'max_amount': 499,
            'crafted_times': 0},
}

while materials and magic_levels:
    material = materials.pop()
    magic = magic_levels.popleft()

    summing = material + magic

    if summing < 100:
        if summing % 2 == 0:
            new_sum = material * 2 + magic * 3
        else:
            new_sum = material * 2 + magic * 2

        present_checker(new_sum)

    elif summing > 499:
        new_sum = material / 2 + magic / 2

        present_checker(new_sum)

    else:
        present_checker(summing)

if (presents_dictionary['Gemstone']['crafted_times'] and presents_dictionary['Porcelain Sculpture']['crafted_times']) or \
        (presents_dictionary['Gold']['crafted_times'] and presents_dictionary['Diamond Jewellery']['crafted_times']):
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left: {", ".join(map(str, materials))}')
elif magic_levels:
    print(f'Magic left: {", ".join(map(str, magic_levels))}')

for key in sorted(presents_dictionary):
    if presents_dictionary[key]['crafted_times'] > 0:
        print(f'{key}: {presents_dictionary[key]["crafted_times"]}')
