first_game_result = input()
second_game_result = input()
third_game_result = input()

won = 0
drawn = 0
lost = 0

if first_game_result [-3] > first_game_result [-1]:
    won = won + 1
elif first_game_result [-3] == first_game_result [-1]:
    drawn = drawn + 1
else:
    lost = lost + 1

if second_game_result [-3] > second_game_result [-1]:
    won = won + 1
elif second_game_result [-3] == second_game_result [-1]:
    drawn = drawn + 1
else:
    lost = lost + 1

if third_game_result [-3] > third_game_result [-1]:
    won = won + 1
elif third_game_result [-3] == third_game_result [-1]:
    drawn = drawn + 1
else:
    lost = lost + 1

print(f"Team won {won} games.")
print(f"Team lost {lost} games.")
print(f"Drawn games: {drawn}")

