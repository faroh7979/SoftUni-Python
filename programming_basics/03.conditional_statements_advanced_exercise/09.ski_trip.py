vacation_days = int(input())
type_of_room = input()
evaluation = input()

vacation_nights = vacation_days - 1
price_per_night = 0

if type_of_room == "room for one person":
    price_per_night = 18
elif type_of_room == "apartment":
    price_per_night = 25
    if vacation_nights < 10:
        price_per_night *= 0.7
    elif 10 <= vacation_nights <= 15:
        price_per_night *= 0.65
    elif vacation_nights > 15:
        price_per_night *= 0.5
elif type_of_room == "president apartment":
    price_per_night = 35
    if vacation_nights < 10:
        price_per_night *= 0.9
    elif 10 <= vacation_nights <= 15:
        price_per_night *= 0.85
    elif vacation_nights > 15:
        price_per_night *= 0.8
total_expense = price_per_night * vacation_nights

if evaluation == "positive":
    total_expense *= 1.25
elif evaluation == "negative":
    total_expense *= 0.9

print(f"{total_expense:.2f}")
