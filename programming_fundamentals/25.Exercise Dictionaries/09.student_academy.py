number_of_grades = int(input())
grades_dict = {}

for evaluate in range(number_of_grades):
    name = input()
    grade = input()
    if name not in grades_dict:
        grades_dict[name] = [float(grade), 1]
    else:
        grades_dict[name][0] += float(grade)
        grades_dict[name][1] += 1
for key in grades_dict:
    average_grade = grades_dict[key][0] / grades_dict[key][1]
    if average_grade >= 4.5:
        print(f'{key} -> {average_grade:.2f}')
