season = input()
group_type = input()
total_scholars = int(input())
total_nights = int(input())
sport = ""
price_per_scholar = 0

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price_per_scholar = 9.60
    elif group_type == "mixed":
        price_per_scholar = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price_per_scholar = 7.20
    elif group_type == "mixed":
        price_per_scholar = 9.50
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        price_per_scholar = 15
    elif group_type == "mixed":
        price_per_scholar = 20
        sport = "Swimming"
if 10 <= total_scholars < 20:
    price_per_scholar *= 0.95
elif 20 <= total_scholars < 50:
    price_per_scholar *= 0.85
elif total_scholars >= 50:
    price_per_scholar *= 0.5
if season == "Winter":
    if group_type == "girls":
        sport = "Gymnastics"
    elif group_type == "boys":
        sport = "Judo"
elif season == "Spring":
    if group_type == "girls":
        sport = "Athletics"
    elif group_type == "boys":
        sport = "Tennis"
elif season == "Summer":
    if group_type == "girls":
        sport = "Volleyball"
    elif group_type == "boys":
        sport = "Football"

total_price = total_scholars * price_per_scholar * total_nights
print(f"{sport} {total_price:.2f} lv.")
