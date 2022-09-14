country_list = input().split(', ')
capital_list = input().split(', ')
full_list = []
capital_dict = {}

for current_index in range(len(country_list)):
    full_list.append(country_list[current_index])
    full_list.append(capital_list[current_index])

for current_list_index in range(0, len(full_list), 2):
    capital_dict[full_list[current_list_index]] = full_list[current_list_index + 1]

for key, value in capital_dict.items():
    print(f'{key} -> {value}')
