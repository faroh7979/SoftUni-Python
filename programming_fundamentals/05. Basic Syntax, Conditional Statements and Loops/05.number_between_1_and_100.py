num = float(input())

while num < 1 or num > 100:
    num = float(input())
else:
    print(f'The number {num:.1f} is between 1 and 100')