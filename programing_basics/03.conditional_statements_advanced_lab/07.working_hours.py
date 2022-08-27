clock_hour = int(input())
weekday = input()

work_days = weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" \
           or weekday == "Friday" or weekday == "Saturday"
work_hours = 10 <= clock_hour <= 18

if work_days and work_hours:
    print("open")
else:
    print("closed")
