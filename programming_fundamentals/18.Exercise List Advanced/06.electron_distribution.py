num_electrons = int(input())
shell_list = []
for shell_position in range(1, num_electrons + 1):
    current_needed_shells = 2 * shell_position ** 2
    if current_needed_shells <= num_electrons:
        shell_list.append(current_needed_shells)
        num_electrons -= current_needed_shells
    else:
        if num_electrons == 0:
            break
        else:
            shell_list.append(num_electrons)
            break
print(shell_list)
