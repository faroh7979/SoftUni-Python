waiting_people = int(input())
current_state = input()
wagon_state_list = list(map(int, current_state.split()))
total_wagons = len(wagon_state_list)
total_spaces = 4 * total_wagons - sum(wagon_state_list)
rested_people_on_que = waiting_people - total_spaces
final_wagon_state = []

for wagon_index in range(total_wagons):
    available_places = 4 - wagon_state_list[wagon_index]
    if available_places <= waiting_people:
        waiting_people -= available_places
        final_wagon_state.append(available_places + wagon_state_list[wagon_index])
    else:
        final_wagon_state.append(waiting_people + wagon_state_list[wagon_index])
        waiting_people = 0
if rested_people_on_que < 0:
    print("The lift has empty spots!")
    print(*final_wagon_state)
elif rested_people_on_que > 0:
    print(f"There isn't enough space! {rested_people_on_que} people in a queue!")
    print(*final_wagon_state)
else:
    print(*final_wagon_state)
