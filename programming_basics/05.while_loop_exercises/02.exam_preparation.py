limit_of_weak_evaluates = int(input())
total_tasks = 0
total_weak_evaluation = 0
total_score = 0
last_task = ''
is_graduated = False
while total_weak_evaluation < limit_of_weak_evaluates:
    task_name = input()
    if task_name == 'Enough':
        is_graduated = True
        break
    evaluate = float(input())
    total_tasks += 1
    total_score += evaluate
    last_task = task_name
    if evaluate <= 4:
        total_weak_evaluation += 1
average_evaluate = total_score / total_tasks
if is_graduated:
    print(f'Average score: {average_evaluate:.2f}')
    print(f'Number of problems: {total_tasks}')
    print(f'Last problem: {last_task}')
else:
    print(f'You need a break, {total_weak_evaluation} poor grades.')
