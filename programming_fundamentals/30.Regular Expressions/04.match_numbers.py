import re

numbers_command = input()
numbers_pattern = r'((^|(?<=\s))\-?([0]|[1-9][0-9]*)(\.\d+)*($|(?=\s)))'

real_numbers = re.findall(numbers_pattern, numbers_command)
for element in real_numbers:
    print(element[0], end=' ')
