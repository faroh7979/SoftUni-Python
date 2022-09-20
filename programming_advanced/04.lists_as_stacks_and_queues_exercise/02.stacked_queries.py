total_queries = int(input())
my_stack = []

for _ in range(total_queries):
    query = input().split()
    query_type = query[0]

    if query_type == '1':
        number_to_add = int(query[1])
        my_stack.append(number_to_add)

    elif query_type == '2':
        if my_stack:
            my_stack.pop()

    elif query_type == '3':
        if my_stack:
            print(max(my_stack))

    elif query_type == '4':
        if my_stack:
            print(min(my_stack))

final_list = []
for _ in range(len(my_stack)):
    current_reversed_element = my_stack.pop()
    final_list.append(current_reversed_element)

print(* final_list, sep=', ')
