exam_starting_hours = int(input())
exam_starting_minutes = int(input())
arriving_hours = int(input())
arriving_minutes = int(input())

total_exam_time_minutes = exam_starting_hours * 60 + exam_starting_minutes
total_arriving_time_minutes = arriving_hours * 60 + arriving_minutes

difference = total_exam_time_minutes - total_arriving_time_minutes

difference_h = abs(difference) // 60
difference_m = abs(difference) % 60

if difference <= -60:
    print("Late")
    print(f"{difference_h}:{difference_m:02d} hours after the start")
elif -60 < difference < 0:
    print("Late")
    print(f"{difference_m} minutes after the start")
elif difference == 0:
    print("On Time")
elif 0 < difference <= 30:
    print("On time")
    print(f"{difference_m} minutes before the start")
elif 30 < difference < 60:
    print("Early")
    print(f"{difference_m:} minutes before the start")
else:
    print("Early")
    print(f"{difference_h}:{difference_m:02d} hours before the start")
