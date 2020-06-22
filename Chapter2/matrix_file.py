from array2d_file import Array2D

class Matrix(object):
    """docstring for Matrix"""
    def __init__(self, numRows,numCols):
        super(Matrix, self).__init__()
        self._theMatrix = Array2D(numRows,numCols)
        self._theMatrix.clear(0)

    def numRows(self):
        return self._theMatrix.numRows()

    def numCols(self):
        return self._theMatrix.numCols()

    def __getitem__(self,idxTuple):
        assert len(idxTuple) == 2,"Invalid number of Array subscript"
        row = idxTuple[0]
        col = idxTuple[1]
        assert row>=0 and row<=self.numRows(),"Invalid Number of rows"
        assert col>=0 and col<=self.numCols(),"Invalid Number of cols"
        return self._theMatrix[row,col]

    def __setitem__(self,idxTuple,scalar):
        assert len(idxTuple) == 2,"Invalid number of Array subscript"
        row = idxTuple[0]
        col = idxTuple[1]
        assert row>=0 and row<=self.numRows(),"Invalid Number of rows"
        assert col>=0 and col<=self.numCols(),"Invalid Number of cols"
        self._theMatrix[row,col] = scalar

    def scaleBy(self,scalar):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self[i,j] *= scalar

    def transpose(self):
        self.transpose = Matrix(self.numCols(),self.numRows())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.transpose[j,i] = self[i,j]
        return self.transpose

    def __add__(self,addMatrix):
        assert addMatrix.numRows() == self.numRows() and addMatrix.numCols() == self.numCols(),"Not valid number of rows or columns"
        addedMatrix = Matrix(self.numRows(),self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                addedMatrix[i,j] = self[i,j]+addMatrix[i,j]

        return addedMatrix

    def __sub__(self,subMatrix):
        assert subMatrix.numRows() == self.numRows() and subMatrix.numCols() == self.numCols(),"Not valid number of rows or columns"
        subedMatrix = Matrix(self.numRows(),self.numCols())
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                subedMatrix[i,j] = self[i,j]-subMatrix[i,j]

        return subedMatrix

    def __repr__(self):
        matrixData = ""
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                matrixData = matrixData + " "+str(self._theMatrix[i,j])
            matrixData = matrixData +"\n"

        return matrixData

    def __mul__(self,mulMatrix):
        assert self.numCols() == mulMatrix.numRows(),"Multiplication cannot be performed"
        mutipliedMatrix = Matrix(self.numRows(),mulMatrix.numCols())
        for i in range(self.numRows()):
            for j in range(mulMatrix.numCols()):
                ansMat = [self._theMatrix[i,x]*mulMatrix[x,j] for x in range(self.numCols())]
                mutipliedMatrix[i,j] = sum(ansMat)

        return mutipliedMatrix

if __name__ == '__main__':
    matrix_obj_a = Matrix(3,2)
    matrix_obj_b = Matrix(2,3)
    matrix_obj_a[0,0] =1
    matrix_obj_a[0,1] =2
    # matrix_obj_a[0,2] =11
    matrix_obj_a[1,0] =12
    matrix_obj_a[2,0] =12
    matrix_obj_a[1,1] = 9
    # matrix_obj_a[1,2] = 7
    matrix_obj_b[0,0] = 3
    matrix_obj_b[0,1] = 4
    matrix_obj_b[0,2] = 7
    matrix_obj_b[1,0] = 5
    matrix_obj_b[1,1] = 3
    print("B",matrix_obj_b)
    print("A",matrix_obj_a)
    # added_matrix = matrix_obj_a+matrix_obj_b
    # print("add",added_matrix)
    print("mul",matrix_obj_a*matrix_obj_b)

    # matrix_obj.transpose()
