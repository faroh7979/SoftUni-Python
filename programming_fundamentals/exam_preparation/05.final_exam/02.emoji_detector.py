import re

line_text = input()
word_list = []
cool_treshold = 1
word_symbol_list = []

text_reg = r'(::|\*\*)([A-Z]{1}[a-z]{2,})\1|(\d{1})'
for match in re.findall(text_reg, line_text):
    if match[2]:
        cool_treshold *= int(match[2])
    if match[1]:
        word_list.append(match[1])
        word_symbol_list.append(match[0] + match[1] + match[0])

print(f'Cool threshold: {cool_treshold}')
print(f'{len(word_list)} emojis found in the text. The cool ones are:')
for index, word in enumerate(word_list):
    current_ascii_value = 0
    for letter in word:
        current_ascii_value += ord(letter)
    if current_ascii_value > cool_treshold:
        print(word_symbol_list[index])
