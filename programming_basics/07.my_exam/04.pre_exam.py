total_days = int(input())
liters_rakia = 0
total_degrees = 0

for boils in range(total_days):
    current_liters = float(input())
    current_degrees = float(input())
    liters_rakia += current_liters
    total_degrees += current_liters * current_degrees
average_degrees = total_degrees / liters_rakia

print(f'Liter: {liters_rakia:.2f}')
print(f'Degrees: {average_degrees:.2f}')
if average_degrees < 38:
    print('Not good, you should baking!')
elif average_degrees <= 42:
    print('Super!')
else:
    print('Dilution with distilled water!')
