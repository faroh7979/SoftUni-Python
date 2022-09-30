text = input()
emoticon_string = []
total_emoticons = text.count(':')
start_index = 0

for current_emoticon in range(total_emoticons):
    current_index = text.index(':', start_index)
    emoticon_string.append(text[current_index] + text[current_index + 1])
    start_index = current_index + 1

print('\n'.join(emoticon_string))
