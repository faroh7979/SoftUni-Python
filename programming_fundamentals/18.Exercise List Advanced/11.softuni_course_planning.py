initial_schedule = input()
schedule_list = initial_schedule.split(', ')

while True:
    initial_command = input()
    if initial_command == 'course start':
        break
    initial_command_list = initial_command.split(':')
    command = initial_command_list[0]
    lesson_title = initial_command_list[1]
    if command == 'Add':
        if lesson_title not in schedule_list:
            schedule_list.append(lesson_title)
    elif command == 'Insert':
        current_index = int(initial_command_list[2])
        if lesson_title not in schedule_list:
            schedule_list.insert(current_index, lesson_title)
    elif command == 'Remove':
        if lesson_title in schedule_list:
            schedule_list.remove(lesson_title)
        if f'{lesson_title}-Exercise' in schedule_list:
            schedule_list.remove(f'{lesson_title}-Exercise')
    elif command == 'Swap':
        second_lesson_title = initial_command_list[2]
        if lesson_title in schedule_list and second_lesson_title in schedule_list:
            first_title_index = schedule_list.index(lesson_title)
            second_title_index = schedule_list.index(second_lesson_title)
            schedule_list[first_title_index], schedule_list[second_title_index] =\
                schedule_list[second_title_index], schedule_list[first_title_index]
            if f'{lesson_title}-Exercise' in schedule_list and f'{second_lesson_title}-Exercise' in schedule_list:
                first_title_index_ex = schedule_list.index(f'{lesson_title}-Exercise')
                second_title_index_ex = schedule_list.index(f'{second_lesson_title}-Exercise')
                schedule_list[first_title_index_ex], schedule_list[second_title_index_ex] =\
                    schedule_list[second_title_index_ex], schedule_list[first_title_index_ex]
            elif f'{lesson_title}-Exercise' in schedule_list:
                lesson_title_swapped_index = schedule_list.index(lesson_title)
                schedule_list.remove(f'{lesson_title}-Exercise')
                schedule_list.insert(lesson_title_swapped_index + 1, f'{lesson_title}-Exercise')
            elif f'{second_lesson_title}-Exercise' in schedule_list:
                second_lesson_title_swapped_index = schedule_list.index(second_lesson_title)
                schedule_list.remove(f'{second_lesson_title}-Exercise')
                schedule_list.insert(second_lesson_title_swapped_index + 1, f'{second_lesson_title}-Exercise')
    elif command == 'Exercise':
        if lesson_title in schedule_list:
            lesson_index = schedule_list.index(lesson_title)
            if f'{lesson_title}-Exercise' not in schedule_list:
                schedule_list.insert(lesson_index + 1, f'{lesson_title}-Exercise')
        else:
            schedule_list.append(lesson_title)
            schedule_list.append(f'{lesson_title}-Exercise')
for indexes in range(1, len(schedule_list) + 1):
    if indexes == len(schedule_list):
        print(f' {indexes}.{"".join(schedule_list[indexes - 1])}', end="")
    else:
        print(f' {indexes}.{"".join(schedule_list[indexes - 1])}')
