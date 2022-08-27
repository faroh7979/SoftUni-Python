num_lines = int(input())
all_num_are_even = True
for i in range(num_lines):
    num = int(input())
    if num % 2 != 0:
        print(f'{num} is odd!')
        all_num_are_even = False
        break
if all_num_are_even:
    print('All numbers are even.')