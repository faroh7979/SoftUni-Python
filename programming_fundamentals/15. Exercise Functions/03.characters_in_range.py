def characters_in_range(first, second):
    firs_char_ord = ord(first)
    second_char_ord = ord(second)
    for char in range(firs_char_ord + 1, second_char_ord):
        current_char = chr(char)
        print(current_char, end=' ')


first_char = input()
second_char = input()
characters_in_range(first_char, second_char)
