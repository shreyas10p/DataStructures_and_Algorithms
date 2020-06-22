from array_name import Array

class Array2D:
    """docstring for Array2D"""
    def __init__(self, numRows,numCols):
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    # def __len__(self):
    #     return

    def __repr__(self):
        return str(self._theRows)

    def clear(self,value):
        for row in range(self.numRows()):
            for col in range(self.numCols()):
                self[row,col] = value

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def __getitem__(self,ndxTuple):
        assert len(ndxTuple) == 2,"Invalid Number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row>=0 and row<len(self._theRows),"Not a valid row index"
        assert col>=0 and col<len(self._theRows[0]),"Not a valid column index"
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self,ndxTuple,value):
        assert len(ndxTuple) == 2,"Invalid Number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row>=0 and row<len(self._theRows),"Not a valid row index"
        assert col>=0 and col<len(self._theRows[0]),"Not a valid column index"
        the1dArray = self._theRows[row]
        the1dArray[col] =value


class _ArrayIterator(object):
    """docstring for _ArrayIterator"""
    def __init__(self, theArray):
        super(_ArrayIterator, self).__init__()
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


if __name__ == '__main__':
    array2d = Array2D(2,3)
    array2d[0,1] = 56
    array2d[0,2] = 1
    print(array2d[0,1])
    print(array2d[0,0])
    print(array2d)
    for x in range(array2d.numRows()):
        print(array2d[x,1])
