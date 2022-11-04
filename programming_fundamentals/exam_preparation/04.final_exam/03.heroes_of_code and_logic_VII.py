def create_heroes_dict(total_heroes, heroes_dict):

    for hero in range(total_heroes):
        command = input().split()
        hero_name = command[0]
        hero_hp = int(command[1])
        hero_mp = int(command[2])
        heroes_dict[hero_name] = {'hero_hp': hero_hp, 'hero_mp': hero_mp}

    return heroes_dict


def battle_field(heroes_dict):
    while True:
        battle_command_no_split = input()
        if battle_command_no_split == 'End':
            return heroes_dict

        battle_command = battle_command_no_split.split(' - ')

        command_type = battle_command[0]
        battle_hero_name = battle_command[1]

        if command_type == 'CastSpell':
            mp_needed = int(battle_command[2])
            spell_name = battle_command[3]
            if heroes_dict[battle_hero_name]['hero_mp'] >= mp_needed:
                heroes_dict[battle_hero_name]['hero_mp'] -= mp_needed
                print(f"{battle_hero_name} has successfully cast {spell_name} and now has {heroes_dict[battle_hero_name]['hero_mp']} MP!")
            else:
                print(f"{battle_hero_name} does not have enough MP to cast {spell_name}!")

        elif command_type == 'TakeDamage':
            damage = int(battle_command[2])
            attacker = battle_command[3]
            if heroes_dict[battle_hero_name]['hero_hp'] - damage > 0:
                heroes_dict[battle_hero_name]['hero_hp'] -= damage
                print(f'{battle_hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[battle_hero_name]["hero_hp"]} HP left!')
            else:
                heroes_dict.pop(battle_hero_name)
                print(f'{battle_hero_name} has been killed by {attacker}!')

        elif command_type == 'Recharge':
            amount = int(battle_command[2])
            if heroes_dict[battle_hero_name]['hero_mp'] + amount > 200:
                recharge_point = 200 - heroes_dict[battle_hero_name]['hero_mp']
                heroes_dict[battle_hero_name]['hero_mp'] = 200
            else:
                recharge_point = amount
                heroes_dict[battle_hero_name]['hero_mp'] += recharge_point
            print(f"{battle_hero_name} recharged for {recharge_point} MP!")

        elif command_type == 'Heal':
            heal_amount = int(battle_command[2])
            if heroes_dict[battle_hero_name]['hero_hp'] + heal_amount > 100:
                recharge_hp_point = 100 - heroes_dict[battle_hero_name]['hero_hp']
                heroes_dict[battle_hero_name]['hero_hp'] = 100
            else:
                recharge_hp_point = heal_amount
                heroes_dict[battle_hero_name]['hero_hp'] += recharge_hp_point
            print(f"{battle_hero_name} healed for {recharge_hp_point} HP!")


def print_dictionary(heroes_dict):
    for key in heroes_dict:
        print(f'{key}')
        print(f'  HP: {heroes_dict[key]["hero_hp"]}')
        print(f'  MP: {heroes_dict[key]["hero_mp"]}')

    return heroes_dict


def final_func(number):
    heroes_dict = {}

    create_heroes_dict(number, heroes_dict)
    battle_field(heroes_dict)
    print_dictionary(heroes_dict)


amount_of_heroes = int(input())
final_func(amount_of_heroes)
