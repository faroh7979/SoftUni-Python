number_of_pairs = int(input())
longest_pair = set()

for _ in range(number_of_pairs):
    first_pair, second_pair = input().split('-')

    first_pair_begin, first_pair_end = first_pair.split(',')
    second_pair_begin, second_pair_end = second_pair.split(',')

    first_pair_collection = set()
    second_pair_collection = set()

    for value in range(int(first_pair_begin), int(first_pair_end) + 1):  # the value is inclusive
        first_pair_collection.add(value)

    for value in range(int(second_pair_begin), int(second_pair_end) + 1):  # the value is inclusive
        second_pair_collection.add(value)

    intersection_set = first_pair_collection.intersection(second_pair_collection)

    if len(intersection_set) > len(longest_pair):
        longest_pair = intersection_set

longest_pair_length = len(longest_pair)
# should be printed with quad brackets, that is the reason for casting to list of {longest_pair}
print(f'Longest intersection is {list(longest_pair)} with length {longest_pair_length}')
