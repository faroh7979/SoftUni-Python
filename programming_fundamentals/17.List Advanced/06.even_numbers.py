int_list = list(map(int, input().split(', ')))
indices = [i for i in range(len(int_list)) if int_list[i] % 2 == 0]
print(indices)
