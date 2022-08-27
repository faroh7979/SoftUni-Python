from math import floor

world_record_seconds = float(input())
distance_meters = float(input())
time_for_meter_seconds = float(input())

penalty_time = floor(distance_meters / 15) * 12.5
general_time = time_for_meter_seconds * distance_meters
total_time = general_time + penalty_time

difference = total_time - world_record_seconds


if difference < 0:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
