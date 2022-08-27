hour = int(input())
minute = int(input())

total_passed_minutes = hour * 60 + minute
current_passed_minutes = total_passed_minutes + 15

current_hour = current_passed_minutes // 60
current_minute = current_passed_minutes % 60

total_daily_minutes = 24 * 60
seconds_to_next_day = total_daily_minutes - total_passed_minutes
if total_daily_minutes - total_passed_minutes > 15:
    if current_minute < 10:
        print(f"{current_hour}:0{current_minute}")
    else:
        print(f"{current_hour}:{current_minute}")
elif 15 - seconds_to_next_day < 10:
    print(f"0:0{15 - seconds_to_next_day}")
else:
    print(f"0:{15 - seconds_to_next_day}")
