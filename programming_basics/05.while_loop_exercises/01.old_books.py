favorite_book = input()
current_book = input()
total_searches = 0
is_founded = True

while favorite_book != current_book:
    if current_book == 'No More Books':
        is_founded = False
        break
    total_searches += 1
    current_book = input()
if is_founded:
    print(f'You checked {total_searches} books and found it.')
else:
    print('The book you search is not here!')
    print(f'You checked {total_searches} books.')
