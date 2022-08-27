total_budget = int(input())
season = input()
total_fisherman = int(input())

price = 0
is_autumn = season == "Autumn"

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if total_fisherman <= 6:
    price *= 0.90
elif 7 <= total_fisherman <= 11:
    price *= 0.85
elif total_fisherman >= 12:
    price *= 0.75

if total_fisherman % 2 == 0 and not is_autumn:
    price *= 0.95

difference = abs(price - total_budget)

if total_budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
