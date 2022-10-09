line_sep = '\n'
all_symbols_for_replacing = ["-", ",", ".", "!", "?"]
symbol_to_replace_others = '@'

file_path = './text.txt'
with open(file_path, 'r') as input_file:
    file_content = input_file.readlines()  # list with all rows as a separated element

final_list = []  # here will be only the even rows with the special symbols replaced
total_rows = len(file_content)
for row_num in range(total_rows):
    if row_num % 2 == 0:
        new_line = file_content[row_num].replace(line_sep, '')  # new string for manipulating and replacing
        for special_symbol in all_symbols_for_replacing:
            new_line = new_line.replace(special_symbol, symbol_to_replace_others)
        final_list.append(new_line)

for line in final_list:
    reversed_line = line.split()[::-1]
    print(" ".join(reversed_line))
