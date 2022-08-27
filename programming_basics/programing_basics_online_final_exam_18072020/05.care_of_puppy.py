total_food = int(input())
eaten_food = 0
total_food_grams = total_food * 1000
daily_eaten = input()

while daily_eaten != 'Adopted':
    daily_eaten = int(daily_eaten)
    eaten_food += daily_eaten
    daily_eaten = input()
difference = abs(total_food_grams - eaten_food)
if total_food_grams >= eaten_food:
    print(f'Food is enough! Leftovers: {difference:.0f} grams.')
else:
    print(f'Food is not enough. You need {difference:.0f} grams more.')
