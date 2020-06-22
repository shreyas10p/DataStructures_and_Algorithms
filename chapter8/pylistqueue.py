class Queue(object):
    """docstring for Queue"""
    def __init__(self):
        super(Queue, self).__init__()
        self.pylist = list()

    def isEmpty(self):
        if(len(self.pylist) == 0):
            return True
        return False

    def length(self):
        return len(self.pylist)

    def enqueue(self,item):
        self.pylist.append(item)

    def dequeue(self):
        assert not self.isEmpty(),"operation cannot be performed"
        return self.pylist.pop(0)

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(29)
    itemA = queue.dequeue()
    itemB = queue.dequeue()
    print(itemA)
    print(itemB)
