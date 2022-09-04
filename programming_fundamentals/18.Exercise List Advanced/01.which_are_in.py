first_list = input().split(', ')
second_list = input().split(', ')
final_list = []

for current_word in first_list:
    for word in second_list:
        if current_word in word:
            final_list.append(current_word)
            break
print(final_list)
