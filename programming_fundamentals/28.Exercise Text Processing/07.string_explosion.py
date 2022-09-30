command_line = input()
command_line_list = []
indexes_explosion = []
indexes_strength = []

for index, value in enumerate(command_line):
    command_line_list.append(value)
    if value == '>':
        indexes_explosion.append(index)
        indexes_strength.append(int(command_line[index + 1]))
for current_index in range(len(indexes_explosion) - 1):
    difference = indexes_explosion[current_index] + indexes_strength[current_index] - indexes_explosion[current_index + 1]
    if difference >= 0:
        indexes_strength[current_index] = indexes_strength[current_index] - difference - 1
        indexes_strength[current_index + 1] += difference + 1
if indexes_strength[-1] + indexes_explosion[-1] >= len(command_line_list):
    difference_two = (indexes_strength[-1] + indexes_explosion[-1]) - (len(command_line_list) - 1)
    indexes_strength[-1] = indexes_strength[-1] - difference_two
indexes_explosion.reverse()
indexes_strength.reverse()
for removing in range(len(indexes_explosion)):
    start_index = indexes_explosion[removing] + 1
    end_index = start_index + indexes_strength[removing]
    for final_index in range(end_index - 1, start_index - 1, - 1):
        command_line_list.pop(final_index)

print("".join(command_line_list))
