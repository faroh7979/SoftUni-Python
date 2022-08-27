total_cats = int(input())
food_price_per_kilograms = 12.45
food_price_per_grams = food_price_per_kilograms / 1000
small_cats = 0
big_cats = 0
huge_cats = 0
total_eaten_food = 0
for cat in range(total_cats):
    eaten_food_grams = float(input())
    if eaten_food_grams < 200:
        small_cats += 1
    elif eaten_food_grams < 300:
        big_cats += 1
    else:
        huge_cats += 1
    total_eaten_food += eaten_food_grams
total_price = total_eaten_food * food_price_per_grams

print(f'Group 1: {small_cats} cats.')
print(f'Group 2: {big_cats} cats.')
print(f'Group 3: {huge_cats} cats.')
print(f'Price for food per day: {total_price:.2f} lv.')