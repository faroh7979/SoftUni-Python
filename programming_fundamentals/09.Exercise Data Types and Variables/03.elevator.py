total_persons = int(input())
capacity = int(input())
total_courses = ''

if capacity >= total_persons:
    total_courses = 1
else:
    total_full_courses = total_persons // capacity
    rested_person = total_persons % capacity
    if rested_person > 0:
        total_courses = total_full_courses + 1
    else:
        total_courses = total_full_courses
print(total_courses)