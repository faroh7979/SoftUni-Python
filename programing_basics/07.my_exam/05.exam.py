total_food_kilograms = int(input())
command_line = input()
total_food_grams = total_food_kilograms * 1000
total_eaten_food = 0
while command_line != 'Adopted':
    eaten_food = int(command_line)
    total_eaten_food += eaten_food
    command_line = input()
difference = abs(total_eaten_food - total_food_grams)

if total_eaten_food <= total_food_grams:
    print(f'Food is enough! Leftovers: {difference} grams.')
else:
    print(f'Food is not enough. You need {difference} grams more.')