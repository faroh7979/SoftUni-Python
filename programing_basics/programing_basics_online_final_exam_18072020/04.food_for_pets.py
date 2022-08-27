total_days = int(input())
total_food = float(input())
dog_total_food = 0
cat_total_food = 0
dog_biscuits = 0
cat_biscuits = 0
total_eaten_food = 0

for days in range(1, total_days + 1):
    dog_quantity = float(input())
    cat_quantity = float(input())
    if days % 3 == 0:
        dog_biscuits += dog_quantity * 0.1
        cat_biscuits += cat_quantity * 0.1
    cat_total_food += cat_quantity
    dog_total_food += dog_quantity
total_eaten_food = dog_total_food + cat_total_food
eaten_food = total_eaten_food / total_food * 100
dog_eaten_food = dog_total_food / total_eaten_food * 100
cat_eaten_food = cat_total_food / total_eaten_food * 100
total_eaten_biscuits = round(dog_biscuits + cat_biscuits, 1)

print(f'Total eaten biscuits: {total_eaten_biscuits:.0f}gr.')
print(f'{eaten_food:.2f}% of the food has been eaten.')
print(f'{dog_eaten_food:.2f}% eaten from the dog.')
print(f'{cat_eaten_food:.2f}% eaten from the cat.')
