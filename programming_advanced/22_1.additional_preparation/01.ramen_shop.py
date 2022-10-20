from collections import deque

bowls = [int(i) for i in input().split(', ')]
players = deque([int(i) for i in input().split(', ')])

while bowls and players:
    bowl = bowls.pop()
    player = players.popleft()

    if bowl > player:
        bowl -= player
        bowls.append(bowl)

    elif bowl < player:
        player -= bowl
        players.appendleft(player)

if not players:
    print('Great job! You served all the customers.')
    if bowls:
        print(f'Bowls of ramen left: {", ".join(map(str, bowls))}')

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f'Customers left: {", ".join(map(str, players))}')
