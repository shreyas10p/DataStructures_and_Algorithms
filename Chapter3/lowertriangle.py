from .Chapter2.array import Array

class TriangleArray(object):
    """docstring fos """
    def __init__(self, nrows, ncols):
        assert nrows == ncols,"Matrix should be square matrix"
        self._tArray = Array(nrows)
        for i in range(nrows):
            self._tArray[i] = Array(_val)

    def numRows(self):
        return len(self._tArray)

    def numCols(self,row):
        return len(self._tArray[row-1])

    def numEle(self):
        return (nrows*(nrows+1)/2)

    def __getitem__(self,idxTuple):
        assert len(idxTuple) == 2,"Not a valid Index"
        row = idxTuple[1]
        col = idxTuple[2]
        assert row < self.numRows() and row >=0,"Invalid row index"
        assert col < self.numCols(row) and col >=0,"Invalid col index"
        array1DIdx = self._tArray[row]
        return array1DIdx[col]

    def __setitem__(self,idxTuple,value):
        assert len(idxTuple) == 2,"Not a valid Index"
        row = idxTuple[1]
        col = idxTuple[2]
        assert row < self.numRows() and row >=0,"Invalid row index"
        assert col < self.numCols(row) and col >=0,"Invalid col index"
        array1DIdx = self._tArray[row]
        array1DIdx[col] = value


if __name__ == '__main__':
    triangleArr = TriangleArray(8,8)
    print(triangleArr)
