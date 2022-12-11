from collections import deque


class vowels:
    VOWELS = ['a', 'e', 'i', 'u', 'y', 'o']

    def __init__(self, iterable: str):
        self.iterable = iterable
        self.new_str = deque([v for v in self.iterable if v.lower() in self.VOWELS])

    def __iter__(self):
        return self

    def __next__(self):
        if not self.new_str:
            raise StopIteration

        return self.new_str.popleft()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
