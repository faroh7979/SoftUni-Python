clothes_box_stack = list(map(int, input().split()))
rack_capacity = int(input())

total_used_racks = 1
current_rack_used = 0


while clothes_box_stack:
    current_capacity = clothes_box_stack.pop()

    if current_rack_used + current_capacity < rack_capacity:
        current_rack_used += current_capacity

    elif current_rack_used + current_capacity == rack_capacity:
        if clothes_box_stack:
            total_used_racks += 1
            current_rack_used = 0

    else:
        total_used_racks += 1
        current_rack_used = 0
        clothes_box_stack.append(current_capacity)

print(total_used_racks)
