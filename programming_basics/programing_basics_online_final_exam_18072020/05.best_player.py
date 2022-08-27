player_name = input()
goals_by = ''
max_goals = 0
is_hat_trick = False

while player_name != 'END':
    player_goals = int(input())
    if player_goals > max_goals:
        max_goals = player_goals
        goals_by = player_name
    if player_goals >= 10:
        break
    player_name = input()
if max_goals > 2:
    is_hat_trick = True
if is_hat_trick:
    print(f'{goals_by} is the best player!')
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f'{goals_by} is the best player!')
    print(f'He has scored {max_goals} goals.')
