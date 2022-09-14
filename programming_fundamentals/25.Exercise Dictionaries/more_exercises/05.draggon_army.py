total_dragons = int(input())
default_health = 250
default_damage = 45
default_armor = 10
dragon_dictionary = {}

for dragon in range(total_dragons):
    current_dragon = input()
    current_dragon_list = current_dragon.split()
    type_dragon = current_dragon_list[0]
    name_dragon = current_dragon_list[1]
    if current_dragon_list[2] == 'null':
        damage_dragon = default_damage
    else:
        damage_dragon = int(current_dragon_list[2])
    if current_dragon_list[3] == 'null':
        health_dragon = default_health
    else:
        health_dragon = int(current_dragon_list[3])
    if current_dragon_list[4] == 'null':
        armor_dragon = default_armor
    else:
        armor_dragon = int(current_dragon_list[4])
    if type_dragon not in dragon_dictionary:
        dragon_dictionary[type_dragon] = \
            {name_dragon: {'damage': damage_dragon, 'health': health_dragon, 'armor': armor_dragon}}
    else:
        if name_dragon != dragon_dictionary[type_dragon]:
            dragon_dictionary[type_dragon][name_dragon] = \
                {'damage': damage_dragon, 'health': health_dragon, 'armor': armor_dragon}
        else:
            dragon_dictionary[type_dragon] = \
                {name_dragon: {'damage': damage_dragon, 'health': health_dragon, 'armor': armor_dragon}}
for key_type in dragon_dictionary:
    total_damage = 0
    total_health = 0
    total_armor = 0
    count_dragons = 0
    printed_test = ''
    for key_name in sorted(dragon_dictionary[key_type]):
        printed_test += f'-{key_name} -> damage: {dragon_dictionary[key_type][key_name]["damage"]}, health: {dragon_dictionary[key_type][key_name]["health"]}, armor: {dragon_dictionary[key_type][key_name]["armor"]}\n'
        total_damage += dragon_dictionary[key_type][key_name]["damage"]
        total_health += dragon_dictionary[key_type][key_name]["health"]
        total_armor += dragon_dictionary[key_type][key_name]["armor"]
        count_dragons += 1
    average_damage = total_damage / count_dragons
    average_health = total_health / count_dragons
    average_armor = total_armor / count_dragons
    print(f'{key_type}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})')
    print("".join(printed_test), end='')
