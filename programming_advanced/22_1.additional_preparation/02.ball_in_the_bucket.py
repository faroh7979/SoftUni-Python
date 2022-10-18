ROWS, COLS = 6, 6
TOTAL_COORDINATES = 3

matrix = [[i for i in input().split()] for _ in range(ROWS)]
coordinates = [[int(i) for i in input().strip('()').split(', ')] for _ in range(TOTAL_COORDINATES)]
prizes = {
    'Lego Construction Set': 300,
    'Teddy Bear': 200,
    'Football': 100,
}


total_score = 0
for coordinate in coordinates:
    current_row, current_col = coordinate
    invalid_coordinate = False

    for current_index in range(len(coordinate)):  # check for rows and cols if is out of matrix
        if coordinate[current_index] < 0 or coordinate[current_index] >= ROWS:
            invalid_coordinate = True
            break

    if invalid_coordinate:
        continue

    current_position = matrix[current_row][current_col]

    if current_position == 'B':
        matrix[current_row][current_col] = 0

        for scoring_row in range(ROWS):
            total_score += int(matrix[scoring_row][current_col])  # because summing only the current column

for toy in prizes:
    if total_score >= prizes[toy]:
        print(f"Good job! You scored {total_score} points, and you've won {toy}.")
        break
else:
    needed_points = prizes['Football'] - total_score
    print(f"Sorry! You need {needed_points} points more to win a prize.")
