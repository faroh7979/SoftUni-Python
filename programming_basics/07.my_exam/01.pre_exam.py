price_package_paper = 5.80
price_plat = 7.20
price_glue = 1.20
count_paper = int(input())
count_plat = int(input())
liters_glue = float(input())
percent_discount = int(input())

total_sum = price_package_paper * count_paper + price_plat * count_plat + price_glue * liters_glue
discount = total_sum * percent_discount / 100
total_expense = total_sum - discount
print(f'{total_expense:.3f}')
