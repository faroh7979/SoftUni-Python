rage_quit_input = input()
temporary_string = ''
final_raged_string = ''
two_digit_multiplier = False

for index, value in enumerate(rage_quit_input):
    if two_digit_multiplier:
        two_digit_multiplier = False
        continue
    if not value.isdigit():
        temporary_string += value.upper()
    else:
        if index < len(rage_quit_input) - 1:
            if rage_quit_input[index + 1].isdigit():
                multiplier = int(value + rage_quit_input[index + 1])
                two_digit_multiplier = True
            else:
                multiplier = int(value)
        else:
            multiplier = int(value)
        final_raged_string += temporary_string * multiplier
        temporary_string = ''
unique_symbols = len(set(final_raged_string))
print(f'Unique symbols used: {unique_symbols}')
print(final_raged_string)
