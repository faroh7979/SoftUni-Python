total_words = int(input())
my_dict = {}

for current_pair in range(total_words):
    word = input()
    synonym = input()
    if word not in my_dict.keys():
        my_dict[word] = synonym
    else:
        my_dict[word] += f', {synonym}'
for key, value in my_dict.items():
    print(f'{key} - {value}')
