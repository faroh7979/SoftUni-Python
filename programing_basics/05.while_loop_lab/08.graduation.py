name = input()
grade = 1
is_graduated = True
total_score = 0
failed_times = 0

while grade < 13:
    evaluate = float(input())
    if evaluate < 4:
        failed_times += 1
        if failed_times > 1:
            is_graduated = False
            break
        evaluate = float(input())
        if evaluate < 4:
            is_graduated = False
            break
        else:
            total_score += evaluate
    else:
        total_score += evaluate
    grade += 1
average_grade = total_score / (grade - 1)

if is_graduated:
    print(f'{name} graduated. Average grade: {average_grade:.2f}')
else:
    print(f'{name} has been excluded at {grade} grade')
