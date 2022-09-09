book_shelf = input()
book_shelf_list = book_shelf.split('&')

while True:
    line = input()
    if line == 'Done':
        break
    command_type = line.split(' | ')
    book_command = command_type[0]
    if book_command == 'Add Book':
        book_name = command_type[1]
        book_counter = book_shelf_list.count(book_name)
        if book_counter > 0:
            continue
        else:
            book_shelf_list.insert(0, book_name)
    elif book_command == 'Take Book':
        book_name = command_type[1]
        book_counter = book_shelf_list.count(book_name)
        if book_counter < 1:
            continue
        else:
            book_shelf_list.remove(book_name)
    elif book_command == 'Swap Books':
        first_book = command_type[1]
        second_book = command_type[2]
        if first_book in book_shelf_list and second_book in book_shelf_list:
            first_book_index = book_shelf_list.index(first_book)
            second_book_index = book_shelf_list.index(second_book)
            book_shelf_list[first_book_index], book_shelf_list[second_book_index] = \
                book_shelf_list[second_book_index], book_shelf_list[first_book_index]
    elif book_command == 'Insert Book':
        book_name = command_type[1]
        book_counter = book_shelf_list.count(book_name)
        if book_counter > 0:
            continue
        else:
            book_shelf_list.append(book_name)
    elif book_command == 'Check Book':
        book_index = int(command_type[1])
        total_book_index = len(book_shelf_list) - 1
        if book_index < 0 or book_index > total_book_index:
            continue
        else:
            print(book_shelf_list[book_index])
print(', '.join(book_shelf_list))
