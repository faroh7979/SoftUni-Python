def even_odd(*args):
    command = args[-1]
    even_list = [i for i in args[:-1] if i % 2 == 0]
    odd_list = [i for i in args[:-1] if i % 2 != 0]

    if command == 'even':
        return even_list
    elif command == 'odd':
        return odd_list



