from collections import deque

material_level = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

# present that searching for, need to be counted
present_dictionary = {
    150: {
        'name': 'Doll',
        'crafted_times': 0
    },
    250: {
        'name': 'Wooden train',
        'crafted_times': 0
    },
    300: {
        'name': 'Teddy bear',
        'crafted_times': 0
    },
    400: {
        'name': 'Bicycle',
        'crafted_times': 0
    }
}
presents_are_crafted = False

crafted_presents = set()
first_winning_pair = {150, 250}
second_winning_pair = {300, 400}

while material_level and magic_level:
    current_material = material_level.pop()
    current_magic = magic_level.popleft()
    total_level = current_material * current_magic

    if total_level in present_dictionary:
        crafted_presents.add(total_level)  # adding the crafted present
        present_dictionary[total_level]['crafted_times'] += 1
        # checking if we have crafted needed pair of presents
        if crafted_presents.issuperset(first_winning_pair) or crafted_presents.issuperset(second_winning_pair):
            presents_are_crafted = True

    elif total_level < 0:
        new_material = current_material + current_magic
        material_level.append(new_material)

    elif total_level > 0:
        current_material += 15
        material_level.append(current_material)

    elif total_level == 0:
        if current_material != 0:
            material_level.append(current_material)

        elif current_magic != 0:
            magic_level.appendleft(current_magic)

if presents_are_crafted:
    print('The presents are crafted! Merry Christmas!')
else:
    print("No presents this Christmas!")

material_level_reversed = list(material_level)[::-1]  # need to print in reverse order
if material_level:
    print(f'Materials left: {", ".join(map(str, material_level_reversed))}')
elif magic_level:
    print(f'Magic left: {", ".join(map(str, magic_level))}')

# set a new dictionary contains needed value for name that should be sorted and their times of crafting
final_sorted_dict = {}
for key in present_dictionary:
    new_key = present_dictionary[key]['name']
    times = present_dictionary[key]['crafted_times']
    final_sorted_dict[new_key] = times

# need to set a list with name of new keys to sort them
list_for_sorting = []
for key in final_sorted_dict:
    list_for_sorting.append(key)

for key in sorted(list_for_sorting):
    if final_sorted_dict[key] > 0:
        print(f'{key}: {final_sorted_dict[key]}')
