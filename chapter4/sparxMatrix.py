import copy

class SparseMatrix(object):
    """docstring for SparseMatrix"""
    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols
        self._theElements = list()

    def numRows(self):
        return self._numRows

    def numCols(self):
        return self._numCols

    def __getitem__(self,nTuple):
        assert 0<= nTuple[0] <= self.numRows() and 0 <= nTuple[1] <= self.numCols(),"Not valid row or col"
        for ele in self._theElements:
            if(ele._row == nTuple[0] and ele._col == nTuple[1]):
                return ele._val

        return 0

    def _findPosition(self,row,col):
        assert 0<= row <= self.numRows() and 0 <= col <= self.numCols(),"Not valid row or col"
        for idx,ele in enumerate(self._theElements):
            if(ele._row == row and ele._col == col):
                return idx

        return None

    def __setitem__(self,nTuple,val):
        assert 0<= nTuple[0] <= self.numRows() and 0 <= nTuple[1] <= self.numCols(),"Not valid row or col"
        pos = self._findPosition(nTuple[0],nTuple[1])
        if val != 0:
            if(pos is not None):
                self._theElements[pos]._val = val
            else:
                self._theElements.append(MatrixElement(nTuple[0],nTuple[1],val))
        else:
            if(pos is not None):
                self._theElements.pop(pos)

    def scale(self,scalar):
        for i in self._theElements:
            i._val *= scalar

    def __repr__(self):
        output = ""
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                output += " "+str(self[i,j])
            output += "\n"
        return output

    def __add__(self,addMatrix):
        assert self.numRows() == addMatrix.numRows() and self.numCols() == addMatrix.numCols(),"Matrix size does not match"
        # addedMatrix = SparseMatrix(self.numRows(),self.numCols())
        addedMatrix = copy.deepcopy(self)
        # for i in self._theElements:
        #     print("self",id(i))
        #     addedMatrix._theElements.append(i)
        #     print("addedid",id(addedMatrix._theElements[-1]))
        for j in addMatrix._theElements:
            value = addedMatrix[j._row,j._col]
            value += j._val
            addedMatrix[j._row,j._col] = value

        return addedMatrix

class MatrixElement(object):
    """docstring for MatrixElement"""
    def __init__(self, row,col,val):
        self._row = row
        self._col = col
        self._val = val

if __name__ == '__main__':
    sMatrix = SparseMatrix(10,10)
    sMatrix[2,3] = 10
    sMatrix[4,2] = 11
    sMatrix[6,7] = 1
    sMatrix[1,2] = 9
    mMatrix = SparseMatrix(10,10)
    mMatrix[2,3] = 11
    mMatrix[1,4] = 8
    mMatrix[6,7] = 1
    mMatrix[1,1] = 10
    print(sMatrix[2,3])
    print("S",sMatrix)
    print("M",mMatrix)
    print("add",sMatrix+mMatrix)
    print(sMatrix)
