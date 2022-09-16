    my_students_dict = {}
    my_course_num_submissions_dict = {}

    while True:
        command_line = input()
        if command_line == 'exam finished':
            break
        command = command_line.split('-')
        name = command[0]
        if len(command) == 3:
            course = command[1]
            score = int(command[2])
            if course not in my_students_dict:
                temporary_dict = {name: score}
                my_students_dict[course] = temporary_dict
                my_course_num_submissions_dict[course] = 1
            else:
                if name not in my_students_dict[course]:
                    my_students_dict[course][name] = score
                    my_course_num_submissions_dict[course] += 1
                else:
                    if my_students_dict[course][name] < score:
                        my_students_dict[course][name] = score
                        my_course_num_submissions_dict[course] += 1
                    else:
                        my_course_num_submissions_dict[course] += 1
        else:
            for current_course in my_students_dict:
                if name in my_students_dict[current_course]:
                    my_students_dict[current_course].pop(name)
    print("Results:")
    for current_course in my_students_dict:
        for current_student, current_score in my_students_dict[current_course].items():
            print(f'{current_student} | {current_score}')
    print('Submissions:')
    for last_key, last_value in my_course_num_submissions_dict.items():
        print(f'{last_key} - {last_value}')
