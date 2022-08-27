period_of_calculations = int(input())
treated_patients = 0
untreated_patients = 0
total_medics = 7

for days in range(1, period_of_calculations + 1):
    patients_for_review = int(input())
    if days % 3 != 0:
        if patients_for_review <= total_medics:
            treated_patients += patients_for_review
        else:
            treated_patients += total_medics
            untreated_patients += patients_for_review - total_medics
    elif days % 3 == 0 and untreated_patients > treated_patients:
        total_medics += 1
        if patients_for_review <= total_medics:
            treated_patients += patients_for_review
        else:
            treated_patients += total_medics
            untreated_patients += patients_for_review - total_medics
    else:
        if patients_for_review <= total_medics:
            treated_patients += patients_for_review
        else:
            treated_patients += total_medics
            untreated_patients += patients_for_review - total_medics
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')
