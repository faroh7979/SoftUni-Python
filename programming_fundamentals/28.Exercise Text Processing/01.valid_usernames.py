usernames = input()
usernames_list = usernames.split(', ')
valid_usernames = []

for username in usernames_list:
    if len(username) < 3 or len(username) > 16:
        continue
    if not username.replace('-', 'a').replace('_', 'a').isalnum():
        continue
    valid_usernames.append(username)

print("\n".join(valid_usernames))
