from .Chapter2.linearbag import Bag

class BagSet(object):
    """docstring for BagSet"""
    def __init__(self, arg):
        self._Bag = Bag()

    def __length__(self):
        return len(self._Bag)

    def __contains__(item,self):
        return item in self._Bag

    def add(item,self):
        if item not in self._Bag:
            self._Bag.add(item)

    def remove(item,self):
        assert item in self._Bag,"Item not in Bag"
        ndx = self._theItems.index( item )
        return self._theItems.pop( ndx )

    def __iter__(self):
        return _BagIterator(self._theItems)

# An iterator for the Bag ADT implemented as a Python list.
class _BagIterator :
    def __init__( self, theList ):
        self._bagItems = theList
        self._curItem = 0

    def __iter__( self ):
        return self

    def __next__( self ):
        if self._curItem < len( self._bagItems ) :
            item = self._bagItems[ self._curItem ]
            self._curItem += 1
            return item
        else :
            raise StopIteration



