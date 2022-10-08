from os import remove

file_path = './deleting_file.txt'

with open(file_path, 'w') as file:
    file.write('This is my new file for deleting')

remove(file_path)
try:
    remove(file_path)
except FileNotFoundError:
    print('File already deleted')
