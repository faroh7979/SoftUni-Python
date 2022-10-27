line = input()
total_price_no_tax = 0
total_price_tax = 0
total_discounted_price = 0
while line != 'special' and line != 'regular':
    current_price = float(line)
    if current_price < 0:
        print('Invalid price!')
        line = input()
        continue
    total_price_no_tax += current_price
    line = input()
total_price_tax = total_price_no_tax * 1.2
taxes = total_price_no_tax * 0.2
if line == 'special':
    total_discounted_price = total_price_tax * 0.9
else:
    total_discounted_price = total_price_tax
if total_discounted_price == 0:
    print('Invalid order!')
else:
    print(f"Congratulations you've just bought a new computer! "
          f"\nPrice without taxes: {total_price_no_tax:.2f}$ "
          f"\nTaxes: {taxes:.2f}$ "
          f"\n----------- "
          f"\nTotal price: {total_discounted_price:.2f}$")
