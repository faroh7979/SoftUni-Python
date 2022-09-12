command = input().split()
bakery = {}

for element in range(0, len(command), 2):
    key = command[element]
    value = command[element + 1]
    bakery[key] = int(value)

print(bakery)