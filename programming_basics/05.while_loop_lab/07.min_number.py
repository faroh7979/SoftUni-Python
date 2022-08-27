from sys import maxsize

line = input()
min_num = maxsize

while line != 'Stop':
    value = int(line)
    if value < min_num:
        min_num = value
    line = input()
print(min_num)
