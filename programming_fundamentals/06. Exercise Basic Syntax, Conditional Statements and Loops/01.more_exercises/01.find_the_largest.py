client_num = int(input())
my_list = []
new_num = ''

for index, digit in enumerate(str(client_num)):
    my_list.append(digit)
my_list.sort(reverse=True)
for index, digit in enumerate(my_list):
    new_num += my_list[index]
print(new_num)
