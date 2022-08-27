step_target = 10000
current_walked_steps = 0

while current_walked_steps < step_target:
    current_steps = input()
    if current_steps == 'Going home':
        current_steps = int(input())
        current_walked_steps += current_steps
        break
    current_steps = int(current_steps)
    current_walked_steps += current_steps
difference = abs(current_walked_steps - step_target)
if current_walked_steps >= step_target:
    print('Goal reached! Good job!')
    print(f'{difference} steps over the goal!')
else:
    print(f'{difference} more steps to reach goal.')
