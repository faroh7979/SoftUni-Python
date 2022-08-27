rent_hall = int(input())

figurines = rent_hall * 0.70
food = figurines * 0.85
sound_efects = food / 2

total = rent_hall + figurines + food + sound_efects
totalf = "{:.2f}".format(total)
print(totalf)
