class Counter(object):
    """docstring for Counter"""
    def __init__(self):
        super(Counter, self).__init__()
        self._counter = 0

    def push(self):
        self._counter += 1

    def reset(self):
        self._counter = 0

if __name__ == '__main__':
    counter = Counter()
    counter.push()
    print(counter._counter)
    counter.push()
    print(counter._counter)
    counter.reset()
    print(counter._counter)
