total_snowballs = int(input())
total_score = 0
final_weight = 0
final_time = 0
final_quality = 0

for _ in range(total_snowballs):
    weight_snowballs = int(input())
    time_snowballs = int(input())
    quality_snowballs = int(input())
    current_score = (weight_snowballs / time_snowballs) ** quality_snowballs
    if current_score > total_score:
        final_weight = weight_snowballs
        final_time = time_snowballs
        final_quality = quality_snowballs
        total_score = current_score
print(f"{final_weight} : {final_time} = {total_score:.0f} ({final_quality})")
