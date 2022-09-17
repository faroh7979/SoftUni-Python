sequence = tuple(map(float, input().split()))
unique_numbers = []

for element in sequence:
    if element not in unique_numbers:
        unique_numbers.append(element)

for element in unique_numbers:
    count_of_element = sequence.count(element)
    print(f'{element} - {count_of_element} times')
