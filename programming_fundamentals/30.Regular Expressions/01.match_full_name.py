import re

names = input()
regex_pattern = r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b'
qualifying = re.findall(regex_pattern, names)
print(" ".join(qualifying))
