products = {}
total_products = 0
total_quantity = 0

while True:
    product_bar = input()
    if product_bar == 'statistics':
        break
    current_product = product_bar.split(': ')
    product = current_product[0]
    value = current_product[1]
    if product not in products:
        products[product] = int(value)
    else:
        products[product] += int(value)
print('Products in stock:')
for key, values in products.items():
    print(f'- {key}: {values}')
    total_products += 1
    total_quantity += values
print(f'Total Products: {total_products}')
print(f'Total Quantity: {total_quantity}')
