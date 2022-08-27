weekday = input()

working_day = weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" or weekday == "Thursday" \
              or weekday == "Friday"
weekend = weekday == "Saturday" or weekday == "Sunday"

if working_day:
    print("Working day")
elif weekend:
    print("Weekend")
else:
    print("Error")
