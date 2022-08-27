from math import ceil
from math import floor

tennis_racket_price = float(input())
tennis_racket_count = int(input())
sneakers_count = int(input())
sneakers_price = tennis_racket_price / 6

total_racket_and_sneakers_price = tennis_racket_price * tennis_racket_count + sneakers_price * sneakers_count
other_equipment = total_racket_and_sneakers_price * 0.2

total_equipment_price = total_racket_and_sneakers_price + other_equipment

sponsor_expence = ceil(total_equipment_price * 7 / 8)
djoko_expence = floor(total_equipment_price / 8)

print(f"Price to be paid by Djokovic {djoko_expence}")
print(f"Price to be paid by sponsors {sponsor_expence}")
