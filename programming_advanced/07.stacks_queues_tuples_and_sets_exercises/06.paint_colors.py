from collections import deque
# Note: You could find some of the main colors needed to keep a secondary color after it is found.
colorful_string = deque(input().split())
main_colors = {'red', 'yellow', 'blue'}
secondary_colors = {'orange', 'purple', 'green'}

founded_both_type_colors = []

while colorful_string:
    if len(colorful_string) == 1:  # check if we have only one substring left, if zero while will break before
        if colorful_string[0] in main_colors or colorful_string[0] in secondary_colors:
            founded_both_type_colors.append(colorful_string[0])  # need of index because it is a deque collection
        break  # the string is empty now

    first_substring = colorful_string.popleft()
    last_substring = colorful_string.pop()
    first_possible_concatenate = first_substring + last_substring
    second_possible_concatenate = last_substring + first_substring

    if first_possible_concatenate in main_colors or first_possible_concatenate in secondary_colors:
        founded_both_type_colors.append(first_possible_concatenate)

    elif second_possible_concatenate in main_colors or second_possible_concatenate in secondary_colors:
        founded_both_type_colors.append(second_possible_concatenate)

    else:
        first_substring = first_substring[:-1]
        last_substring = last_substring[:-1]

        colorful_string_length = len(colorful_string)  # because we should return the both popped substrings
        middle_of_string = int(colorful_string_length / 2)

        if colorful_string_length > 0:
            # should check how many substring there is and put the middle as it said in task
            if colorful_string_length % 2 == 0:
                middle_of_string = int(colorful_string_length / 2)
            else:
                middle_of_string = int(colorful_string_length / 2) + 1

            if last_substring:  # no need of empty substring
                colorful_string.insert(middle_of_string, last_substring)  # insert first because after we ll be replaced
            if first_substring:  # no need of empty substring
                colorful_string.insert(middle_of_string, first_substring)

        else:  # if only manipulated substring left
            if last_substring:
                colorful_string.append(first_substring)
            if first_substring:
                colorful_string.append(first_substring)

# we should check if our collection contains secondary color and decide if should keep it or remove it
elements_for_removing = []
for element in founded_both_type_colors:
    if element in secondary_colors:
        if element == 'orange':
            if 'red' in founded_both_type_colors and 'yellow' in founded_both_type_colors:
                continue
            else:
                elements_for_removing.append(element)

        elif element == 'purple':
            if 'red' in founded_both_type_colors and 'blue' in founded_both_type_colors:
                continue
            else:
                elements_for_removing.append(element)

        elif element == 'green':
            if 'blue' in founded_both_type_colors and 'yellow' in founded_both_type_colors:
                continue
            else:
                elements_for_removing.append(element)

if elements_for_removing:
    for removing_element in elements_for_removing:
        founded_both_type_colors.remove(removing_element)

print(founded_both_type_colors)
