price_bag_over_20 = float(input())                       #•	"The total price of bags is: {цената на багажите} lv."
bag_kologrames = float(input())
days_before_trip = int(input())
count_bags = int(input())

if bag_kologrames < 10:
    price_bag = price_bag_over_20 * 0.2

elif bag_kologrames >= 10 and bag_kologrames <= 20:
    price_bag = price_bag_over_20 * 0.5

else: price_bag = price_bag_over_20

if days_before_trip > 30:
    price = price_bag * 1.1

elif days_before_trip <= 30 and days_before_trip >= 7:
    price = price_bag * 1.15

else: price = price_bag * 1.40

total_price = price * count_bags

total_pricef = "{:.2f}".format(total_price)

print(f"The total price of bags is: {total_pricef} lv.")
