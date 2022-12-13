class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.current_index = - 1
        self.length = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        self.current_index += 1
        if self.counter > self.number:
            raise StopIteration

        if self.current_index == self.length:
            self.current_index = 0

        return self.sequence[self.current_index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end ='')
