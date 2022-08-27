first_word = input()
second_word = input()
new_word = ''
length = len(first_word)
key_word = ''

for index in range(length):
    new_word = key_word
    if first_word[index] != second_word[index]:
        new_word += second_word[index]
        for third_index in range(index + 1, length):
            new_word += first_word[third_index]
        print(new_word)
        key_word += new_word[index]
    else:
        key_word += first_word[index]