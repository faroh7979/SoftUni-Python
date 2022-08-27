customer=float(input())

if customer >=5 and customer <=11.9:

    print("Cold")
elif customer >=12 and customer <=14.9:
    print("Cool")
elif customer >=15 and customer <=20:
    print("Mild")
elif customer >=20.1 and customer <=25.9:
    print("Warm")
elif customer >=26 and customer <=35:
    print("Hot")
else:
    print("unknown")
