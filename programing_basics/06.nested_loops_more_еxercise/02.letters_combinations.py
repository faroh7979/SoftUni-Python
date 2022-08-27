interval_start = input()
interval_end = input()
missing_letter = input()

asci_start = ord(interval_start)
asci_end = ord(interval_end)
asci_missing = ord(missing_letter)
total_prints = 0

for first_letter in range(asci_start, asci_end + 1):
    if first_letter == asci_missing:
        continue
    for second_letter in range(asci_start, asci_end + 1):
        if second_letter == asci_missing:
            continue
        for third_letter in range(asci_start, asci_end + 1):
            if third_letter == asci_missing:
                continue
            print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end=" ")
            total_prints += 1
print(total_prints)
