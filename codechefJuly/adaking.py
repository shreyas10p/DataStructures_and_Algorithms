import ctypes
from itertools import product



if __name__ == '__main__':
    KING_POSITION_ROW = 0
    KING_POSITION_COL = 0
    KING_CELL = 'O'
    EMPTY_CELL = '.'
    OBSTACLE = 'X'
    testCases = int(input())
    nxtCellList = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(testCases):
        moves = int(input())
        emptyList =[]
        for rows in range(8):
            emptyList.append([EMPTY_CELL for cell in range(8)])
        emptyList[KING_POSITION_ROW][KING_POSITION_COL] = KING_CELL
        nxtCellRow = 0
        nxtCellCol = 0
        nxtCellIndex = -1
        moveList=[]
        nrow = KING_POSITION_ROW
        ncol = KING_POSITION_COL
        while(moves!=1):
            nxtCellIndex += 1
            if(nxtCellIndex>7):
                nrow = nxtCellRow
                ncol = nxtCellCol
                nxtCellIndex = 0
            print(nxtCellRow,nxtCellCol)
            nxtCellRow = nrow +nxtCellList[nxtCellIndex][0]
            nxtCellCol = ncol +nxtCellList[nxtCellIndex][1]
            if(0<=nxtCellRow<8 and 0<=nxtCellCol<8):
                if([nxtCellRow,nxtCellCol]!=[KING_POSITION_ROW,KING_POSITION_COL]):
                    if([nxtCellRow,nxtCellCol] not in moveList):
                        print("here",moves)
                        moveList.append([nxtCellRow,nxtCellCol])
            moves -=1

        print(moveList)


