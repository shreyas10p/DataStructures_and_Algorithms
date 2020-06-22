class Queue(object):
    """docstring for Queue"""
    def __init__(self):
        super(Queue, self).__init__()
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self):
        return self._head is None

    def length(self):
        return self._size

    def enqueue(self,item):
        node = _QueueNode(item)
        if(self.isEmpty()):
            self._head = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        assert self._size>0,"Operation cannot be performed"
        node = self._head
        self._head = self._head._next
        if(self._head is self._tail):
            self._tail = None
        self._size -= 1
        return node._item



class _QueueNode(object):
    """docstring for _QueueNode"""
    def __init__(self, item):
        super(_QueueNode, self).__init__()
        self._item = item
        self._next = None


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(90)
    queue.enqueue(89)
    queue.enqueue(50)
    queue.enqueue(89)
    eleA = queue.dequeue()
    eleB = queue.dequeue()
    print(eleA)
    print(eleB)
    queueB = Queue()
    queueB.enqueue(50)
    eleC = queueB.dequeue()
    # eleB = queue.dequeue()
    print(eleC)
    queueB.enqueue(10)
    queueB.enqueue(90)
    queueB.enqueue(100)
    print(queueB.dequeue())
