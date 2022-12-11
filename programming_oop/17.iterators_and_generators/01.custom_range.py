class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.counter = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter > self.end:
            raise StopIteration

        self.counter += 1
        return self.counter - 1


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
