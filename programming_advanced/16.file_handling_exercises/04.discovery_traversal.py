from os import listdir, path


def files_output(extensions_dict, directory_path, is_on_the_next_level=False):
    for file_name in listdir(directory_path):
        directory_path = path.join(directory_path, file_name)

        if path.isfile:

            extension = ''
            for symbol in file_name[::-1]:
                extension += symbol
                if symbol == '.':
                    extension = extension[::-1]
                    break

            if extension not in extensions_dict:
                extensions_dict[extension] = [file_name]

            else:
                extensions_dict[extension].append(file_name)

        elif path.isdir(directory_path) and not is_on_the_next_level:
            files_output(extensions_dict, directory_path, is_on_the_next_level=True)


directory_path_input = input()
dict_extension = {}
result_for_file = ''

files_output(dict_extension, directory_path_input)

dict_extension = dict(sorted(dict_extension.items(), key=lambda x: (x[0], x[1])))

for key, value in dict_extension.items():
    result_for_file += f'{key}\n'
    for element in value:
        result_for_file += f'- - - {element}\n'

with open(f'{directory_path_input}/report.txt', 'w') as statistics:
    statistics.write(result_for_file)
