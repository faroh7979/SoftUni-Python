movie_name = input()
available_sits = ''
ticket_type = ''
total_sold_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
while movie_name != 'Finish':
    sold_tickets = 0
    available_sits = int(input())
    while sold_tickets < available_sits:
        ticket_type = input()
        if ticket_type == 'End':
            break
        sold_tickets += 1
        if ticket_type == 'student':
            student_tickets += 1
        elif ticket_type == 'standard':
            standard_tickets += 1
        elif ticket_type == 'kid':
            kid_tickets += 1
    percentage_sold = sold_tickets / available_sits * 100
    print(f'{movie_name} - {percentage_sold:.2f}% full.')
    movie_name = input()
total_sold_tickets = student_tickets + standard_tickets + kid_tickets
student_percentage = student_tickets / total_sold_tickets * 100
standard_percentage = standard_tickets / total_sold_tickets * 100
kid_percentage = kid_tickets / total_sold_tickets * 100
print(f'Total tickets: {total_sold_tickets}')
print(f'{student_percentage:.2f}% student tickets.')
print(f'{standard_percentage:.2f}% standard tickets.')
print(f'{kid_percentage:.2f}% kids tickets.')
