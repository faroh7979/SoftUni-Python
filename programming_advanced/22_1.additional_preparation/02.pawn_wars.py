from collections import deque

ROWS, COLS = 8, 8
chessboard = []

white_pawn = [0, 0]
black_pawn = [0, 0]
players_turns = deque(['w', 'b'])

for row_index in range(ROWS):
    col = input().split()
    chessboard.append(col)

    if 'b' in col:
        black_pawn = [row_index, col.index('b')]

    if 'w' in col:
        white_pawn = [row_index, col.index('w')]

while True:
    players_move = players_turns.popleft()
    players_turns.append(players_move)

    if players_move == 'w':
        if white_pawn[0] - 1 == 0:
            print(f'Game over! White pawn is promoted to a queen at {chr(97 + white_pawn[1])}8.')
            break

        if white_pawn[1] + 1 < COLS:
            if chessboard[white_pawn[0] - 1][white_pawn[1] + 1] == 'b':
                print(f'Game over! White win, capture on {chr(97 + white_pawn[1] + 1)}{ROWS - white_pawn[0] + 1}.')
                break

        if white_pawn[1] - 1 >= 0:
            if chessboard[white_pawn[0] - 1][white_pawn[1] - 1] == 'b':
                print(f'Game over! White win, capture on {chr(97 + white_pawn[1] - 1)}{ROWS - white_pawn[0] + 1}.')
                break

        chessboard[white_pawn[0]][white_pawn[1]] = '-'
        chessboard[white_pawn[0] - 1][white_pawn[1]] = 'w'
        white_pawn[0] -= 1

    elif players_move == 'b':
        if black_pawn[0] + 1 == ROWS:
            print(f'Game over! Black pawn is promoted to a queen at {chr(97 + black_pawn[1])}1.')
            break

        if black_pawn[1] + 1 < COLS:
            if chessboard[black_pawn[0] + 1][black_pawn[1] + 1] == 'w':
                print(f'Game over! Black win, capture on {chr(97 + black_pawn[1] + 1)}{ROWS - black_pawn[0] + 1}.')
                break

        if black_pawn[1] - 1 >= 0:
            if chessboard[black_pawn[0] + 1][black_pawn[1] - 1] == 'w':
                print(f'Game over! Black win, capture on {chr(97 + black_pawn[1] - 1)}{ROWS - black_pawn[0] + 1}.')
                break

        chessboard[black_pawn[0]][black_pawn[1]] = '-'
        chessboard[black_pawn[0] + 1][black_pawn[1]] = 'b'
        black_pawn[0] += 1
