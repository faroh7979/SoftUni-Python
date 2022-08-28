gift_names = input().split(' ')
command = input()

while command != 'No Money':
    current_command = command.split(' ')
    command_type = current_command[0]
    gift = current_command[1]
    if command_type == 'OutOfStock':
        if gift in gift_names:
            count_find = gift_names.count(gift)
            for _ in range(count_find):
                gift_index = gift_names.index(gift)
                gift_names.remove(gift)
                gift_names.insert(gift_index, 'None')
    elif command_type == 'Required':
        index = int(current_command[2])
        if 0 <= index < len(gift_names):
            gift_names.pop(index)
            gift_names.insert(index, gift)
    elif command_type == 'JustInCase':
        last_index = len(gift_names) - 1
        if gift_names[last_index] != 'None':
            gift_names.pop(last_index)
            gift_names.insert(last_index, gift)
        else:
            gift_names.pop(last_index - 1)
            gift_names.insert(last_index - 1, gift)
    command = input()
if "None" in gift_names:
    none_count = gift_names.count('None')
    for _ in range(none_count):
        gift_names.remove('None')
for current_index in range(len(gift_names)):
    print(gift_names[current_index], end=" ")
