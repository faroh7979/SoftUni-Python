from collections import deque

total_station = int(input())
stations_deque = deque()
wining_station = False  # will be used to check if the qualifying station is founded

for _ in range(total_station):
    current_station_details = []

    current_station = list(map(int, input().split()))
    stations_deque.append(current_station)

for current_station_number in range(total_station):
    if wining_station:
        print(current_station_number - 1)
        wining_station = False  # to escape the last print if the qualifying station is not the last one
        break

    if current_station_number > 0:  # using for FIFO, after the first rotation
        current_station_info = stations_deque.popleft()
        stations_deque.append(current_station_info)

    total_fuel = 0
    total_distance = 0

    for current_element in stations_deque:
        wining_station = True # if somewhere on the track fuel is not enough it will be changed to False on line 38
        current_fuel = current_element[0]
        current_distance = current_element[1]

        total_fuel += current_fuel
        total_distance += current_distance

        if total_fuel >= total_distance:
            continue

        else:
            wining_station = False
            break

if wining_station:  # if the last one is the only one qualifying station, that is the reason for minus 1 in the print
    print(total_station - 1)
