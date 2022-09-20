from collections import deque

integer_list = deque(list(map(int, input().split())))

for _ in range(len(integer_list)):
    print(integer_list.pop(), end=' ')
