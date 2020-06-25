import itertools


class Maze(object):
    MAZE_WALL = "*"
    MAZE_PATH_TOKEN = "x"
    MAZE_TRIED_TOKEN = "o"

    """docstring for Maze"""
    def __init__(self, Rows,Cols):
        super(Maze, self).__init__()
        self._maze = Array2D(Rows,Cols)
        self._startPos = None
        self._endPos = None

    def numRows(self):
        return self._maze.numRows()

    def numCols(self):
        return self._maze.numCols()

    def setWall(self,row,col):
        assert row >= 0 and row < self.numRows() and \
                col >= 0 and  col <self.numCols(),"Not a valid cell"
        self._maze[row,col] = self.MAZE_WALL

    def setStart(self,row,col):
        assert row >= 0 and row < self.numRows() and \
                col >= 0 and  col <self.numCols(),"Not a valid cell"
        self._startPos = CellPosition(row,col)
        self._maze[row,col] = self.MAZE_PATH_TOKEN

    def setEnd(self,row,col):
        assert row >= 0 and row < self.numRows() and \
                col >= 0 and  col <self.numCols(),"Not a valid cell"
        self._endPos = CellPosition(row,col)

    def findPath(self):
        _pathStack = Stack()
        assert self._startPos is not None,"starting position is not defined"
        _pathStack.push(self._startPos)
        _currentCellRow = _pathStack.peek().row
        _currentCellCol = _pathStack.peek().col
        while([_currentCellRow,_currentCellCol] != [self._endPos.row,self._endPos.col]):
            print("here")
            _nextPath = False
            _check = False
            for i,j in itertools.product(range(-1, 2,1), repeat=2):
                if(abs(i-j) ==1):
                    _nextPath = self._validMove(_currentCellRow+i,_currentCellCol+j)
                    if(_nextPath):
                        _check = True
                        print(_currentCellRow+i,_currentCellCol+j,"\n")
                        self._maze[_currentCellRow+i,_currentCellCol+j] = self.MAZE_PATH_TOKEN
                        _pathStack.push(CellPosition(_currentCellRow+i,_currentCellCol+j))
                        break

            if(not _check):
                removedPath = _pathStack.pop()
                self._maze[removedPath.row,removedPath.col] = self.MAZE_TRIED_TOKEN
            if(_pathStack is None):

                return False
            _currentCellRow = _pathStack.peek().row
            _currentCellCol = _pathStack.peek().col

        return True

    def reset(self):
        self._maze.clear(None)

    def draw(self):
        mazeLayout = ""
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                mazeLayout += " "+str(self._maze[i,j])
            mazeLayout = mazeLayout+"\n"
        return mazeLayout

    def _validMove(self,row,col):
        return row >= 0 and row < self.numRows() and \
                col >= 0 and  col <self.numCols() and self._maze[row,col] is None

    def _exitFound(self,row,col):
        return self._exitPos.row == row and self._exitPos.col == col

    def _markTried(self,row,col):
        assert row >= 0 and row < self.numRows() and \
                col >= 0 and  col <self.numCols(),"Not a valid cell"
        self._maze[row,col] = MAZE_TRIED_TOKEN

    def _markPath(self,row,col):
        assert row >= 0 and row < self.numRows() and \
                col >= 0 and  col <self.numCols(),"Not a valid cell"
        self._maze[row,col] = MAZE_PATH_TOKEN

class CellPosition(object):
    """docstring for CellPosition"""
    def __init__(self, row,col):
        super(CellPosition, self).__init__()
        self.row = row
        self.col = col

    # Extracts an integer value pair from the given input file.
def readValuePair( infile ):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)


def buildMaze( filename ):
    infile = open( filename, "r" )
    nrows, ncols = readValuePair( infile )
    maze = Maze( nrows, ncols )
    row, col = readValuePair( infile )
    maze.setStart( row, col )
    row, col = readValuePair( infile )
    maze.setEnd( row, col )
    for row in range( nrows ) :
        line = infile.readline()
        for col in range( len(line) ) :
            if line[col] == "*" :
                maze.setWall( row, col )
    infile.close()
    return maze


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

        from Chapter2.array2d_file import Array2D
        from lliststack import Stack
    else:
        from ..Chapter2.array2d_file import Array2D
    maze = buildMaze( "mazefile.txt" )
    if maze.findPath():
        print( "Path found...." )
        print(maze.draw())
    else :
        print( "Path not found...." )





