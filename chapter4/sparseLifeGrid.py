

class SparseLifeGrid(object):

    """docstring for SparseLifeGrid"""
    def __init__(self):
        self._theElements = []

    def __repr__(self):
        reprStr = "["
        for ele in self._theElements:
            reprStr = reprStr +"("+str(ele.row)+","+str(ele.col)+")"
            reprStr += ", "
        return reprStr+" ]"

    def numLiveCells(self):
        return len(self._theElements)

    def minRange(self):
        minRow = self._theElements[0].row
        minCol = self._theElements[0].col
        for i in range(self.numLiveCells()):
            if self._theElements[i].row < minRow:
                minRow = self._theElements[i].row

            if self._theElements[i].col < minCol:
                minCol = self._theElements[i].col

        return minRow,minCol

    def maxRange(self):
        maxRow,maxCol = self._theElements[0].row,self._theElements[0].col
        for i in range(self.numLiveCells()):
            if self._theElements[i].row >= maxRow:
                maxRow = self._theElements[i].row
            if self._theElements[i].col >= maxCol:
                maxCol = self._theElements[i].col

        return maxRow,maxCol

    def configure(self,coorList):
        self._theElements = []
        for ele in coorList:
            self.setCell(ele[0],ele[1])

    def clearCell(self,row,col):
        minRow,minCol = self.minRange()
        maxRow,maxCol = self.maxRange()
        assert minRow <= row <= maxRow and minCol<=col<=maxCol,"Out of range error"
        for idx in range(self.numLiveCells()):
            if(self._theElements[idx].row == row and self._theElements[idx].col == col):
                self._theElements.pop(idx)

                return True

        return False



    def setCell(self,row,col):
        newCell = MatrixElement(row,col)
        self._theElements.append(newCell)

    def isLiveCell(self,row,col):
        for idx in range(self.numLiveCells()):
            if(self._theElements[idx].row == row and self._theElements[idx].col == col):
                return True

        return False

    def numLiveNeighbours(self,row,col):
        _neighRow = [row-1,row,row+1]
        _neighCol = [col-1,col,col+1]
        _count = 0

        for i in range(0,3):
            for j in range(0,3):
                try:
                    if self.isLiveCell(_neighRow[i],_neighCol[j]):

                        if not (i==1 and j==1):
                            _count += 1
                except:
                    continue
        return _count


class MatrixElement(object):
    """docstring for MatrixElement"""
    def __init__(self,row,col):
        self.row = row
        self.col = col

def evolve(grid):
    livecells = []
    minRow,minCol = grid.minRange()
    maxRow,maxCol = grid.maxRange()
    print(minRow,maxRow)
    evDict = {}
    for i in range(minRow-1,maxRow+2):
        for j in range(minCol-1,maxCol+2):
            neighbour = grid.numLiveNeighbours(i,j)
            evDict[(i,j)] = neighbour
            if(neighbour == 2 or neighbour==3):
                livecells.append((i,j))
    grid.configure(livecells)

if __name__ == '__main__':
    INIT_CONFIG = [ (1,1), (1,2), (2,2), (3,2) ]
    lifegrid = SparseLifeGrid()
    lifegrid.configure(INIT_CONFIG)
    print(lifegrid.isLiveCell(1,2))
    evolve(lifegrid)
    print(lifegrid)
    evolve(lifegrid)
    print(lifegrid)
    evolve(lifegrid)
    print(lifegrid)
