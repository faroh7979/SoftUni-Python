taste = input()
size = input()
total_sets = int(input())
single_set_price = 0
total_gels = 0

if taste == "Watermelon":
    if size == "small":
        single_set_price = 56
        total_gels = total_sets * 2
    elif size == "big":
        single_set_price = 28.70
        total_gels = total_sets * 5
elif taste == "Mango":
    if size == "small":
        single_set_price = 36.66
        total_gels = total_sets * 2
    elif size == "big":
        single_set_price = 19.60
        total_gels = total_sets * 5
elif taste == "Pineapple":
    if size == "small":
        single_set_price = 42.10
        total_gels = total_sets * 2
    elif size == "big":
        single_set_price = 24.80
        total_gels = total_sets * 5
elif taste == "Raspberry":
    if size == "small":
        single_set_price = 20.00
        total_gels = total_sets * 2
    elif size == "big":
        single_set_price = 15.20
        total_gels = total_sets * 5
total_price = single_set_price * total_gels
if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.50
print(f"{total_price:.2f} lv.")
