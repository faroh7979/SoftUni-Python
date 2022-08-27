customer_numbers = int(input())
total_divided_2 = 0
total_divided_3 = 0
total_divided_4 = 0

for iteration in range(customer_numbers):
    current_number = int(input())
    if current_number % 2 == 0:
        total_divided_2 += 1
    if current_number % 3 == 0:
        total_divided_3 += 1
    if current_number % 4 == 0:
        total_divided_4 += 1
percentage_divided_by_2 = total_divided_2 / customer_numbers * 100
percentage_divided_by_3 = total_divided_3 / customer_numbers * 100
percentage_divided_by_4 = total_divided_4 / customer_numbers * 100
print(f'{percentage_divided_by_2:.2f}%')
print(f'{percentage_divided_by_3:.2f}%')
print(f'{percentage_divided_by_4:.2f}%')
