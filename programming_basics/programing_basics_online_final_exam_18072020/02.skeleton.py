target_time_minutes = int(input())
target_time_seconds = int(input())
lenght_meters = float(input())
seconds_for_100_meters = float(input())

won_time = lenght_meters / 120 * 2.5
needed_seconds = (lenght_meters / 100 * seconds_for_100_meters) - won_time
calculated_target_time_seconds = target_time_minutes * 60 + target_time_seconds

difference = calculated_target_time_seconds -needed_seconds
absdiff = abs(difference)

if difference >= 0:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {needed_seconds:.3f}.")
else:
    print(f"No, Marin failed! He was {absdiff:.3f} second slower.")
