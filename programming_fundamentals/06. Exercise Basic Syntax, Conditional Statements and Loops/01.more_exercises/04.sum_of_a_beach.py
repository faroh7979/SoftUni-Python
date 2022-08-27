client_string = input()
client_string_lower = client_string.lower()
key_words_num = client_string_lower.count('water', 0, 22222222) +\
    client_string_lower.count('sand', 0, 22222222) +\
    client_string_lower.count('fish', 0, 22222222) +\
    client_string_lower.count('sun', 0, 22222222)
print(key_words_num)
