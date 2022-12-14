def read_next(*args):
    counter = 0

    while counter < len(args):
        yield f"".join([str(el) for el in args[counter]])

        counter += 1


for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')
