first_player_eggs = int(input())
second_player_eggs = int(input())
early_end = False
while first_player_eggs != 0 and second_player_eggs != 0:
    winner = input()
    if winner == 'End of battle':
        early_end = True
        break
    elif winner == 'one':
        second_player_eggs -= 1
    elif winner == 'two':
        first_player_eggs -= 1

if early_end:
    print(f'Player one has {first_player_eggs} eggs left.')
    print(f'Player two has {second_player_eggs} eggs left.')
elif first_player_eggs == 0:
    print(f'Player one is out of eggs. Player two has {second_player_eggs} eggs left.')
elif second_player_eggs == 0:
    print(f'Player two is out of eggs. Player one has {first_player_eggs} eggs left.')
