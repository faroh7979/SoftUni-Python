minutes_walking_daily = int(input())
count_walking_daily = int(input())
calories_daily = int(input())

calories_burn_per_minute = 5

total_minutes_walking = minutes_walking_daily * count_walking_daily
total_burnt_calories = total_minutes_walking * calories_burn_per_minute

if calories_daily * 0.5 <= total_burnt_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burnt_calories}.")

else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burnt_calories}.")
