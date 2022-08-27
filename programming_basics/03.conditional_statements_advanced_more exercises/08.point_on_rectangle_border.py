x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())
position = "Inside / Outside"

if x == x1 or x == x2:
    if y1 <= y <= y2:
        position = "Border"
elif y == y1 or y == y2:
    if x1 <= x <= x2:
        position = "Border"
print(position)
