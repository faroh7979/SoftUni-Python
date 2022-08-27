heritage = float(input())
year_to_be_live = int(input())
ages_ivan = 18
regular_yearly_expense = 12000
total_expense = 0

for years in range(1800, year_to_be_live + 1):
    if years % 2 == 0:
        total_expense += regular_yearly_expense
        ages_ivan += 1
    else:
        total_expense += regular_yearly_expense + 50 * ages_ivan
        ages_ivan += 1
difference = abs(heritage - total_expense)

if total_expense <= heritage:
    print(f'Yes! He will live a carefree life and will have {difference:.2f} dollars left.')
else:
    print(f'He will need {difference:.2f} dollars to survive.')
