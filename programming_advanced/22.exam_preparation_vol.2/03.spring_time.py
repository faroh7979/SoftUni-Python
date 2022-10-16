def start_spring(**kwargs):
    flower_dict = {}
    final_string = ''

    for item, collection in kwargs.items():
        if collection not in flower_dict:
            flower_dict[collection] = [item]
        else:
            flower_dict[collection].append(item)

    flower_dict = dict(sorted(flower_dict.items(), key=lambda x: (- len(x[1]), x[0])))

    for key, value in flower_dict.items():
        final_string += f'{key}:\n'
        for sub_value in sorted(value):
            final_string += f'-{sub_value}\n'

    return final_string


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))

