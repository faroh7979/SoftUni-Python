string_nums = int(input())
my_string = ''
is_balanced = True

for string in range(1, string_nums + 1):
    current_string = input()
    my_string += current_string
open_bracket_count = my_string.count(chr(40))
closed_bracket_count = my_string.count(chr(41))
open_bracket_position = my_string.find(chr(40))
closed_bracket_position = my_string.find(chr(41))
start_searching = 0
end_searching = len(str(my_string))

if open_bracket_count != closed_bracket_count:
    is_balanced = False
    print('UNBALANCED')
else:
    for _ in range(open_bracket_count):
        open_bracket_position = my_string.find(chr(40), start_searching, end_searching)
        closed_bracket_position = my_string.find(chr(41), start_searching, end_searching)
        if closed_bracket_position < open_bracket_position:
            is_balanced = False
            print('UNBALANCED')
            break
        if my_string[open_bracket_position] == my_string[open_bracket_position + 1]:
            is_balanced = False
            print('UNBALANCED')
            break
        if closed_bracket_position == len(my_string) - 1:
            continue
        else:
            if my_string[closed_bracket_position] == my_string[closed_bracket_position + 1]:
                is_balanced = False
                print('UNBALANCED')
                break
        start_searching = closed_bracket_position + 1
if is_balanced:
    print('BALANCED')
