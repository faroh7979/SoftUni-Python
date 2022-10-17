import re

url_pattern = r'(www.[A-Za-z0-9]{1}[A-Za-z0-9\-]*(\.[a-z]+)+)'
url_list = []

while True:
    command = input()
    if not command:
        break
    valid_url = re.search(url_pattern, command)
    if valid_url:
        url_list.append(valid_url[0])
print('\n'.join(url_list))
