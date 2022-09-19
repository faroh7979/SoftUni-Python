from collections import deque

chocolates = deque(map(int, input().split(', ')))
milk_cups = deque(map(int, input().split(', ')))

the_job_is_done = False
prepared_milk_shakes = 0

while chocolates and milk_cups:
    chocolates_quantity = chocolates.pop()
    if chocolates_quantity <= 0:  # should remove zero and negative values

        if milk_cups[0] <= 0:  # should remove also current milk_cup if not greater than zero
            milk_cups.popleft()

        if not chocolates:  # should break, because of empty deck
            break
        continue

    milk_cup_quantity = milk_cups.popleft()
    if milk_cup_quantity <= 0:
        # we should return the value of chocolates, because we will restart the loop
        chocolates.append(chocolates_quantity)

        if not milk_cups:  # should break, because of empty deck
            break
        continue

    if chocolates_quantity == milk_cup_quantity:
        prepared_milk_shakes += 1
        if prepared_milk_shakes == 5:
            the_job_is_done = True
            break

    else:
        chocolates_quantity -= 5
        chocolates.append(chocolates_quantity)
        milk_cups.append(milk_cup_quantity)

if the_job_is_done:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f'Chocolate: {", ".join(map(str, chocolates))}')
else:
    print("Chocolate: empty")

if milk_cups:
    print(f'Milk: {", ".join(map(str, milk_cups))}')
else:
    print("Milk: empty")
