from collections import deque


class dictionary_iter:
    def __init__(self, my_dict: dict):
        self.my_dict = my_dict
        self.list = deque([(k, v) for k, v in self.my_dict.items()])

    def __iter__(self):
        return self

    def __next__(self):

        if not self.list:
            raise StopIteration

        return self.list.popleft()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
