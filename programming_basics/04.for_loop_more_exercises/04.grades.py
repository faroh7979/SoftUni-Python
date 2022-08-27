total_students = int(input())
weak = 0
average = 0
good = 0
very_good = 0
sum_evaluate = 0

for evaluate in range(total_students):
    current_evaluate = float(input())
    sum_evaluate += current_evaluate
    if current_evaluate < 3:
        weak += 1
    elif current_evaluate < 4:
        average += 1
    elif current_evaluate < 5:
        good += 1
    else:
        very_good += 1
top_students = very_good / total_students * 100
good_students = good / total_students * 100
average_students = average / total_students * 100
weak_students = weak / total_students * 100
average = sum_evaluate / total_students

print(f'Top students: {top_students:.2f}%')
print(f'Between 4.00 and 4.99: {good_students:.2f}%')
print(f'Between 3.00 and 3.99: {average_students:.2f}%')
print(f'Fail: {weak_students:.2f}%')
print(f'Average: {average:.2f}')
