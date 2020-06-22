from array2d_file import Array2D

class LifeGrid(object):

    LIVE_CELL = 1
    DEAD_CELL = 0

    """docstring for LifeGrid"""
    def __init__(self,nrows, ncols):
        self._grid = Array2D(nrows,ncols)
        self._grid.clear(LifeGrid.DEAD_CELL)

    def __repr__(self):
        reprStr = "["
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                if(self.isCellAlive(i,j)):
                    reprStr = reprStr + "("+str(i)+","+str(j)+")"
                    reprStr += ", "
        return reprStr +" ]"

    def numRows(self):
        return self._grid.numRows()

    def numCols(self):
        return self._grid.numCols()

    def configure(self,coorList):
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i,j)

        for item in coorList:
            assert item[0] < self.numRows() and item[1] <self.numCols(),"invalid row or column"
            self.setCell(item[0],item[1])

    def clearCell(self,row,col):
        assert 0<=row < self.numRows() and 0<=col<self.numCols(),"invalid row or col"
        self._grid[row,col] = LifeGrid.DEAD_CELL

    def setCell(self,row,col):
        assert 0<=row < self.numRows() and 0<=col<self.numCols(),"invalid row or col"
        self._grid[row,col] = LifeGrid.LIVE_CELL

    def isCellAlive(self,row,col):
        assert 0<=row < self.numRows() and 0<=col<self.numCols(),"invalid row or col"
        return self._grid[row,col] == LifeGrid.LIVE_CELL

    def numLiveNeighbours(self,row,col):
        assert 0<=row < self.numRows() and 0<=col<self.numCols(),"invalid row or col"
        _neighRow = [row-1,row,row+1]
        _neighCol = [col-1,col,col+1]
        _count = 0

        for i in range(0,3):
            for j in range(0,3):
                try:
                    if self.isCellAlive(_neighRow[i],_neighCol[j]):
                        if not (i==1 and j==1):
                            _count += 1
                except:
                    continue
        return _count

def evolve(grid):
    livecells = []
    neighbourDict = {}
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            neighbour = grid.numLiveNeighbours(i,j)
            neighbourDict[(i,j)] = neighbour
            if(neighbour == 2 or neighbour==3):

                livecells.append((i,j))
    grid.configure(livecells)


if __name__ == '__main__':
    INIT_CONFIG = [ (1,1), (1,2), (2,2), (3,2) ]
    lifegrid = LifeGrid(8,8)
    lifegrid.configure(INIT_CONFIG)
    print(lifegrid)
    evolve(lifegrid)
    print(lifegrid)







