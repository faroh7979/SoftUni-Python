import re

sentence = input()
searched_word = input()
word_pattern = fr'\b{searched_word}\b'
word_raw_list = re.findall(word_pattern, sentence, flags=re.I)
print(len(word_raw_list))
