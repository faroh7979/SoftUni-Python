magic_num = int(input())
x1 = ''
x2 = ''
x3 = ''
total = ''
total_solutions = 0

for x1 in range(0, magic_num + 1):
    for x2 in range(0, magic_num + 1):
        for x3 in range(0, magic_num + 1):
            total = x1 + x2 + x3
            if total == magic_num:
                total_solutions += 1
print(total_solutions)
