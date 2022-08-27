total_groups = int(input())
musala_peak = 0
montblanc_peak = 0
kilimanjaro_peak = 0
k2_peak = 0
everest_peak = 0
total_participants = 0
for group in range(total_groups):
    participants = int(input())
    if participants <= 5:
        musala_peak += participants
    elif participants <= 12:
        montblanc_peak += participants
    elif participants <= 25:
        kilimanjaro_peak += participants
    elif participants <= 40:
        k2_peak += participants
    elif participants > 40:
        everest_peak += participants
    total_participants += participants
musala_peak_percentage = musala_peak / total_participants * 100
montblanc_peak_percentage = montblanc_peak / total_participants * 100
kilimanjaro_peak_percentage = kilimanjaro_peak / total_participants * 100
k2_peak_percentage = k2_peak / total_participants * 100
everest_peak_percentage = everest_peak / total_participants * 100
print(f'{musala_peak_percentage:.2f}%')
print(f'{montblanc_peak_percentage:.2f}%')
print(f'{kilimanjaro_peak_percentage:.2f}%')
print(f'{k2_peak_percentage:.2f}%')
print(f'{everest_peak_percentage:.2f}%')
