month = input()
total_nights = int(input())

atelier_expense = 0
apartment_expense = 0

if month == "May" or month == "October":
    atelier_expense = 50
    apartment_expense = 65
    if 7 < total_nights <= 14:
        atelier_expense *= 0.95
    elif total_nights > 14:
        atelier_expense *= 0.7
        apartment_expense *= 0.9
elif month == "June" or month == "September":
    atelier_expense = 75.20
    apartment_expense = 68.7
    if total_nights > 14:
        atelier_expense *= 0.8
        apartment_expense *= 0.9
elif month == "July" or month == "August":
    atelier_expense = 76
    apartment_expense = 77
    if total_nights > 14:
        apartment_expense *= 0.9
total_apartment_price = apartment_expense * total_nights
total_atelier_price = atelier_expense * total_nights
print(f"Apartment: {total_apartment_price:.2f} lv.")
print(f"Studio: {total_atelier_price:.2f} lv.")
