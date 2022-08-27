total_months = int(input())
water_bill = total_months * 20
internet_bill = total_months * 15
electricity_bill = 0

for period in range(total_months):
    electricity = float(input())
    electricity_bill += electricity
other_bills = (water_bill + internet_bill + electricity_bill) * 0.2 + (water_bill + internet_bill + electricity_bill)
total_bills = water_bill + internet_bill + electricity_bill + other_bills
average_bill = total_bills / total_months

print(f'Electricity: {electricity_bill:.2f} lv')
print(f'Water: {water_bill:.2f} lv')
print(f'Internet: {internet_bill:.2f} lv')
print(f'Other: {other_bills:.2f} lv')
print(f'Average: {average_bill:.2f} lv')
