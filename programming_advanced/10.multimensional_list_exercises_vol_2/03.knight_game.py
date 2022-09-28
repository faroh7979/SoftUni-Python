chess_board_size = int(input())
matrix = [[_ for _ in input()] for _ in range(chess_board_size)]

knight_possible_moves = (
    (2, 1),
    (2, - 1),
    (1, 2),
    (1, - 2),
    (- 1, 2),
    (- 1, - 2),
    (- 2, 1),
    (- 2, - 1)
)

removed_knights = 0

while True:
    max_hits = 0
    max_hits_position = []

    for row in range(chess_board_size):
        for col in range(chess_board_size):
            if matrix[row][col] == 'K':
                current_attacks = 0

                for movement in knight_possible_moves:
                    new_row = row + movement[0]
                    new_col = col + movement[1]

                    if 0 <= new_row < chess_board_size and 0 <= new_col < chess_board_size:
                        if matrix[new_row][new_col] == 'K':
                            current_attacks += 1

                if current_attacks > max_hits:
                    max_hits = current_attacks
                    max_hits_position = [row, col]

    if max_hits_position:
        matrix[max_hits_position[0]][max_hits_position[1]] = 'O'
        removed_knights += 1

    else:
        break

print(removed_knights)
