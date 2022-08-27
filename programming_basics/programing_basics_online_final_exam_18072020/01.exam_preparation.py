strawberry_price = float(input())
raspberry_price = strawberry_price * 0.5
orange_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2
raspberry_price = strawberry_price * 0.5
banana_quantity = float(input())
orange_quantity = float(input())
raspberry_quantity = float(input())
strawberry_quantity = float(input())
total_expense = strawberry_price * strawberry_quantity + orange_price * orange_quantity +\
                banana_price * banana_quantity + raspberry_price * raspberry_quantity
print(f'{total_expense:.2f}')
