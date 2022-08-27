round_of_championship = input()
ticket_level = input()
total_tickets = int(input())
selfie_with_the_trophy = input()
single_ticket_price = 0
trophy_ticket = 0

if round_of_championship == "Quarter final":
    if ticket_level == "Standard":
        single_ticket_price = 55.50
    elif ticket_level == "Premium":
        single_ticket_price = 105.20
    elif ticket_level == "VIP":
        single_ticket_price = 118.90
elif round_of_championship == "Semi final":
    if ticket_level == "Standard":
        single_ticket_price = 75.88
    elif ticket_level == "Premium":
        single_ticket_price = 125.22
    elif ticket_level == "VIP":
        single_ticket_price = 300.40
elif round_of_championship == "Final":
    if ticket_level == "Standard":
        single_ticket_price = 110.10
    elif ticket_level == "Premium":
        single_ticket_price = 160.66
    elif ticket_level == "VIP":
        single_ticket_price = 400.00
only_ticket_price = single_ticket_price * total_tickets

if selfie_with_the_trophy == "Y" and only_ticket_price <= 4000:
    trophy_ticket = 40

if 2500 < only_ticket_price <= 4000:
    only_ticket_price *= 0.9
elif only_ticket_price > 4000:
    only_ticket_price *= 0.75

total_price = only_ticket_price + trophy_ticket * total_tickets
print(f"{total_price:.2f}")
