string_input = input()
my_dict = {}

for current_letter in string_input:
    if current_letter != " ":
        if current_letter not in my_dict.keys():
            my_dict[current_letter] = 1
        else:
            my_dict[current_letter] += 1

for key, element in my_dict.items():
    print(f'{key} -> {element}')
