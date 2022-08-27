from math import ceil

total_guests = int(input())
entry_tax = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

total_umbrella = ceil(total_guests / 2)
total_sunbed = ceil(total_guests * 0.75)

total_entry_taxes = total_guests * entry_tax
total_umbrella_price = total_umbrella * umbrella_price
total_sunbed_price = total_sunbed * sunbed_price

total_expense = total_entry_taxes + total_umbrella_price + total_sunbed_price

print(f"{total_expense:.2f} lv.")
