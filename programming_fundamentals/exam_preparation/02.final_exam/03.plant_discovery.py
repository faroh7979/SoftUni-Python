total_plants = int(input())
plant_dictionary = {}

for plant in range(total_plants):
    plant_command = input()
    plant_split = plant_command.split('<->')
    current_plant = plant_split[0]
    current_rarity = int(plant_split[1])
    plant_dictionary[current_plant] = {'rarity': current_rarity, 'rating': 0, 'rating_counter': 0}
# print(plant_dictionary)
while True:
    while_command = input()
    if while_command == 'Exhibition':
        break
    while_command_split = while_command.split(': ')
    if while_command_split[0] == 'Rate':
        plant_again, rating_again = while_command_split[1].split(' - ')
        if plant_again not in plant_dictionary:
            print('error')
            continue
        plant_dictionary[plant_again]['rating'] += int(rating_again)
        plant_dictionary[plant_again]['rating_counter'] += 1
    elif while_command_split[0] == 'Update':
        plant_again, new_rarity = while_command_split[1].split(' - ')
        if plant_again not in plant_dictionary:
            print('error')
            continue
        plant_dictionary[plant_again]['rarity'] = int(new_rarity)
    elif while_command_split[0] == 'Reset':
        plant_again = while_command_split[1]
        if plant_again not in plant_dictionary:
            print('error')
            continue
        plant_dictionary[plant_again]['rating'] = 0
        plant_dictionary[plant_again]['rating_counter'] = 0
print('Plants for the exhibition:')
for key in plant_dictionary:
    if plant_dictionary[key]['rating_counter'] > 0:
        average_rating = plant_dictionary[key]['rating'] / plant_dictionary[key]['rating_counter']
    else:
        average_rating = 0
    print(f'- {key}; Rarity: {plant_dictionary[key]["rarity"]}; Rating: {average_rating:.2f}')
