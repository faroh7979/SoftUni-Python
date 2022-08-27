points = int(input())

if points <= 100:
    bonus = 5
elif points < 1000:
    bonus = points * 0.2
else: bonus = points * 0.1

if points % 2 == 0:
    bonus_third = 1
else: bonus_third = 0
if str(points)[-1] == str(5):
    bonus_fourth = 2
else: bonus_fourth = 0

bonus_point = bonus + bonus_third + bonus_fourth
total_points = points + bonus_point

print(bonus_point)
print(total_points)
# print(5%10)
