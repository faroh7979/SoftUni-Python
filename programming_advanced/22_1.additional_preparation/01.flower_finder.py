from collections import deque

vowels = deque([i for i in input().split()])
consonants = [i for i in input().split()]

searched_word = [
    "rose",
    "tulip",
    "lotus",
    "daffodil"
]

searched_word_copy = searched_word.copy()

founded_word = False
while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for current_index in range(len(searched_word)):
        searched_word[current_index] = searched_word[current_index].replace(vowel, '')
        searched_word[current_index] = searched_word[current_index].replace(consonant, '')

    if '' in searched_word:
        founded_word = True
        break

if founded_word:
    the_word = ''
    for inx in range(len(searched_word_copy)):
        if searched_word[inx] == '':
            the_word = searched_word_copy[inx]
            break

    print(f'Word found: {the_word}')

else:
    print("Cannot find any word!")

if vowels:
    print(f'Vowels left: {" ".join(vowels)}')

if consonants:
    print(f'Consonants left: {" ".join(consonants)}')
