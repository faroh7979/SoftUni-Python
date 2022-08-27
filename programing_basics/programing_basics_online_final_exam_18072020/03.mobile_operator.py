contract_length = input()
contract_type = input()
extra_internet = input()
payment_months = int(input())
monthly_tax = 0

if contract_length == "one":
    if contract_type == "Small":
        monthly_tax = 9.98
    elif contract_type == "Middle":
        monthly_tax = 18.99
    elif contract_type == "Large":
        monthly_tax = 25.98
    elif contract_type == "ExtraLarge":
        monthly_tax = 35.99
elif contract_length == "two":
    if contract_type == "Small":
        monthly_tax = 8.58
    elif contract_type == "Middle":
        monthly_tax = 17.09
    elif contract_type == "Large":
        monthly_tax = 23.59
    elif contract_type == "ExtraLarge":
        monthly_tax = 31.79

if extra_internet == "yes":
    if monthly_tax <= 10:
        monthly_tax += 5.50
    elif monthly_tax <= 30:
        monthly_tax += 4.35
    elif monthly_tax > 30:
        monthly_tax += 3.85
if contract_length == "two":
    monthly_tax *= 0.9625
total_price = monthly_tax * payment_months
print(f"{total_price:.2f} lv.")
