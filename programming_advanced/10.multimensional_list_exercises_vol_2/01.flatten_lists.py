string_matrix = input().split('|')

final_list = []

for sublist in string_matrix[::-1]:
    final_list.extend(sublist.split())

print(" ".join(final_list))
