employee_dict = {}

while True:
    command_line = input()
    if command_line == 'End':
        break
    company, employee_id = command_line.split(' -> ')
    if company not in employee_dict:
        employee_dict[company] = f', -- {employee_id}'
    else:
        if employee_id not in employee_dict[company]:
            employee_dict[company] += f', -- {employee_id}'
for key, value in employee_dict.items():
    converted_value = ("\n".join(employee_dict[key].split(', ')))
    print(key, end="")
    print(converted_value)

