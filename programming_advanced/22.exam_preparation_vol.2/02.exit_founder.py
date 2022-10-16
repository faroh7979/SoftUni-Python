from collections import deque

players_que = deque(input().split(', '))
rows, cols = 6, 6

matrix = [[i for i in input().split()]for _ in range(rows)]
current_move = 0
moves_for_resting = []

while True:
    player_on_move = players_que.popleft()
    players_que.append(player_on_move)

    coordinates = input()
    current_row = int(coordinates[1])
    current_col = int(coordinates[-2])

    current_move += 1  # keep on track for resting moves
    if current_move in moves_for_resting:
        continue

    if matrix[current_row][current_col] == 'E':
        print(f"{player_on_move} found the Exit and wins the game!")
        break

    elif matrix[current_row][current_col] == 'T':
        print(f"{player_on_move} is out of the game! The winner is {players_que[0]}.")
        break

    elif matrix[current_row][current_col] == 'W':
        print(f"{player_on_move} hits a wall and needs to rest.")
        moves_for_resting.append(current_move + 2)
