budget = int(input())
command = input()
expense = 0

while command != "End":
    expense += int(command)
    if expense > budget:
        print('You went in overdraft!')
        break
    command = input()
else:
    print('You bought everything needed.')
