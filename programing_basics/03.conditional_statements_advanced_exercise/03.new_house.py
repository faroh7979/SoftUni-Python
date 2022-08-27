flower_type = input()
total_flowers = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.80
tulip_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

expense = 0

if flower_type == "Roses":
    if total_flowers > 80:
        expense = total_flowers * rose_price * 0.9
    else:
        expense = total_flowers * rose_price
elif flower_type == "Dahlias":
    if total_flowers > 90:
        expense = total_flowers * dahlia_price * 0.85
    else:
        expense = total_flowers * dahlia_price
elif flower_type == "Tulips":
    if total_flowers > 80:
        expense = total_flowers * tulip_price * 0.85
    else:
        expense = total_flowers * tulip_price
elif flower_type == "Narcissus":
    if total_flowers < 120:
        expense = total_flowers * narcissus_price * 1.15
    else:
        expense = total_flowers * narcissus_price
elif flower_type == "Gladiolus":
    if total_flowers < 80:
        expense = total_flowers * gladiolus_price * 1.20
    else:
        expense = total_flowers * gladiolus_price
difference = abs(budget - expense)
if budget >= expense:
    print(f"Hey, you have a great garden with {total_flowers} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")
