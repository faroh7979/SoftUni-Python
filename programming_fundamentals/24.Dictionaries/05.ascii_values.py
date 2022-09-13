char_list = input().split(', ')
my_first_dict_comprehension = {key: ord(key) for key in char_list}
print(my_first_dict_comprehension)
