destination = input()
holiday_period = input()
total_nights = int(input())
single_night_price = 0

if destination == "France":
    if holiday_period == "21-23":
        single_night_price = 30
    elif holiday_period == "24-27":
        single_night_price = 35
    elif holiday_period == "28-31":
        single_night_price = 40
elif destination == "Italy":
    if holiday_period == "21-23":
        single_night_price = 28
    elif holiday_period == "24-27":
        single_night_price = 32
    elif holiday_period == "28-31":
        single_night_price = 39
elif destination == "Germany":
    if holiday_period == "21-23":
        single_night_price = 32
    elif holiday_period == "24-27":
        single_night_price = 37
    elif holiday_period == "28-31":
        single_night_price = 43

total_price = total_nights * single_night_price
print(f"Easter trip to {destination} : {total_price:.2f} leva.")
