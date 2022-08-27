fruit = input()
week_day = input()
quantity = float(input())

valid_fruit = fruit == "banana" or fruit == "apple" or fruit == "orange" or fruit == "grapefruit" or fruit == "kiwi" \
              or fruit == "pineapple" or fruit == "grapes"

valid_day = week_day == "Monday" or week_day == "Tuesday" or week_day == "Wednesday" or week_day == "Thursday" \
            or week_day == "Friday" or week_day == "Saturday" or week_day == "Sunday"

workdays = week_day == "Monday" or week_day == "Tuesday" or week_day == "Wednesday" or week_day == "Thursday" \
            or week_day == "Friday"
weekends = week_day == "Saturday" or week_day == "Sunday"

price = 0

if workdays and fruit == "banana":
    price = 2.50
elif workdays and fruit == "apple":
    price = 1.20
elif workdays and fruit == "orange":
    price = 0.85
elif workdays and fruit == "grapefruit":
    price = 1.45
elif workdays and fruit == "kiwi":
    price = 2.70
elif workdays and fruit == "pineapple":
    price = 5.50
elif workdays and fruit == "grapes":
    price = 3.85
elif weekends and fruit == "banana":
    price = 2.70
elif weekends and fruit == "apple":
    price = 1.25
elif weekends and fruit == "orange":
    price = 0.90
elif weekends and fruit == "grapefruit":
    price = 1.60
elif weekends and fruit == "kiwi":
    price = 3.00
elif weekends and fruit == "pineapple":
    price = 5.60
elif weekends and fruit == "grapes":
    price = 4.20

total_price = price * quantity

if valid_fruit and valid_day:
    print(f"{total_price:.2f}")
else:
    print("error")
