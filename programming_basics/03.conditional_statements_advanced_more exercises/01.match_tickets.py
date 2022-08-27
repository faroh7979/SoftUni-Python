budget = float(input())
hospitality = input()
total_fans = int(input())
vip_ticket = 499.99
regular_ticket = 249.99
transport_expense = 0
ticket_type = regular_ticket

if 1 <= total_fans <= 4:
    transport_expense = budget * 0.75
elif 5 <= total_fans <= 9:
    transport_expense = budget * 0.6
elif 10 <= total_fans <= 24:
    transport_expense = budget * 0.5
elif 25 <= total_fans <= 49:
    transport_expense = budget * 0.4
elif total_fans >= 50:
    transport_expense = budget * 0.25
if hospitality == "VIP":
    ticket_type = vip_ticket

total_expense = total_fans * ticket_type + transport_expense
difference = abs(total_expense - budget)

if total_expense <= budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
