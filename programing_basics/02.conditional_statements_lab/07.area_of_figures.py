from math import pi

figure = input()

if figure == "square":
    side_a = float(input())
    area = "{:.3f}".format(round(side_a * side_a , 3))
    print(area)

elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area= "{:.3f}".format(round(side_a*side_b , 3))
    print(area)

elif figure == "circle":
    radius = float(input())
    area = "{:.3f}".format(round(pi * radius * radius , 3))
    print(area)

elif figure == "triangle":
    side_a = float(input())
    ha = float(input())
    area = "{:.3f}".format(round(ha * side_a / 2 , 3))
    print(area)

