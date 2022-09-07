message = input().split()
new_words = []
string = ''

for index in range(len(message)):
    current_word = message[index]
    current_word_list = [letter for letter in current_word]
    ascii_list = [symbol_ for symbol_ in current_word if symbol_.isdigit()]
    letter_list = [symbol_ for symbol_ in current_word if not symbol_.isdigit()]
    first_char = chr(int(''.join(ascii_list)))
    first_char_length = ascii_list.__len__()
    first_char_list = [digit_ for digit_ in first_char]
    letter_list[-1], letter_list[0] = letter_list[0],  letter_list[-1]
    new_word = first_char_list + letter_list
    new_words.append(new_word)
    ascii_list = []
for current_list in new_words:
    string += f"{''.join(current_list)} "
print(string)
