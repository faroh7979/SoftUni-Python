total_days = int(input())
total_available_food = float(input())
cat_eaten_food = 0
dog_eaten_food = 0
total_eaten_biscuits = 0

for meals in range(1, total_days + 1):
    dog_eaten_food_current = int(input())
    cat_eaten_food_current = int(input())
    if meals % 3 == 0:
        total_eaten_biscuits += ((dog_eaten_food_current + cat_eaten_food_current) * 0.1)
    cat_eaten_food += cat_eaten_food_current
    dog_eaten_food += dog_eaten_food_current

total_eaten_food = dog_eaten_food + cat_eaten_food
percentage_total_eaten_food = total_eaten_food / total_available_food * 100
percentage_dog_eaten_food = dog_eaten_food / total_eaten_food * 100
percentage_cat_eaten_food = cat_eaten_food / total_eaten_food * 100

print(f'Total eaten biscuits: {total_eaten_biscuits:.0f}gr.')
print(f'{percentage_total_eaten_food:.2f}% of the food has been eaten. ')
print(f'{percentage_dog_eaten_food:.2f}% eaten from the dog.')
print(f'{percentage_cat_eaten_food:.2f}% eaten from the cat.')
