line = input()
asci_code = ''
con_times = 0
c_times = 0
o_times = 0
n_times = 0
print_space = 0
main_word = ''
additional_word = ''
while line != 'End':
    asci_code = ord(line)
    if (65 <= asci_code <= 90 or 97 <= asci_code <= 122) and asci_code != 99 and asci_code != 110 and asci_code != 111:
        additional_word += line
    elif asci_code == 99 and c_times > 0:
        additional_word += line
    elif asci_code == 99:
        c_times += 1
        con_times += 1
        print_space += 1
    elif asci_code == 110 and n_times > 0:
        additional_word += line
    elif asci_code == 110:
        n_times += 1
        con_times += 1
        print_space += 1
    elif asci_code == 111 and o_times > 0:
        additional_word += line
    elif asci_code == 111:
        o_times += 1
        con_times += 1
        print_space += 1
    if print_space == 3:
        additional_word += ' '
        print_space = 0
    if con_times == 3:
        c_times = 0
        o_times = 0
        n_times = 0
        con_times = 0
        main_word += additional_word
        additional_word = ''
    line = input()
print(main_word)
