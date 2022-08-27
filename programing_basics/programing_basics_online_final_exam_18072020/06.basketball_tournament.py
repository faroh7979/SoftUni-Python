tournament_name = input()
desi_team_wins = 0
desi_team_loses = 0
total_games = 0
while tournament_name != 'End of tournaments':
    total_current_games = int(input())
    for game in range(1, total_current_games + 1):
        desi_team_points = int(input())
        enemy_team_points = int(input())
        point_diff = abs(desi_team_points - enemy_team_points)
        if desi_team_points > enemy_team_points:
            desi_team_wins += 1
            total_games += 1
            print(f'Game {game} of tournament {tournament_name}: win with {point_diff} points.')
        elif desi_team_points < enemy_team_points:
            desi_team_loses += 1
            total_games += 1
            print(f'Game {game} of tournament {tournament_name}: lost with {point_diff} points.')
        else:
            print('No possible draw!')
    tournament_name = input()
win_percentage = desi_team_wins / total_games * 100
lost_percentage = desi_team_loses / total_games * 100
print(f'{win_percentage:.2f}% matches win')
print(f'{lost_percentage:.2f}% matches lost')
