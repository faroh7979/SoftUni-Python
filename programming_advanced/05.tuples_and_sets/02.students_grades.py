number_of_students = int(input())
students_dict = {}

for _ in range(number_of_students):
    student_command = tuple(input().split())
    student_name = student_command[0]
    student_grade = float(student_command[1])

    if student_name not in students_dict:
        students_dict[student_name] = [student_grade]

    else:
        students_dict[student_name].append(student_grade)

for key in students_dict:
    grades_in_string = list(map(str, students_dict[key]))
    average_of_grades = sum(students_dict[key]) / len(students_dict[key])
    print(f'{key} -> ', end='')
    for evaluate in students_dict[key]:
        print(f'{evaluate:.2f}', end=" ")
    print(f'(avg: {average_of_grades:.2f})')
