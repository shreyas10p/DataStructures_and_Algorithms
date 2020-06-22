import copy

class SparseMatrixSort(object):
    """docstring for SparseMatrix"""
    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols
        self._theElements = list()

    def __setitem__(self,nTuple,val):
        assert 0<= nTuple[0] <= self.numRows() and 0 <= nTuple[1] <= self.numCols(),"Not valid row or col"
        eleIndex = self.factorIndex(nTuple[0],nTuple[1])
        pos,Found = self.__findPosition(eleIndex)
        eleListLen = self.nonZeroLen()
        if val != 0:
            if(Found):
                self._theElements[pos]._val = val
            elif(pos==eleListLen):
                self._theElements.append(MatrixElement(self.factorIndex(nTuple[0],nTuple[1]),val))
            else:
                temp = self._theElements[eleListLen-1]
                for i in range(eleListLen-1,pos,-1):
                    self._theElements[i] = self._theElements[i-1]
                self._theElements[pos] = MatrixElement(self.factorIndex(nTuple[0],nTuple[1]),val)
                self._theElements.append(temp)
        else:
            if(self._theElements[pos]._index == self.factorIndex(nTuple[0],nTuple[1])):
                self._theElements.pop(pos)

    def __getitem__(self,nTuple):
        assert 0<= nTuple[0] <= self.numRows() and 0 <= nTuple[1] <= self.numCols(),"Not valid row or col"
        eleIndex = self.factorIndex(nTuple[0],nTuple[1])
        pos,Found = self.__findPosition(eleIndex)
        if(Found):
            return self._theElements[pos]._val
        else:
            return 0

    def __repr__(self):
        output = ""
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                output += " "+str(self[i,j])
            output += "\n"
        return output

    def __findPosition(self,eleIndex):
        low = 0
        high = len(self._theElements) - 1
        while(low<=high):
            mid = (low+high)/2
            if(self._theElements[mid]._index == eleIndex):
                return mid,True
            elif(self._theElements[mid]._index < eleIndex):
                low = mid +1
            elif(self._theElements[mid]._index > eleIndex):
                high = mid - 1

        return low,False

    def numRows(self):
        return self._numRows

    def numCols(self):
        return self._numCols

    def nonZeroLen(self):
        return len(self._theElements)

    def factorIndex(self,row,col):
        return ((self.numCols())*row)+col

    def matrixIndexices(self,indexNum):
        return [int(indexNum/self.numCols()),indexNum%self.numCols()]

    def scale(self,scalar):
        for i in self._theElements:
            i._val *= scalar

    def __add__(self,addMatrix):
        assert self.numRows() == addMatrix.numRows() and self.numCols() == addMatrix.numCols(),"Matrix size does not match"
        addedMatrix = copy.deepcopy(self)
        for j in addMatrix._theElements:
            [jRow,jCol] = self.matrixIndexices(j._index)
            value = addedMatrix[jRow,jCol]
            value += j._val
            addedMatrix[jRow,jCol] = value

        return addedMatrix

    def __sub__(self,subMatrix):
        assert self.numRows() == subMatrix.numRows() and self.numCols() == subMatrix.numCols(),"Matrix size does not match"
        substractedMatrix = copy.deepcopy(self)
        for j in subMatrix._theElements:
            [jRow,jCol] = self.matrixIndexices(j._index)
            value = substractedMatrix[jRow,jCol]
            value -= j._val
            substractedMatrix[jRow,jCol] = value

        return substractedMatrix

class MatrixElement(object):
    """docstring for MatrixElement"""
    def __init__(self, index,val):
        self._index = index
        self._val = val

    def __repr__(self):
        return str(self._index)+","+str(self._val)

if __name__ == '__main__':
    sMatrix = SparseMatrixSort(10,10)
    sMatrix[2,3] = 10
    sMatrix[4,2] = 11
    sMatrix[6,7] = 1
    sMatrix[1,2] = 9
    mMatrix = SparseMatrixSort(10,10)
    mMatrix[2,3] = 11
    mMatrix[1,4] = 8
    mMatrix[6,7] = 1
    mMatrix[1,1] = 10
    print(sMatrix[2,3])
    print("S",sMatrix._theElements)
    print("M",mMatrix._theElements)
    print("add",sMatrix+mMatrix)
    print("sub",sMatrix-mMatrix)
    print(sMatrix)
