master_dict = {}
helping_string = ''
while True:
    students_name = input()
    if ":" not in students_name:
        for symbol in students_name:
            if symbol == '_':
                helping_string += " "
            else:
                helping_string += symbol
        break
    students_name_upd = students_name.split(':')
    name = students_name_upd[0]
    student_id = int(students_name_upd[1])
    course = students_name_upd[2]
    master_dict[student_id] = {course: name}

for key in master_dict.keys():
    for second_key_nested, student_name in master_dict[key].items():
        if second_key_nested == helping_string:
            print(f'{student_name} - {key}')
