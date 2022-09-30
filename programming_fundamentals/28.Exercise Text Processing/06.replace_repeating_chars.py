command_line = input()
new_cleared_string = ''
new_index = 0
symbol = 0
for symbol in range(0, len(command_line)):
    if symbol != new_index:
        continue
    for repeated in range(1, len(command_line)):
        if symbol + repeated >= len(command_line):
            break
        if command_line[symbol] != command_line[symbol + repeated]:
            new_index = symbol + repeated
            new_cleared_string += command_line[symbol]
            break
new_cleared_string += command_line[symbol]
print(new_cleared_string)
