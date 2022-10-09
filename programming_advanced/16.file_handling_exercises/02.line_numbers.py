from string import punctuation
punctuation_list = punctuation

file_path = './text_task_two.txt'

with open(file_path, 'r') as file:
    text_list = file.readlines()

final_string = ''
for current_index in range(len(text_list)):
    current_line = text_list[current_index]
    total_punctuation_symbols = 0

    current_line_letters = 0
    for element in current_line:
        if element.isalpha():
            current_line_letters += 1

    # line + 1 because index starting from zero, and slice notation because of line separator at the end
    current_string = f'Line {current_index + 1}: {current_line[:-1]}'

    for symbol in punctuation_list:
        total_punctuation_symbols += current_line.count(symbol)

    final_string += f'{current_string} ({current_line_letters})({total_punctuation_symbols})\n'

new_file_path = './output.txt'
with open(new_file_path, 'w') as new_file:
    new_file.write(final_string)
