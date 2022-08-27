town = input()
reservation_type = input()
vip_card = input()
idle_time = int(input())
price_per_day = 0


if town == "Bansko" or town == "Borovets":
    if reservation_type == "withEquipment":
        price_per_day = 100
        if vip_card == "yes":
            price_per_day *= 0.9
    elif reservation_type == "noEquipment":
        price_per_day = 80
        if vip_card == "yes":
            price_per_day *= 0.95
elif town == "Varna" or town == "Burgas":
    if reservation_type == "withBreakfast":
        price_per_day = 130
        if vip_card == "yes":
            price_per_day *= 0.88
    elif reservation_type == "noBreakfast":
        price_per_day = 100
        if vip_card == "yes":
            price_per_day *= 0.93
if idle_time > 7:
    idle_time -= 1
total_price = idle_time * price_per_day
if idle_time < 1:
    print("Days must be positive number!")
elif (town == "Bansko" or town == "Burgas" or town == "Borovets" or town == "Varna") \
        and (reservation_type == "noEquipment" or reservation_type == "withEquipment" or \
             reservation_type == "noBreakfast" or reservation_type == "withBreakfast"):
    print(f"The price is {total_price:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
