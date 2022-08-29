def bill(product, quantity):
    result = None
    if product == 'coffee':
        result = 1.50 * quantity
    elif product == 'water':
        result = 1.00 * quantity
    elif product == 'coke':
        result = 1.40 * quantity
    elif product == 'snacks':
        result = 2.00 * quantity
    return f'{result:.2f}'


choice = input()
total = int(input())
print(bill(choice, total))
