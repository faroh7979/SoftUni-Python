divisor = int(input())
boundary = int(input())
searched_num = ''
for n in range(boundary, 0, -1):
    if n % divisor == 0:
        searched_num = n
        break
print(searched_num)
