student_dict = {}

while True:
    command_line = input()
    if command_line == 'end':
        break
    command = command_line.split(' : ')
    course = command[0]
    student_name = command[1]
    if course not in student_dict:
        student_dict[course] = [f'-- {student_name}']
    else:
        student_dict[course] += [f'-- {student_name}']
for key in student_dict:
    print(f'{key}: {len(student_dict[key])}')
    print(f'\n'.join(student_dict[key]))
