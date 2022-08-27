city = input()
s_volume = float(input())

commission_percentage = 0

valid_commission = s_volume > 0
valid_cities = city == "Sofia" or city == "Varna" or city == "Plovdiv"

if city == "Sofia":
    if 0 <= s_volume <= 500:
        commission_percentage = 0.05
    elif 500 < s_volume <= 1000:
        commission_percentage = 0.07
    elif 1000 < s_volume <= 10000:
        commission_percentage = 0.08
    elif s_volume > 10000:
        commission_percentage = 0.12
elif city == "Varna":
    if 0 <= s_volume <= 500:
        commission_percentage = 0.045
    elif 500 < s_volume <= 1000:
        commission_percentage = 0.075
    elif 1000 < s_volume <= 10000:
        commission_percentage = 0.10
    elif s_volume > 10000:
        commission_percentage = 0.13
elif city == "Plovdiv":
    if 0 <= s_volume <= 500:
        commission_percentage = 0.055
    elif 500 < s_volume <= 1000:
        commission_percentage = 0.08
    elif 1000 < s_volume <= 10000:
        commission_percentage = 0.12
    elif s_volume > 10000:
        commission_percentage = 0.145

total_commission = s_volume * commission_percentage

if total_commission >= 0 and valid_commission and valid_cities:
    print(f"{total_commission:.2f}")
else:
    print("error")
