from math import floor

needed_hours = int(input())
days_to_deliver = int(input())
workers_extra_time = int(input())

regular_work_hours = days_to_deliver * 0.9 * 8
extra_work_hours = days_to_deliver * workers_extra_time * 2
total_work_time = floor(regular_work_hours + extra_work_hours)

difference = abs(total_work_time - needed_hours)

if needed_hours <= total_work_time:
    print(f"Yes!{difference} hours left.")
else:
    print(f"Not enough time!{difference} hours needed.")
