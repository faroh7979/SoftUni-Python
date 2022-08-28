total_integers = int(input())
my_list = []
filtered_list = []

for _ in range(total_integers):
    current_int = int(input())
    my_list.append(current_int)
command = input()
if command == 'even':
    for current_element in my_list:
        if current_element % 2 == 0:
            filtered_list.append(current_element)
elif command == 'odd':
    for current_element in my_list:
        if current_element % 2 != 0:
            filtered_list.append(current_element)
elif command == 'negative':
    for current_element in my_list:
        if current_element < 0:
            filtered_list.append(current_element)
elif command == 'positive':
    for current_element in my_list:
        if current_element >= 0:
            filtered_list.append(current_element)
print(filtered_list)
