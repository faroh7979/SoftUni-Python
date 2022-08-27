yearly_charge = int(input())

snickers = yearly_charge - yearly_charge * 0.4
equipment = snickers - snickers * 0.2
ball = 0.25 * equipment
accesories = 0.2 * ball

total_expense = snickers + equipment + ball + accesories + yearly_charge
total_expensef = "{:.2f}".format(total_expense)
print(total_expensef)
