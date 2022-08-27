total_weights = int(input())
total_tons = 0
total_price = 0
total_bus_weight = 0
total_truck_weight = 0
total_train_weight = 0

for weights in range(total_weights):
    current_weight = int(input())
    total_tons += current_weight
    if current_weight < 4:
        total_bus_weight += current_weight
        total_price += current_weight * 200
    elif current_weight < 12:
        total_truck_weight += current_weight
        total_price += current_weight * 175
    else:
        total_train_weight += current_weight
        total_price += current_weight * 120
average_ton_price = total_price / total_tons
bus_percentage = total_bus_weight / total_tons * 100
truck_percentage = total_truck_weight / total_tons * 100
train_percentage = total_train_weight / total_tons * 100

print(f'{average_ton_price:.2f}')
print(f'{bus_percentage:.2f}%')
print(f'{truck_percentage:.2f}%')
print(f'{train_percentage:.2f}%')
