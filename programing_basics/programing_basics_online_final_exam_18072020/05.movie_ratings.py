from sys import maxsize

total_picked_movies = int(input())
max_rate = -maxsize
max_rate_name = ''
min_rate = maxsize
min_rate_name = ''
total_score = 0

for movies in range(total_picked_movies):
    movie_name = input()
    movie_rate = float(input())
    if movie_rate > max_rate:
        max_rate = movie_rate
        max_rate_name = movie_name
    if movie_rate < min_rate:
        min_rate = movie_rate
        min_rate_name = movie_name
    total_score += movie_rate
average_rating = total_score / total_picked_movies

print(f'{max_rate_name} is with highest rating: {max_rate:.1f}')
print(f'{min_rate_name} is with lowest rating: {min_rate:.1f}')
print(f'Average rating: {average_rating:.1f}')
