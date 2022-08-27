budget = float(input())
destination = input()
season = input()
total_days = int(input())
daily_expense = 0

if destination == "Dubai":
    if season == "Winter":
        daily_expense = 45000
    elif season == "Summer":
        daily_expense = 40000
elif destination == "Sofia":
    if season == "Winter":
        daily_expense = 17000
    elif season == "Summer":
        daily_expense = 12500
elif destination == "London":
    if season == "Winter":
        daily_expense = 24000
    elif season == "Summer":
        daily_expense = 20250
if destination == "Dubai":
    daily_expense *= 0.7
elif destination == "Sofia":
    daily_expense *= 1.25
total_price = total_days * daily_expense
difference = abs(budget - total_price)
if budget >= total_price:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
