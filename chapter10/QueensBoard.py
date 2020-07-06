
class QueensBoard(object):
    """docstring for QueensBoard"""
    def __init__(self, size):
        super(QueensBoard, self).__init__()
        self._board = Array(size)
        self._size = size

    def size(self):
        return self._size

    def numQueens(self):
        count = 0
        for i in range(self._size):
            if(self._board[i] is not None):
                count += 1
        return count

    def unguarded(self,row,col):
        checkRow = any(row == self._board[i] for i in range(self._size))
        if(self._board[col] is not None or checkRow):
            return False
        for i in range(self.numQueens()):
            if(self._board[i] is not None):
                if(col-i == row - self._board[i]):
                    return False
        return True

    def placeQueen(self,row,col):
        self._board[col] = row

    def removeQueen(self,row,col):
        self._board[col] = None

    def reset(self):
        for i in range(self._size):
            self._board[i] = None

    def solveNQueens( self, row ):

        if self.numQueens() == self.size() :
            return True
        else :
            for col in range( self.size() ):
                if self.unguarded( row, col ):
                    self.placeQueen( row, col )
                    if self.solveNQueens(  col+1 ) :
                        return True
                    else :
                        self.removeQueen( row, col )

        return False


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) )+'/Chapter2' )

        from array import Array
    else:
        from ..Chapter2.array import Array
    board = QueensBoard(8)
    board.solveNQueens(1)
    for i in range(board.size()):
        print(board._board[i])
