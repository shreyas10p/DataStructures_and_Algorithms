class Bag(object):
    """docstring for Bag"""
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self,target):
        curNode = self._head
        while(curNode is not None and curNode._data != target):
            curNode = curNode._next
        return curNode is not None

    def add(self,ele):
        curNode = self._head
        newNode = _BagListNode(ele,curNode)
        self._head = newNode
        self._size += 1

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
    """docstring for _BagListNode"""
    def __init__(self, data,next):
        super(_BagListNode, self).__init__()
        self._data = data
        self._next = next


if __name__ == '__main__':
    bag = Bag()
    bag.add(4)
    bag.add(6)
    bag.add(8)
    bag.add(10)
    bag.add(12)
    bag.add(14)
    bag.remove(10)
    bag.remove(14)
    for x in bag:
        print(x)

