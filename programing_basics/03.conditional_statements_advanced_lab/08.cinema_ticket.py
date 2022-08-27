week_day = input()

price = 0

if week_day == "Monday" or week_day == "Tuesday" or week_day == "Friday":
    price = 12
elif week_day == "Wednesday" or week_day == "Thursday":
    price = 14
elif week_day == "Saturday" or week_day == "Sunday":
    price = 16
print(price)
