class SortedBag(object):
    """docstring for SortedBag"""
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self,item):
        curNode = self._head
        while(curNode is not None and curNode._data != item):
            curNode = curNode._next
        return curNode is not None

    def add(self,target):
        curNode = self._head
        preNode = None
        targetObj = _BagListNode(target)
        while(curNode is not None and curNode._data < target):
            preNode = curNode
            curNode = curNode._next
        targetObj._next = curNode
        if curNode is self._head:
            self._head = targetObj
        else:
            preNode._next = targetObj
        self._size +=1

    def remove(self,target):
        assert target in self,"element must be in the bag"
        preNode = None
        curNode = self._head
        while(curNode is not None and curNode._data != target):
            preNode = curNode
            curNode = curNode._next
        nextNode = curNode._next
        if preNode is None:
            self._head = nextNode
        else:
            preNode._next = nextNode
        self._size -= 1

    def __iter__(self):
        return _BagIterator(self._head)

# An iterator for the Bag ADT implemented as a Python list.
class _BagIterator :
    def __init__( self, theList ):
        self._bagItems = theList

    def __iter__( self ):
        return self

    def next( self ):
        if(self._bagItems is not None):
            item = self._bagItems._data
            self._bagItems = self._bagItems._next
            return item
        else:
            raise StopIteration


class _BagListNode(object):
    """docstring for _"""
    def __init__(self, data):
        self._data = data
        self._next = None


if __name__ == '__main__':
    sortedBag = SortedBag()
    sortedBag.add(2)
    sortedBag.add(4)
    sortedBag.add(3)
    sortedBag.add(5)
    for x in sortedBag:
        print(x)
