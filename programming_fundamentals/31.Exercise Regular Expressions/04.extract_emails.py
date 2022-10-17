import re
line_info = input()

info_pattern = r'(?<=\s)([A-Za-z]{1}[A-za-z0-9\_\-\.]+@[A-Za-z]{1}[A-Za-z\-]*(\.[A-Za-z]{1}[A-Za-z\-]*)+)'
all_emails = re.findall(info_pattern, line_info)
for email in all_emails:
    print(email[0])
