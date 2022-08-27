men_all = int(input())
women_all = int(input())
table_all = int(input())
taken_tables = 0
no_table = False
for man in range(1, men_all + 1):
    if no_table:
        break
    for woman in range(1, women_all + 1):
        taken_tables += 1
        if taken_tables <= table_all:
            print(f'({man} <-> {woman})', end=' ')
        else:
            no_table = True
        if no_table:
            break
