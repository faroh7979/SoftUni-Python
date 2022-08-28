group_size = int(input())
days_of_adventure = int(input())
total_companions = group_size
my_coins = 0

for day_num in range(1, days_of_adventure + 1):
    my_coins += 50
    if day_num % 10 == 0:
        total_companions -= 2
    if day_num % 15 == 0:
        total_companions += 5
    if day_num % 3 == 0:
        my_coins -= (3 * total_companions)
        if day_num % 5 == 0:
            my_coins -= (2 * total_companions)
    if day_num % 5 == 0:
        my_coins += (20 * total_companions)
    my_coins -= (total_companions * 2)
average_companion_coins = int(my_coins / total_companions)
print(f"{total_companions} companions received {average_companion_coins} coins each.")
