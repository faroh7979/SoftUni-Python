command = input()
final_list = []
while command != 'End':
    sorted_list = command.split('-')
    current_priority = int(sorted_list[0]) - 1
    current_task = sorted_list[1]
    final_list.append((current_priority, current_task))
    command = input()

sorted_task = [x[1] for x in sorted(final_list)]

print(sorted_task)
