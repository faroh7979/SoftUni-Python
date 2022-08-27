days_off = int(input())

work_day_playing_minutes = 63
day_off_playing_minutes = 127

needed_sleep_minutes = 30000
works_day_count = 365 - days_off

playing_minutes = days_off * day_off_playing_minutes + work_day_playing_minutes * works_day_count

difference = abs(playing_minutes - needed_sleep_minutes)
difference_h = difference // 60
difference_m = difference % 60

if playing_minutes >= needed_sleep_minutes:
    print("Tom will run away")
    print(f"{difference_h} hours and {difference_m} minutes more for play")
else:
    print("Tom sleeps well")
    print(f"{difference_h} hours and {difference_m} minutes less for play")
