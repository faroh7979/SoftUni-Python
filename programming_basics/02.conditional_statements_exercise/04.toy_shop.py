tour_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
mignon_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
mignon_price = 8.2
truck_price = 2

total_price = puzzles_count * puzzle_price +\
            dolls_count * doll_price +\
            bears_count * bear_price +\
            mignon_count * mignon_price +\
            trucks_count * truck_price

toys_num = puzzles_count + dolls_count + bears_count + mignon_count + trucks_count

if toys_num >= 50:
    total_price *= 0.75

total_price *= 0.9
difference = abs(total_price - tour_price)
if total_price >= tour_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
