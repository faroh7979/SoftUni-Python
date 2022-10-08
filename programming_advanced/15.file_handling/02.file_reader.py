file_path = './numbers.txt'
file_link = open(file_path, 'r')
result = 0

for line in file_link:
    result += int(line.strip())

print(result)
