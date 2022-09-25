command_line = input()
digit_symbols = ''
letter_symbols = ''
other_symbols = ''

for element in command_line:
    if element.isdigit():
        digit_symbols += element
    elif element.isalpha():
        letter_symbols += element
    else:
        other_symbols += element

print(digit_symbols)
print(letter_symbols)
print(other_symbols)
