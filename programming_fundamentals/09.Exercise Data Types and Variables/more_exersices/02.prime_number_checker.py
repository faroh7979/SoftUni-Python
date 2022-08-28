client_num = int(input())
is_prime = True

for divider in range(2, client_num):
    if client_num % divider == 0:
        is_prime = False
        break
if is_prime:
    print(is_prime)
else:
    print(is_prime)
