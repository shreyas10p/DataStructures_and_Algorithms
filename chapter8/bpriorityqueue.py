from .Chapter2.array import Array
from llistqueue import Queue

#Bounded Priority Queue
class BPriorityQueue(object):
    """docstring for BPriorityQueue"""
    def __init__(self, arg,maxSize):
        super(BPriorityQueue, self).__init__()
        self._qsize = 0
        self._qArray = Array(maxSize)
        for i in range(maxSize):
            self._qArray[i] = Queue()

    def isEmpty(self):
        return len(self._qArray) == 0

    def __len__(self):
        return self._qsize

    def enqueue(self,item,priority):
        self._qArray[priority].enqueue(item)
        self._qsize += 1

    def dequeue(self):
        assert self._qsize!=0,"Operation cannot be performed"
        i=0
        p = len(self._qArray)
        while i<p and not self._qArray[i].isEmpty():
            i+=1

        return self._qArray[i].dequeue()

if __name__ == '__main__':
    uqueue = BPriorityQueue(6)
    uqueue.enqueue("purple",5)
    uqueue.enqueue("black",1)
    uqueue.enqueue( "orange", 3 )
    uqueue.enqueue( "white", 0 )
    uqueue.enqueue( "green", 1 )
    uqueue.enqueue( "yellow", 5 )
    print(uqueue.dequeue())
    print(uqueue.dequeue())
