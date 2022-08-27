product = input()
city = input()
quantity = float(input())

coffee = 0
water = 0
beer = 0
sweets = 0
peanuts = 0

if city == "Sofia":
    if product == "coffee":
        coffee = 0.50 * quantity
        print(coffee)
    elif product == "water":
        water = 0.80 * quantity
        print(water)
    elif product == "beer":
        beer = 1.20 * quantity
        print(beer)
    elif product == "sweets":
        sweets = 1.45 * quantity
        print(sweets)
    elif product == "peanuts":
        peanuts = 1.60 * quantity
        print(peanuts)
elif city == "Plovdiv":
    if product == "coffee":
        coffee = 0.40 * quantity
        print(coffee)
    elif product == "water":
        water = 0.70 * quantity
        print(water)
    elif product == "beer":
        beer = 1.15 * quantity
        print(beer)
    elif product == "sweets":
        sweets = 1.30 * quantity
        print(sweets)
    elif product == "peanuts":
        peanuts = 1.50 * quantity
        print(peanuts)
elif city == "Varna":
    if product == "coffee":
        coffee = 0.45 * quantity
        print(coffee)
    elif product == "water":
        water = 0.70 * quantity
        print(water)
    elif product == "beer":
        beer = 1.10 * quantity
        print(beer)
    elif product == "sweets":
        sweets = 1.35 * quantity
        print(sweets)
    elif product == "peanuts":
        peanuts = 1.55 * quantity
        print(peanuts)
