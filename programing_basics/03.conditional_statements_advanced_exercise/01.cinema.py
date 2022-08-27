type_broadcasting = input()
rows = int(input())
columns = int(input())

price = 0
total_spectators = rows * columns

if type_broadcasting == "Premiere":
    price = 12
elif type_broadcasting == "Normal":
    price = 7.50
elif type_broadcasting == "Discount":
    price = 5

incomes = total_spectators * price
print(f"{incomes:.2f} leva")
