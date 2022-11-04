import re

total_barcodes = int(input())

for barcode in range(total_barcodes):
    line_barcode = input()
    current_pattern = r'^@#+[A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1}@#+$'
    current_barcode = re.findall(current_pattern, line_barcode)
    current_string = ''
    if current_barcode:
        for letter in current_barcode[0]:
            if letter.isdigit():
                current_string += letter
        if current_string:
            print(f'Product group: {current_string}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
