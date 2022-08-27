client_word = input()
length = len(client_word)

for i in range(length, 0, -1):
    print(client_word[i-1], end="")
