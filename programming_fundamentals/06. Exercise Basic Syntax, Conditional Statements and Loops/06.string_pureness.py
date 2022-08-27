num_of_strings = int(input())

for _ in range(num_of_strings):
    current_string = input()
    is_pure = True
    for char in current_string:
        if ord(char) == 95 or ord(char) == 46 or ord(char) == 44:
            print(f'{current_string} is not pure!')
            is_pure = False
            break
    if is_pure:
        print(f"{current_string} is pure.")
