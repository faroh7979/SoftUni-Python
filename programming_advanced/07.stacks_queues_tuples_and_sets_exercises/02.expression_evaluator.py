from collections import deque

string_for_maths = input().split()
numbers_for_calculating = deque()
current_score = 0
operation_elements = ['+', '-', '*', '/']

for element in string_for_maths:
    if element in operation_elements:
        current_score = numbers_for_calculating.popleft()  # we will put current_score on the first place on the deque

        if element == '+':
            current_score += sum(numbers_for_calculating)

            numbers_for_calculating = deque()  # we should clear it before adding current_score
            numbers_for_calculating.append(current_score)

        elif element == '-':
            current_score -= sum(numbers_for_calculating)

            numbers_for_calculating = deque()  # we should clear it before adding current_score
            numbers_for_calculating.append(current_score)

        elif element == '*':
            for multiplier in numbers_for_calculating:
                current_score *= multiplier

            numbers_for_calculating = deque()  # we should clear it before adding current_score
            numbers_for_calculating.append(current_score)

        elif element == '/':
            for divider in numbers_for_calculating:
                current_score = int(current_score / divider)

            numbers_for_calculating = deque()  # we should clear it before adding current_score
            numbers_for_calculating.append(current_score)

    else:
        numbers_for_calculating.append(int(element))

print(current_score)
