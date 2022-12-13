class countdown_iterator:
    def __init__(self, total_counts: int):
        self.total_counts = total_counts
        self.current = self.total_counts + 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.end:
            raise StopIteration

        self.current -= 1
        return self.current


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
