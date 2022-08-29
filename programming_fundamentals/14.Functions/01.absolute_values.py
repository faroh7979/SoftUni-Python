num_list = input().split(" ")
float_list = []
for current_value in num_list:
    current_float = float(current_value)
    current_float_abs = abs(current_float)
    float_list.append(current_float_abs)
print(float_list)
