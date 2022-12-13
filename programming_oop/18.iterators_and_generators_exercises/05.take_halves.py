from sys import maxsize


def solution():

    def integers():
        current_num = 1

        while current_num < maxsize:
            yield current_num
            current_num += 1

    def halves():

        for i in integers():
            yield i / 2

    def take(n, seq):
        current_count = 1
        while current_count < n:
            yield halves()
            current_count += 1

    return (take, halves, integers)


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
