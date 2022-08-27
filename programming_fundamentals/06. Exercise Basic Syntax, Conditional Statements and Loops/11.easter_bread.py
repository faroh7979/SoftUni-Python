import sys
maxsize = sys.maxsize
budget = float(input())
flour_kg_price = float(input())
pack_of_eggs = flour_kg_price * 0.75
liter_milk = flour_kg_price * 1.25
quarter_milk_price = liter_milk / 4
loaf_price = flour_kg_price + pack_of_eggs + quarter_milk_price
total_loaves = 0
total_collected_eggs = 0
total_spend = 0

for loaf_num in range(1, maxsize):
    total_spend += loaf_price
    if budget <= total_spend:
        total_spend -= loaf_price
        break
    total_loaves += 1
    total_collected_eggs += 3
    if loaf_num % 3 == 0:
        total_collected_eggs -= (total_loaves - 2)
money_left = budget - total_spend
print(f'You made {total_loaves:.0f} loaves of Easter bread! Now you have {total_collected_eggs:.0f} \
eggs and {money_left:.2f}BGN left.')
