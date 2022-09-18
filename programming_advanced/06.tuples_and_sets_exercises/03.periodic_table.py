total_inputs = int(input())
unique_elements = set()

for _ in range(total_inputs):
    current_elements = input().split()
    for element in current_elements:
        unique_elements.add(element)

for chemical_element in unique_elements:
    print(chemical_element)
