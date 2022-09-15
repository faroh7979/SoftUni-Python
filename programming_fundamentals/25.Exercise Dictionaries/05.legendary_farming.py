legendary_dict = {'shards': 0, "fragments": 0, "motes": 0}
legendary_item_produced = False
legendary_item = ''

while not legendary_item_produced:
    resources = input()
    resources_list = resources.lower().split()
    for current_index in range(0, len(resources_list), 2):
        quantity = int(resources_list[current_index])
        material = resources_list[current_index + 1]
        if material not in legendary_dict:
            legendary_dict[material] = 0
        legendary_dict[material] += quantity
        if legendary_dict['shards'] >= 250:
            legendary_dict['shards'] -= 250
            legendary_item_produced = True
            legendary_item = "Shadowmourne"
            break
        elif legendary_dict['fragments'] >= 250:
            legendary_dict['fragments'] -= 250
            legendary_item_produced = True
            legendary_item = "Valanyr"
            break
        elif legendary_dict['motes'] >= 250:
            legendary_dict['motes'] -= 250
            legendary_item_produced = True
            legendary_item = "Dragonwrath"
            break
if legendary_item_produced:
    print(f'{legendary_item} obtained!')
    for legend_material, legend_quantity in legendary_dict.items():
        print(f'{legend_material}: {legend_quantity}')
