total_time = int(input())
scenes_count = int(input())
scenes_lenght = int(input())

preparing = 0.15

total_needed_time = (scenes_count * scenes_lenght) + (total_time * preparing)

rested_time = round(total_time - total_needed_time,0)
rested_timef = "{:.0f}".format(rested_time)

more_time = round(total_needed_time - total_time,0)
more_timef = "{:.0f}".format(more_time)

if rested_time >= 0:
    print(f"You managed to finish the movie on time! You have {rested_timef} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {more_timef} minutes.")
