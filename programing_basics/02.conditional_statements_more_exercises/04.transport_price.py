n_total_kilometers = int(input())
period_of_day = input()

taxi_price = 0.70
bus_price = 0.09 * n_total_kilometers
train_price = 0.06 * n_total_kilometers

if period_of_day == "day":
    taxi_price += 0.79 * n_total_kilometers
else:
    taxi_price += 0.9 * n_total_kilometers

if n_total_kilometers < 20:
    print(f"{taxi_price:.2f}")
elif n_total_kilometers < 100:
    print(f"{bus_price:.2f}")
else:
    print(f"{train_price:.2f}")
