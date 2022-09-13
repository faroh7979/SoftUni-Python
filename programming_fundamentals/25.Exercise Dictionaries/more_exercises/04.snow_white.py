dwarf_dict = {}
final_list = []
physics_list = []

while True:
    command_line = input()
    if command_line == "Once upon a time":
        break
    command_split = command_line.split(' <:> ')
    dwarf_name = command_split[0]
    dwarf_hat = command_split[1]
    dwarf_physics = int(command_split[2])
    if dwarf_hat not in dwarf_dict:
        dwarf_dict[dwarf_hat] = {dwarf_name: {'dwarf_physics': dwarf_physics}}
    else:
        if dwarf_dict[dwarf_hat] != dwarf_name:
            dwarf_dict[dwarf_hat][dwarf_name] = {'dwarf_physics': dwarf_physics}
        else:
            if dwarf_dict[dwarf_hat][dwarf_name]['dwarf_physics'] < dwarf_physics:
                dwarf_dict[dwarf_hat][dwarf_name]['dwarf_physics'] = dwarf_physics
# print(dwarf_dict)

for first_key in dwarf_dict:
    for second_key in dwarf_dict[first_key]:
        for third_key in dwarf_dict[first_key][second_key]:
            tempr_list = f'{first_key}, {second_key}, {third_key}, {dwarf_dict[first_key][second_key][third_key]}'
            temporary_list = tempr_list.split(', ')
            final_list.append(temporary_list)
for current_index in range(0, len(final_list)):
    physics_list.append(int(final_list[current_index][3]))
physics_list = sorted(physics_list, reverse=True)
for index, value in enumerate(physics_list):
    for add_index in range(0, len(final_list)):
        if int(final_list[index + add_index][3]) == value:
            object_ins = final_list[index + add_index]
            final_list[index].insert(index + add_index, object_ins)
            final_list.pop(index + add_index)
            break
print(final_list)
print(physics_list)