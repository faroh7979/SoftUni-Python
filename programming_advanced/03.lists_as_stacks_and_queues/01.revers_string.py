user_string = input()
reversed_list = []

for letter in user_string:
    reversed_list.append(letter)

print("".join(reversed_list[::-1]))
