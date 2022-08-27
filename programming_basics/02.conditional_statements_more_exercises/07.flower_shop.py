from math import ceil
from math import floor

total_magnolias = int(input())
total_hyacinths = int(input())
total_roses = int(input())
total_cacti = int(input())
present_price = float(input())

price_magnolias = 3.25
price_hyacinths = 4
price_roses = 3.50
price_cacti = 8

nra = 5/100

total_profit = total_magnolias * price_magnolias +\
            total_cacti * price_cacti +\
            total_roses * price_roses +\
            total_hyacinths * price_hyacinths
total_profit *= 0.95

difference = abs(total_profit - present_price)

if total_profit >= present_price:
    print(f"She is left with {floor(difference)} leva.")
else:
    print(f"She will have to borrow {ceil(difference)} leva.")
