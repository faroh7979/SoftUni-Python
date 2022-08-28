factor = int(input())
count = int(input())
my_list = []
current_num = factor

for _ in range(count):
    my_list.append(current_num)
    current_num += factor
print(my_list)
