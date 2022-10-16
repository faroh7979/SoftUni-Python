from collections import deque

seat_numbers = input().split(', ')

first_nums = deque(map(int, (input().split(', '))))
second_nums = deque(map(int, (input().split(', '))))

total_rotations = 0
taken_seats = []

while total_rotations < 10:
    total_rotations += 1

    int_first = first_nums.popleft()
    int_second = second_nums.pop()
    ascii_character = chr(int_first + int_second)
    first_generated_seat = str(int_first) + ascii_character
    second_generated_seat = str(int_second) + ascii_character

    if first_generated_seat in seat_numbers or second_generated_seat in seat_numbers:
        if first_generated_seat in taken_seats or second_generated_seat in taken_seats:
            continue

        else:
            if first_generated_seat in seat_numbers:
                taken_seats.append(first_generated_seat)

            elif second_generated_seat in seat_numbers:
                taken_seats.append(second_generated_seat)

            if len(taken_seats) == 3:
                break

    else:
        first_nums.append(int_first)
        second_nums.appendleft(int_second)

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {total_rotations}')
