world_record_seconds = float(input())
distance_meters = float(input())
time_in_seconds_for_meter_climbing = float(input())

slowly_times = distance_meters // 50

penalty_time_in_sedonds = slowly_times * 30

regular_time = distance_meters * time_in_seconds_for_meter_climbing

total_time = regular_time + penalty_time_in_sedonds
total_timef = "{:.2f}".format(total_time)

time_difference = total_time - world_record_seconds
time_differencef = "{:.2f}".format(time_difference)

if time_difference < 0:
    print(f"Yes! The new record is {total_timef} seconds.")

else:
    print(f"No! He was {time_differencef} seconds slower.")
