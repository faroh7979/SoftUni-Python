team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
terminated_game = False
card_notebook = input().split()

for card in card_notebook:
    if card in team_a:
        team_a.remove(card)
    elif card in team_b:
        team_b.remove(card)
    if team_a.__len__() < 7 or team_b.__len__() < 7:
        terminated_game = True
        break
team_a_players = team_a.__len__()
team_b_players = team_b.__len__()

if terminated_game:
    print(f'Team A - {team_a_players}; Team B - {team_b_players}')
    print('Game was terminated')
else:
    print(f'Team A - {team_a_players}; Team B - {team_b_players}')
