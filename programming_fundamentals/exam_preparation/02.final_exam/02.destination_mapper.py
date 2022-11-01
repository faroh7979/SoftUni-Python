import re
total_score = 0
destination_list = []

reg_destinations = input()
destination_pattern = r'=([A-Z][A-z]{2,})=|\/([A-Z][A-z]{2,})\/'
valid_destinations = re.findall(destination_pattern, reg_destinations)
for element in valid_destinations:
    for sub_element in element:
        if sub_element:
            destination_list.append(sub_element)
            total_score += len(sub_element)
print(f'Destinations: {", ".join(destination_list)}')
print(f'Travel Points: {total_score}')
