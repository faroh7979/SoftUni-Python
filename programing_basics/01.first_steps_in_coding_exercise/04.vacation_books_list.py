total_book_pages = int(input())
pages_an_hour = int(input())
days_to_read = int(input())

needable_hours = total_book_pages // days_to_read
needed_daily_hours = needable_hours // pages_an_hour

print(needed_daily_hours)
