total_sold_games = int(input())
hearthstone = 0
for_nite = 0
over_watch = 0
others = 0


for games in range(total_sold_games):
    game_name = input()
    if game_name == 'Hearthstone':
        hearthstone += 1
    elif game_name == 'Fornite':
        for_nite += 1
    elif game_name == 'Overwatch':
        over_watch += 1
    else:
        others += 1
for_nite_percentage = for_nite / total_sold_games * 100
hearthstone_percentage = hearthstone / total_sold_games * 100
over_watch_percentage = over_watch / total_sold_games * 100
others_percentage = others / total_sold_games * 100

print(f'Hearthstone - {hearthstone_percentage:.2f}%')
print(f'Fornite - {for_nite_percentage:.2f}%')
print(f'Overwatch - {over_watch_percentage:.2f}%')
print(f'Others - {others_percentage:.2f}%')
