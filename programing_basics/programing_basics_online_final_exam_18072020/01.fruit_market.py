strawberry_price_leva = float(input())
banana_quantity_kg = float(input())
orange_quantity_kg = float(input())
raspberry_quantitty_kg = float(input())
strawberry_quantity_kg = float(input())

raspbery_price_leva = strawberry_price_leva * 0.5
orange_price_leva = raspbery_price_leva * 0.6
banana_price_leva = raspbery_price_leva * 0.2

total_expense = strawberry_quantity_kg * strawberry_price_leva +\
                banana_quantity_kg * banana_price_leva +\
                orange_quantity_kg * orange_price_leva +\
                raspberry_quantitty_kg * raspbery_price_leva

total_expensef = "{:.2f}".format(total_expense)

print(total_expensef)

