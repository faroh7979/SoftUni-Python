from math import floor

total_tournament_participate = int(input())
starting_points = int(input())
next_tournaments_points = 0
won_tournaments = 0

for tournaments in range(total_tournament_participate):
    stage = input()
    if stage == 'W':
        next_tournaments_points += 2000
        won_tournaments += 1
    elif stage == 'F':
        next_tournaments_points += 1200
    elif stage == 'SF':
        next_tournaments_points += 720
final_points = starting_points + next_tournaments_points
average_points = floor(next_tournaments_points / total_tournament_participate)
percentage_of_winning_tournaments = won_tournaments / total_tournament_participate * 100

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{percentage_of_winning_tournaments:.2f}%')
