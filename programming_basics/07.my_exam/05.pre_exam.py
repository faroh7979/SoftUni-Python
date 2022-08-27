sea_total_trips = int(input())
mountain_total_trips = int(input())
sea_rested_trips = sea_total_trips
mountain_rested_trips = mountain_total_trips
total_profit = 0
everything_is_sold = True

while sea_rested_trips > 0 or mountain_rested_trips > 0:
    command_line = input()
    if command_line == 'Stop':
        everything_is_sold = False
        break
    elif command_line == 'sea':
        if sea_rested_trips > 0:
            sea_rested_trips -= 1
            total_profit += 680
    elif command_line == 'mountain':
        if mountain_rested_trips > 0:
            mountain_rested_trips -= 1
            total_profit += 499

if everything_is_sold:
    print('Good job! Everything is sold.')
print(f'Profit: {total_profit} leva.')
