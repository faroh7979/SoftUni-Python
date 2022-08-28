lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
total_expense = 0

for lost_fights_num in range(1, lost_fights + 1):
    if lost_fights_num % 2 == 0:
        total_expense += helmet_price
    if lost_fights_num % 3 == 0:
        total_expense += sword_price
        if lost_fights_num % 2 == 0:
            total_expense += shield_price
    if lost_fights_num % 12 == 0:
        total_expense += armor_price
print(f"Gladiator expenses: {total_expense:.2f} aureus")
