client_word = input()
length = len(client_word)
my_list = []

for index in range(length):
    if client_word[index].isupper():
        my_list.append(index)
print(my_list)
