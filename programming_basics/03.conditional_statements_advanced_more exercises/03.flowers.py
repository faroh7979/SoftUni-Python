chrysanthemum_total = int(input())
roses_total = int(input())
tulips_total = int(input())
season = input()
is_holiday = input()
total_flowers = chrysanthemum_total + roses_total + tulips_total
bouquet = 2
chrysanthemum_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15
if is_holiday == "Y":
    chrysanthemum_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15
bouquet_price = chrysanthemum_price * chrysanthemum_total + tulips_price * tulips_total + roses_price * roses_total
if tulips_total > 7 and season == "Spring":
    bouquet_price *= 0.95
if roses_total >= 10 and season == "Winter":
    bouquet_price *= 0.90
if total_flowers > 20:
    bouquet_price *= 0.8
bouquet_price += bouquet
print(f"{bouquet_price:.2f}")
