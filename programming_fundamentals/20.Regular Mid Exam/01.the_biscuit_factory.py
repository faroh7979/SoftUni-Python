biscuits_day_worker = int(input())
count_of_workers = int(input())
enemy_factory_biscuits = int(input())
my_total_biscuits = 0
total_days = 30
daily_producing = biscuits_day_worker * count_of_workers
third_day_producing = int(daily_producing * 0.75)

for day in range(1, total_days +1):
    if day % 3 == 0:
        my_total_biscuits += third_day_producing
    else:
        my_total_biscuits += daily_producing
if my_total_biscuits > enemy_factory_biscuits:
    difference = my_total_biscuits - enemy_factory_biscuits
    percentage = (difference / enemy_factory_biscuits) * 100
    print(f'You have produced {my_total_biscuits} biscuits for the past month.')
    print(f'You produce {percentage:.2f} percent more biscuits.')
else:
    difference = enemy_factory_biscuits - my_total_biscuits
    percentage = (difference / enemy_factory_biscuits) * 100
    print(f'You have produced {my_total_biscuits} biscuits for the past month.')
    print(f'You produce {percentage:.2f} percent less biscuits.')
