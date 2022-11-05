def dict_creation(target_towns):

    while True:
        command_line = input()

        if command_line == 'Sail':
            return target_towns

        command_split = command_line.split('||')
        town = command_split[0]
        population = int(command_split[1])
        gold = int(command_split[2])

        if town not in target_towns:
            target_towns[town] = {'population': population, 'gold': gold}

        else:
            target_towns[town]['population'] += population
            target_towns[town]['gold'] += gold


def attacking_mode(target_towns):
    while True:
        command_attack = input()

        if command_attack == 'End':
            return target_towns

        command_attack_split = command_attack.split('=>')
        current_command = command_attack_split[0]

        if current_command == 'Plunder':
            current_town = command_attack_split[1]
            current_people = int(command_attack_split[2])
            current_gold = int(command_attack_split[3])

            target_towns[current_town]['population'] -= current_people
            target_towns[current_town]['gold'] -= current_gold

            print(f"{current_town} plundered! {current_gold} gold stolen, {current_people} citizens killed.")

            if target_towns[current_town]['population'] <= 0 or target_towns[current_town]['gold'] <= 0:
                target_towns.pop(current_town)
                print(f"{current_town} has been wiped off the map!")

        elif current_command == 'Prosper':
            prosper_town = command_attack_split[1]
            prosper_gold = int(command_attack_split[2])

            if prosper_gold < 0:
                print('Gold added cannot be a negative number!')
                continue
            else:
                target_towns[prosper_town]['gold'] += prosper_gold
                prosper_total = target_towns[prosper_town]['gold']
                print(f"{prosper_gold} gold added to the city treasury. {prosper_town} now has {prosper_total} gold.")


def print_func(target_towns):
    remained_cities = len(target_towns)

    if remained_cities == 0:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")

    else:
        print(f"Ahoy, Captain! There are {remained_cities} wealthy settlements to go to:")
    for key in target_towns:
        print(f"{key} -> Population: {target_towns[key]['population']} citizens, Gold: {target_towns[key]['gold']} kg")


def final_func():
    target_towns = {}

    dict_creation(target_towns)
    attacking_mode(target_towns)
    print_func(target_towns)


final_func()
