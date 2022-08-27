priceveg=float(input())
pricefru=float(input())
weightveg=int(input())
weightfru=int(input())
increase=(priceveg*weightveg+pricefru*weightfru)/1.94
increasef="{:.2f}".format(increase)
print(increasef)
