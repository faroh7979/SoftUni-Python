current_year = int(input())
length = len(str(current_year))
set_year = set()
founded = False

for year in range(current_year + 1, 10 ** (length + 1)):
    for i in range(len(str(year))):
        set_year.add(str(year)[i])
    current_length = len(str(year))
    if current_length == len(set_year):
        print(year)
        founded = True
        break
    if founded:
        break
    set_year = set()
