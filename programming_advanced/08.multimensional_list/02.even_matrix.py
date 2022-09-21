total_matrix_rows = int(input())
final_list = []

for current_row in range(total_matrix_rows):
    current_column = [int(i) for i in input().split(', ') if int(i) % 2 == 0]
    final_list.append(current_column)

print(final_list)
