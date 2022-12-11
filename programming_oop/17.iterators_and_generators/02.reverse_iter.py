class reverse_iter:
    def __init__(self, iter_obj):
        self.iter_obj = iter_obj
        self.index = len(iter_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration

        self.index -= 1
        return self.iter_obj[self.index]


reversed_list = reverse_iter("python")
for item in reversed_list:
    print(item)
