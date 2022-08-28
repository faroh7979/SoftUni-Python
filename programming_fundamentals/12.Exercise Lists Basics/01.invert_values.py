custom_string = input()
my_list = custom_string.split()
opposite_list = []

for element in my_list:
    opposite_list.append(-int(element))
print(opposite_list)