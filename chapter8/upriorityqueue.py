class PriorityQueue(object):
    """docstring for PriorityQueue"""
    def __init__(self):
        super(PriorityQueue, self).__init__()
        self._lqueue =list()

    def isEmpty(self):
        return len(self._lqueue) == 0

    def length(self):
        return len(self._lqueue)

    def enqueue(self,item,priority):
        node = _QueueNode(item,priority)
        self._lqueue.append(node)

    def dequeue(self):
        assert not self.isEmpty(),"Operation cannot be performed"
        high = self._lqueue[0]._priority
        qList = self._lqueue
        hIndex = 0
        for i in range(self.length()):
            if(qList[i]._priority > high):
                high = qList[i]._priority
                hIndex = i
        item = qList.pop(hIndex)
        return item._item



class _QueueNode(object):
    """docstring for _QueueNode"""
    def __init__(self, item,priority):
        super(_QueueNode, self).__init__()
        self._item = item
        self._priority = priority

if __name__ == '__main__':
    uqueue = PriorityQueue()
    uqueue.enqueue("purple",5)
    uqueue.enqueue("black",1)
    uqueue.enqueue( "orange", 3 )
    uqueue.enqueue( "white", 0 )
    uqueue.enqueue( "green", 1 )
    uqueue.enqueue( "yellow", 5 )
    print(uqueue.dequeue())
    print(uqueue.dequeue())
