incomes = input()
total_money = 0

while incomes != 'NoMoreMoney':
    incomes = float(incomes)
    if incomes < 0:
        print('Invalid operation!')
        break
    incomes = float(incomes)
    print(f'Increase: {incomes:.2f}')
    total_money += incomes
    incomes = input()
print(f'Total: {total_money:.2f}')
