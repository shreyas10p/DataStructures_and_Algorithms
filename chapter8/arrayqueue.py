from .chapter2.array_name import Array

class Queue(object):
    """docstring for Queue"""
    def __init__(self, maxSize):
        super(Queue, self).__init__()
        self._count = 0
        self._front = 0
        self._back = maxSize -1
        self._aqueue = Array(maxSize)

    def isEmpty(self):
        if(len(self._aqueue)== 0):
            return True
        return False

    def isFull(self):
        return self._count == len(self._aqueue)

    def length(self):
        return self._count

    def enqueue(self,item):
        assert self.isFull(),"operation cannot be performed"
        maxSize = len(self._aqueue)
        self._back = ((self._back + 1)% maxSize)
        self._aqueue[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(),"Operation cannot be performed"
        element = self._aqueue[self._front]
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return element
