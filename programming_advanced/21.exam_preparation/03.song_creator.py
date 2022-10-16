def add_songs(*args):
    songs_dict = {}
    final_string = ''

    for element in args:
        key = element[0]
        value = element[1]

        if key not in songs_dict:
            songs_dict[key] = []
        if value:
            for sub_element in value:
                songs_dict[key].append(sub_element)

    for key, value in songs_dict.items():
        final_string += f'- {key}\n'
        if value:
            for value_element in value:
                final_string += f'{value_element}\n'

    return final_string


print(add_songs(
    ("Beat It", []),
    ("Beat It",
     ["Just beat it (beat it), beat it (beat it)",
      "No one wants to be defeated"]),
    ("Beat It", []),
    ("Beat It",
     ["Showin' how funky and strong is your fight",
      "It doesn't matter who's wrong or right"]),
))


