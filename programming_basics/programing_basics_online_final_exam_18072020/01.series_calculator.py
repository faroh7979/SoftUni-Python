from math import floor

show_name = input()
seasons_count = int(input())
episodes_count = int(input())
episode_lenght_no_adv = float(input())

advertisement = episode_lenght_no_adv * 0.2
special_episode_addding = 10

total_time = (seasons_count * episodes_count * episode_lenght_no_adv) +\
             (seasons_count * special_episode_addding) +\
             (seasons_count * episodes_count * advertisement)

total_timef = floor(total_time)

print(f"Total time needed to watch the {show_name} series is {total_timef} minutes.")

