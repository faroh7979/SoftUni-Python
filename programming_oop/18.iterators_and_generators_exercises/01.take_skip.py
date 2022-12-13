class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.begin = 0 - self.step
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current_count == self.count:
            raise StopIteration

        self.current_count += 1
        self.begin += self.step
        return self.begin


numbers = take_skip(2, 6)
for number in numbers:
    print(number)
