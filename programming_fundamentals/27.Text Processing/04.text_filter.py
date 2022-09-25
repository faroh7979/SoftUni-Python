banned_words = input()
banned_words_list = banned_words.split(', ')
current_text = input()

for element in banned_words_list:
    current_length = len(element)
    current_text = current_text.replace(element, f'{"*" * current_length}')

print(current_text)
