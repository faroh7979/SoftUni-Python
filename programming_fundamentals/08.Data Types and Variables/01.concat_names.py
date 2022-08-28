first_string = input()
second_string = input()
third_string = input()
first = first_string.isalpha()
second = second_string.isalpha()
third = third_string.isalpha()

if first and second:
    print(f'{first_string}{third_string}{second_string}')
elif first and third:
    print(f'{first_string}{second_string}{third_string}')
elif second and third:
    print(f'{second_string}{first_string}{third_string}')