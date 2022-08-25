chicken_menus = int(input())
fish_menus = int(input())
vegie_menus = int(input())

chicken_price = 10.35
fish_price = 12.40
vegie_price = 8.15

menus_sum = (chicken_menus * chicken_price) + \
            (fish_price * fish_menus) + \
            (vegie_price * vegie_menus)

desert = menus_sum * 0.2
delivery = 2.50

total = menus_sum + desert + delivery

print (total)
