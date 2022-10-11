from re import findall
line = input()
digit_pattern = r'\d+'

while line:
    matches = findall(digit_pattern, line)
    if matches:
        print(' '.join(matches), end=' ')
    line = input()
