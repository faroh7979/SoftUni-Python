n = int(input())
max_value = float('-inf')
min_value = float('inf')
if n > 0:
    for i in range(0, n):
        client_value = int(input())
        if client_value > max_value:
            max_value = client_value
        if client_value < min_value:
            min_value = client_value
    print(f"Max number: {max_value}")
    print(f"Min number: {min_value}")
else:
    print(f"Max number: 0")
    print(f"Min number: 0")
