from collections import deque

robots = input().split(';')
starting_time = list(map(int, input().split(':')))
current_time_seconds = starting_time[0] * 3600 + starting_time[1] * 60 + starting_time[2]
produced_item = ''

item_is_taken = True
robots_list = []
items_que = deque()

for robot in robots:
    current_list = []
    split_robot = robot.split('-')

    current_list.append(split_robot[0])
    current_list.append(int(split_robot[1]))
    current_list.append(int(current_time_seconds) + 1)

    robots_list.append(current_list)

while True:
    item = input()

    if item == 'End':
        break
    items_que.append(item)

while items_que:
    if not item_is_taken:
        items_que.append(produced_item)

    produced_item = items_que.popleft()
    current_time_seconds += 1
    hours = current_time_seconds // 3600
    minutes = (current_time_seconds - hours * 3600) // 60
    seconds = current_time_seconds - (hours * 3600 + minutes * 60)
    hours %= 24
    item_is_taken = False

    for current_index, working_robot in enumerate(robots_list):

        working_name = working_robot[0]
        working_time = working_robot[1]
        working_till = working_robot[2]

        if working_till <= current_time_seconds:
            working_robot[2] = working_robot[1] + current_time_seconds
            print(f'{working_name} - {produced_item} [{hours:02d}:{minutes:02d}:{seconds:02d}]')
            item_is_taken = True
            break

        if current_index == len(robots_list) - 1:
            items_que.append(produced_item)
            item_is_taken = True
