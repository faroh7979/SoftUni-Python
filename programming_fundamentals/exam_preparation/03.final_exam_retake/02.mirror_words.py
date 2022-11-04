import re
competition_string = input()
mirror_list = []

competition_pattern = r'([@#]{1})([A-Za-z]{3,})\1(\1)([A-Za-z]{3,})\1'
final_match = re.findall(competition_pattern, competition_string)
total_matches = len(final_match)
for match in final_match:
    if match[1] == match[3][::-1]:
        mirror_list.append(f'{match[1]} <=> {match[3]}')
if total_matches == 0:
    print("No word pairs found!")
    print("No mirror words!")
else:
    print(f"{total_matches} word pairs found!")
    if len(mirror_list) == 0:
        print("No mirror words!")
    else:
        print('The mirror words are:')
        print(", ".join(mirror_list))
