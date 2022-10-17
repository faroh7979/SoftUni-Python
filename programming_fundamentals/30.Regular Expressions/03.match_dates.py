import re

date_input = input()
date_pattern =\
    r'[0-9]{2}\.[A-Z]{1}[a-z]{2}\.\d{4}\b|[0-9]{2}-[A-Z]{1}[a-z]{2}-\d{4}\b|[0-9]{2}/[A-Z]{1}[a-z]{2}/\d{4}\b'
my_list = re.findall(date_pattern, date_input)
for element in my_list:
    if "/" in element:
        day, month, year = element.split('/')
    elif "." in element:
        day, month, year = element.split('.')
    elif "-" in element:
        day, month, year = element.split('-')
    print(f'Day: {day}, Month: {month}, Year: {year}')
