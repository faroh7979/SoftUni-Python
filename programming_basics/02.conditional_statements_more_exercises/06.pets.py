from math import floor
from math import ceil

total_days = int(input())
left_food_kg = int(input())
dog_daily_food = float(input())
cat_daily_food = float(input())
turtle_daily_food_gram = float(input())

total_needed_food = dog_daily_food * total_days +\
                    cat_daily_food * total_days + \
                    turtle_daily_food_gram / 1000 * total_days

difference = abs(total_needed_food - left_food_kg)

if total_needed_food <= left_food_kg:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")
