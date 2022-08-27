budget = float(input())
video_cards_count = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards_price = 250
sum_video_cards = video_cards_count * video_cards_price

processors_price = sum_video_cards * 0.35
ram_price = sum_video_cards * 0.1

total_price = sum_video_cards + processors_count * processors_price + ram_count * ram_price

if video_cards_count > processors_count:
    total_price *= 0.85
difference = abs(total_price - budget)

if budget >= total_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
