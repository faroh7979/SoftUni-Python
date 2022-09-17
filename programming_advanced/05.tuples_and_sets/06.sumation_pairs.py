from collections import deque

kid_names = deque(input().split())
n_toss = int(input())

counter = 1
while len(kid_names) > 1:
    if counter == n_toss:
        removed_child = kid_names.popleft()
        counter = 1
        print(f'Removed {removed_child}')
    else:
        moved_child = kid_names.popleft()
        kid_names.append(moved_child)
        counter += 1

last_kid = kid_names.popleft()

print(f'Last is {last_kid}')
