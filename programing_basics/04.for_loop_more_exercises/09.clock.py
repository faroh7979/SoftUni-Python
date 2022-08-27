minutes_per_day = 24 * 60
hh = 0
mm = 0
for period in range(minutes_per_day):
    print(f"{hh} : {mm}")
    mm += 1
    if mm == 60:
        mm = 0
        hh += 1
