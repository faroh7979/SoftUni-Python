count_guests = int(input())
price_per_person_income = float(input())
budget_desi = float(input())

cake = budget_desi * 0.1

if count_guests >= 10 and count_guests <= 15:
    discount = 0.15
elif count_guests > 15 and count_guests <= 20:
    discount = 0.2
elif count_guests > 20:
    discount = 0.25
else:
    discount = 0
total_expence = count_guests * (price_per_person_income - price_per_person_income * discount) + cake

money_difference = budget_desi - total_expence

if money_difference >= 0:
    print(f"It is party time! {money_difference:.2f} leva left.")
else:
    print(f"No party! {abs(money_difference):.2f} leva needed.")
