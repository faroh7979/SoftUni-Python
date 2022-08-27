actor_name = input()
starting_academy_point = float(input())
total_judges = int(input())
total_actor_points = 0 + starting_academy_point

for i in range(total_judges):
    judge_name = input()
    points_by_judge = float(input())
    judge_given_points = len(judge_name) * points_by_judge / 2
    total_actor_points += judge_given_points
    if total_actor_points > 1250.5:
        break
if total_actor_points > 1250.5:
    print(f'Congratulations, {actor_name} got a nominee for leading role with {total_actor_points:.1f}!')
else:
    difference = 1250.5 - total_actor_points
    print(f'Sorry, {actor_name} you need {difference:.1f} more!')
