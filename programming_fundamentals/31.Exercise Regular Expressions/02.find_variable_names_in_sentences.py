from re import findall

string_line = input()
name_pattern = r'\b_([A-Z,a-z,0-9]+)\b'

variable_names = findall(name_pattern, string_line)
print(','.join(variable_names))
