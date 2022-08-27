total_joinery = int(input())
type_joinery = input()
delivery_type = input()
single_price = 0
delivery = 60

if type_joinery == "90X130":
    single_price = 110
    if total_joinery > 60:
        single_price *= 0.92
    elif total_joinery > 30:
        single_price *= 0.95
elif type_joinery == "100X150":
    single_price = 140
    if total_joinery > 80:
        single_price *= 0.90
    elif total_joinery > 40:
        single_price *= 0.94
elif type_joinery == "130X180":
    single_price = 190
    if total_joinery > 50:
        single_price *= 0.88
    elif total_joinery > 20:
        single_price *= 0.93
elif type_joinery == "200X300":
    single_price = 250
    if total_joinery > 50:
        single_price *= 0.86
    elif total_joinery > 25:
        single_price *= 0.91
if delivery_type == "Without delivery":
    delivery = 0
total_price = total_joinery * single_price + delivery
if total_joinery < 10:
    print("Invalid order")
else:
    if total_joinery > 99:
        total_price *= 0.96
        print(f"{total_price:.2f} BGN")
    else:
        print(f"{total_price:.2f} BGN")
