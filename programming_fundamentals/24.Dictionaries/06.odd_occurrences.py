given_string_list = input()
given_string_list_lower = given_string_list.lower().split()
my_dict = {}

for current_string in given_string_list_lower:
    if current_string not in my_dict.keys():
        my_dict[current_string] = 1
    else:
        my_dict[current_string] += 1
for key, value in my_dict.items():
    if value % 2 != 0:
        print(f'{key}', end=" ")
