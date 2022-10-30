output = '''Go to University
28.05.2020
Don't forget laptop and notebook
Name: Go to University - Due Date: 28.05.2020
Task Name: Go to University - Due Date: 28.05.2020 is added to the section
Cleared 0 tasks.
Section Daily tasks:
Name: Go to University - Due Date: 28.05.2020
Name: Make bed - Due Date: 27/05/2020'''


expcted_output = '''Go to University
28.05.2020
Don't forget laptop and notebook
Name: Go to University - Due Date: 28.05.2020
Task Name: Go to University - Due Date: 28.05.2020 is added to the section
Cleared 0 tasks.
Section Daily tasks:
Name: Go to University - Due Date: 28.05.2020
Name: Make bed - Due Date: 27/05/2020'''

# for current_index in range(len(expcted_output)):
#     if output[current_index] != expcted_output[current_index]:
#         print(current_index)

print(expcted_output == output)
