total_names = int(input())
all_names = []

for _ in range(total_names):
    name = input()
    all_names.append(name)

unique_names = set(all_names)

for unique_name in unique_names:
    print(unique_name)
