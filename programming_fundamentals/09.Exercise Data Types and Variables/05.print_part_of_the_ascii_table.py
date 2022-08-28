start_ascii = int(input())
end_ascii = int(input())

for current_char in range(start_ascii, end_ascii + 1):
    current_symbol = chr(current_char)
    print(current_symbol, end=' ')
