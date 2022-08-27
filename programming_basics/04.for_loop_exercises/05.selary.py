total_open_tabs = int(input())
salary = float(input())
fine = 0
rested_salary = 0
for tabs in range(total_open_tabs):
    website_name = input()
    if website_name == 'Facebook':
        fine += 150
    elif website_name == 'Instagram':
        fine += 100
    elif website_name == 'Reddit':
        fine += 50
    rested_salary = salary - fine
    if rested_salary <= 0:
        break
if rested_salary <= 0:
    print('You have lost your salary.')
else:
    print(f'{rested_salary:.0f}')
