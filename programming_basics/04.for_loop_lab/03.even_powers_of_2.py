power = int(input())
output = 1
print(output)
for num in range(2, power + 1, 2):
    output *= 4
    print(output)
