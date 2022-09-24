from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
car_on_crossroad = deque()
there_is_crash = False
total_safe_passed_cars = 0

while True:

    if there_is_crash:
        break

    command = input()

    if command == 'END':
        break

    elif command == 'green':
        if car_on_crossroad:
            green_zone = green_light_duration
            window_zone = free_window_duration

            for _ in range(len(car_on_crossroad)):
                if green_zone == 0:
                    continue

                current_car = car_on_crossroad.popleft()
                needed_seconds_to_pass = len(current_car)

                if green_zone >= needed_seconds_to_pass:
                    green_zone -= needed_seconds_to_pass
                    total_safe_passed_cars += 1

                else:
                    if_crash_hit_letter = green_zone + window_zone
                    needed_seconds_to_pass -= green_zone
                    green_zone = 0

                    if needed_seconds_to_pass <= window_zone:
                        total_safe_passed_cars += 1

                    else:
                        there_is_crash = True
                        print("A crash happened!")
                        print(f"{current_car} was hit at {current_car[if_crash_hit_letter]}.")
                        break

    else:
        car_on_crossroad.append(command)

if not there_is_crash:
    print("Everyone is safe.")
    print(f"{total_safe_passed_cars} total cars passed the crossroads.")
