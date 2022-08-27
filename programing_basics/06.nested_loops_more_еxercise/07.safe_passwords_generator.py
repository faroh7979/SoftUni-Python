splitter = "|"
template = 'ABxyBA'
a = int(input())
b = int(input())
max_passwords = int(input())
A = 35
B = 64
printed_pass = 0
stop = False
for x in range(1, a + 1):
    if stop:
        break
    for y in range(1, b + 1):
        chr_A = chr(A)
        chr_B = chr(B)
        print(f'{chr_A}{chr_B}{x}{y}{chr_B}{chr_A}', end=splitter)
        printed_pass += 1
        A += 1
        B += 1
        if A > 55:
            A = 35
        if B > 96:
            B = 64
        if printed_pass == max_passwords:
            stop = True
            break
