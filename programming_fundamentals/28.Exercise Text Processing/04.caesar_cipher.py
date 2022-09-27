command_line = input()
new_string = ''

for symbol in command_line:
    current_symbol = ord(symbol) + 3
    new_string += chr(current_symbol)

print(new_string)
