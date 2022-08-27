from math import ceil

series_name = input()
length_episode = int(input())
length_break = int(input())

lunch_time = length_break / 8
rest_time = length_break / 4

needed_time = lunch_time + rest_time + length_episode
difference = ceil(abs(length_break - needed_time))

if needed_time <= length_break:
    print(f"You have enough time to watch {series_name} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {difference} more minutes.")
