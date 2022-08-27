capacity = int(input())
total_spectators = int(input())
a_spectators = 0
b_spectators = 0
c_spectators = 0
d_spectators = 0

for fans in range(total_spectators):
    sector = input()
    if sector == 'A':
        a_spectators += 1
    elif sector == 'B':
        b_spectators += 1
    elif sector == 'V':
        c_spectators += 1
    elif sector == 'G':
        d_spectators += 1
a_percentage = a_spectators / total_spectators * 100
b_percentage = b_spectators / total_spectators * 100
c_percentage = c_spectators / total_spectators * 100
d_percentage = d_spectators / total_spectators * 100
fans_to_capacity = total_spectators / capacity * 100

print(f'{a_percentage:.2f}%')
print(f'{b_percentage:.2f}%')
print(f'{c_percentage:.2f}%')
print(f'{d_percentage:.2f}%')
print(f'{fans_to_capacity:.2f}%')
