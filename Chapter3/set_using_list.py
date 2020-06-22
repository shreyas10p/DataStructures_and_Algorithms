class Set(object):
    """docstring for Set"""
    def __init__(self, arg):
        self._theElements = list()

    def __length__(self):
        return len(self._theElements)

    # Determines if an item is contained in the set.
    def __contains__( self, item ):
        return item in self._theElements

    def add(self,element):
        if element not in self._theElements:
            self._theElements.append(element)

    def remove(self,element):
        assert element in self._theElements, "Element must be present in set"
        idx = self._theElements.index(element)
        return self._theElements.pop(idx)

    def __eq__(self,setB):
        if len(self) != len(setB):
            return False
        else:
            return self.isSubsetOf( setB )

    def isSubsetOf(self,setB):
        for element in self._theElements:
            if element not in setB:
                return False

        return True

    def union(self,setB):
        newSet = Set()
        newSet._theElements.extend(self._theElements)
        for element in setB:
            if element not in self._theElements:
                newSet.append(element)
        return newSet

    def __iter__(self):
        return _SetIterator(self._theElements)

# An iterator for the Set ADT implemented as a Python list.
class _SetIterator :
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
