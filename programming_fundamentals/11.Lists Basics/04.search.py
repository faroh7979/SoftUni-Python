total_strings = int(input())
key_word = input()
whole_list = []
keyword_list = []

for _ in range(total_strings):
    current_string = input()
    whole_list.append(current_string)
    if key_word in current_string:
        keyword_list.append(current_string)
print(whole_list)
print(keyword_list)