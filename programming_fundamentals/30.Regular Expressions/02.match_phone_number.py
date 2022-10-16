import re

phones = input()
phone_pattern = r'\+359-2-[0-9]{3}-[0-9]{4}\b|\+359 2 [0-9]{3} [0-9]{4}\b'
valid_phones = re.findall(phone_pattern, phones)
print(', '.join(valid_phones))
