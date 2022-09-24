from collections import deque

single_bullet_price = int(input())
gun_barrel_size = int(input())
bullets_by_size = list(map(int, input().split()))
locks_by_size = deque(map(int, input().split()))
intelligence_value = int(input())
total_used_bullets = 0

while bullets_by_size and locks_by_size:
    total_used_bullets += 1

    current_lock = locks_by_size.popleft()
    current_bullet = bullets_by_size.pop()

    if current_bullet <= current_lock:
        print('Bang!')

    else:
        locks_by_size.appendleft(current_lock)
        print('Ping!')

    if total_used_bullets % gun_barrel_size == 0 and bullets_by_size:
        print('Reloading!')

bullets_left = len(bullets_by_size)
locks_left = len(locks_by_size)

bullets_expense = single_bullet_price * total_used_bullets
earned_money = intelligence_value - bullets_expense

if not locks_left:
    print(f'{bullets_left} bullets left. Earned ${earned_money}')
else:
    print(f"Couldn't get through. Locks left: {locks_left}")
