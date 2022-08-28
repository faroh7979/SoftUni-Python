first_int = int(input())
second_int = int(input())
my_list = [first_int, second_int]

a_old = my_list[0]
a_new = my_list[1]
b_old = my_list[1]
b_new = my_list[0]

print('Before:')
print(f'a = {a_old}')
print(f'b = {b_old}')
print('After:')
print(f'a = {a_new}')
print(f'b = {b_new}')
