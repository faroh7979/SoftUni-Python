v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

total_water_in_pool = p1 * h + p2 * h
p1_percentage = p1 * h / total_water_in_pool * 100
p2_percentage = p2 * h / total_water_in_pool * 100
p_total = total_water_in_pool / v * 100

difference = abs(total_water_in_pool - v)

if v >= total_water_in_pool:
    print(f"The pool is {p_total:.2f}% full. Pipe 1: {p1_percentage:.2f}%. Pipe 2: {p2_percentage:.2f}%.")
else:
    print(f"For {h:.2f} hours the pool overflows with {difference:.2f} liters.")
