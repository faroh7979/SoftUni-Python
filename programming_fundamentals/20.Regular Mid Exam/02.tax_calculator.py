main_vehicle = input()
main_vehicle_list = main_vehicle.split('>>')
current_tax = 0
total_tax = 0

for vehicle in main_vehicle_list:
    work_vehicle = vehicle.split()
    type_vehicle = work_vehicle[0]
    years_vehicle = int(work_vehicle[1])
    kilometers_vehicle = int(work_vehicle[2])
    if type_vehicle == 'family' or type_vehicle == 'heavyDuty' or type_vehicle == 'sports':
        if type_vehicle == "family":
            increase = (kilometers_vehicle // 3000) * 12
            current_tax = 50 + increase - years_vehicle * 5
        elif type_vehicle == "heavyDuty":
            increase = (kilometers_vehicle // 9000) * 14
            current_tax = 80 + increase - years_vehicle * 8
        elif type_vehicle == "sports":
            increase = (kilometers_vehicle // 2000) * 18
            current_tax = 100 + increase - years_vehicle * 9
        total_tax += current_tax
        print(f"A {type_vehicle} car will pay {current_tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")
print(f"The National Revenue Agency will collect {total_tax:.2f} euros in taxes.")
