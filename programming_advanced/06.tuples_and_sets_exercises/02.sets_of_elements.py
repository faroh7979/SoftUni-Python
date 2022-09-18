first_set_number_of_elements, second_set_number_of_elements = list(map(int, input().split()))
first_set = set()
second_set = set()

for _ in range(first_set_number_of_elements):
    element = input()
    first_set.add(element)

for _ in range(second_set_number_of_elements):
    second_element = input()
    second_set.add(second_element)

final_set = first_set.intersection(second_set)

for number in final_set:
    print(number)
