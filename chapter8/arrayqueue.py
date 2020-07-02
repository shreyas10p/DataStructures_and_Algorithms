# from .chapter2.array_name import Array

class Queue(object):
    """docstring for Queue"""
    def __init__(self, maxSize):
        super(Queue, self).__init__()
        self._count = 0
        self._front = 0
        self._back = maxSize -1
        self._aqueue = Array(maxSize)

    def __repr__(self):
        reprStr = ""
        for i in range(self.length()):
            reprStr += " "+str(self._aqueue[i])
        return reprStr

    def isEmpty(self):
        if(self._count == 0):
            return True
        return False

    def isFull(self):
        return self._count == len(self._aqueue)

    def length(self):
        return self._count

    def enqueue(self,item):
        assert not self.isFull(),"operation cannot be performed"
        maxSize = len(self._aqueue)
        self._back = ((self._back + 1)% maxSize)
        self._aqueue[self._back] = item
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(),"Operation cannot be performed"
        element = self._aqueue[self._front]
        maxSize = len(self._aqueue)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return element

    def reverse(self):
        stack = []
        while(self._count!=0):
            print(self.isEmpty())
            stack.append(self.dequeue())

        while(len(stack)!=0):
            ele = stack.pop()
            self.enqueue(ele)


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

        from Chapter2.array import Array
    else:
        from ..Chapter2.array import Array

    queue = Queue(6)
    queue.enqueue(5)
    queue.enqueue(1)
    queue.enqueue(3)
    queue.enqueue(0)
    queue.enqueue(1)
    queue.enqueue(5)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.reverse()
    print(queue.dequeue())
