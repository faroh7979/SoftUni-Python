seconds_per_day = 24 * 60 * 60
hh = 0
mm = 0
ss = 0

for period in range(seconds_per_day):
    print(f"{hh} : {mm} : {ss}")
    ss += 1
    if ss == 60:
        ss = 0
        mm += 1
    if mm == 60:
        mm = 0
        hh += 1
