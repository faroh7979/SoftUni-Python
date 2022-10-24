import re

total_inputs = int(input())
validation_pattern = r'(^[\$\%])([A-Z]{1}[a-z]{2,})\1: \[(\d+)\]\|\[(\d+)\]\|\[(\d+)\]\|$'
validation_list = []

for current_input in range(total_inputs):
    validation_text = input()
    validation_string = re.findall(validation_pattern, validation_text)
    validation_list.append(validation_string)

for element in validation_list:
    if element:
        decryption_message = ''
        decryption_message += chr(int(element[0][2])) + chr(int(element[0][3])) + chr(int(element[0][4]))
        print(f"{element[0][1]}: {decryption_message}")
    else:
        print('Valid message not found!')
