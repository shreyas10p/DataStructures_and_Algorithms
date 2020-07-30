import ctypes

class Array(object):
    """docstring for Array"""
    def __init__(self, size):
        assert size>0,"Array must be greater than 0"
        self.size = size
        arrayType = ctypes.py_object*size
        self._slots = arrayType()
        self.clear(None)

    def __repr__(self):
        return str(self._slots)

    def __len__(self):
        return self.size

    def __getitem__(self,index):
        assert index >=0 and index < len(self),"Index Not in range"
        return self._slots[index]

    def __setitem__(self,index,value):
        assert index >=0 and index < len(self),"Index Not in range"
        self._slots[index] = value

    def clear(self,value):
        for element in range(len(self)):
            self._slots[element]=value

    def __iter__(self):
        return _ArrayIterator(self._slots)

class _ArrayIterator(object):
    """docstring for _ArrayIterator"""
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__( self ):
        if self._curNdx < len( self._arrayRef ) :
            entry = self._arrayRef[ self._curNdx ]
            self._curNdx += 1
            return entry
        else :
            raise StopIteration


