file_input_path = './input.txt'
file_words_path = './words.txt'

word_list = []
with open(file_words_path, 'r') as file:
    searched_word_list = file.read().split()

with open(file_input_path, 'r')as file:
    for line in file:
        line = ''.join(line.split(','))
        line = ''.join(line.split('!'))
        line = ''.join(line.split('?'))
        line = ''.join(line.split('.'))
        word_list += (line[1:].split())
    word_list_lower = [word.lower() for word in word_list]

dictionary = {}
for searched_word in searched_word_list:
    matched_times = word_list_lower.count(searched_word.lower())
    dictionary[searched_word] = matched_times

dictionary = dict(sorted(dictionary.items(), key=lambda x: -x[1]))

final_file = ''
for key, value in dictionary.items():
    final_file += f'{key} - {value}\n'

new_file_path = './output.txt'

with open(new_file_path, 'w') as file:
    file.write(final_file)
