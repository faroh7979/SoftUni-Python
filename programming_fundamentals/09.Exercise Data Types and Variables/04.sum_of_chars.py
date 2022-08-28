num_of_char = int(input())
total_score = 0

for _ in range(num_of_char):
    current_char = input()
    total_score += ord(current_char)
print(f'The sum equals: {total_score}')