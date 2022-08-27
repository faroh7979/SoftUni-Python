team_name = input()
played_games = int(input())
total_points = 0
wins = 0
drawn = 0
loses = 0

for games in range(played_games):
    result = input()
    if result == 'W':
        total_points += 3
        wins += 1
    elif result == 'D':
        total_points += 1
        drawn += 1
    elif result == 'L':
        loses += 1

if played_games == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    win_rate = wins / played_games * 100
    print(f'{team_name} has won {total_points} points during this season.')
    print('Total stats:')
    print(f'## W: {wins}')
    print(f'## D: {drawn}')
    print(f'## L: {loses}')
    print(f'Win rate: {win_rate:.2f}%')
