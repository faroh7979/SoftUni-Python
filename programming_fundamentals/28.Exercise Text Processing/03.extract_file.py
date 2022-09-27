file_path = input()
file_path_list = file_path.split("\\")
last_element = file_path_list[-1]
file_name, file_extensions = last_element.split('.')
print(f'File name: {file_name}')
print(f'File extension: {file_extensions}')
