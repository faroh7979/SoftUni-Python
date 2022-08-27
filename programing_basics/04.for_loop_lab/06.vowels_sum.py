text = input()
text_len = len(text)
points = 0

for i in range(0, text_len):
    if text[i] == 'a' or text[i] == 'A':
        points += 1
    elif text[i] == 'e' or text[i] == 'E':
        points += 2
    elif text[i] == 'i' or text[i] == 'I':
        points += 3
    elif text[i] == 'o' or text[i] == 'O':
        points += 4
    elif text[i] == 'u' or text[i] == 'U':
        points += 5
print(points)
