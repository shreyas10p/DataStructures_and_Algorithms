t = int(input())

while(t):
  k = int(input())

  board = [
    [1,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
  ]

  row = int(k / 8) # Last unfilled row number
  unfilledInRow = k % 8 # No of obstacles in last unfilled row
  print(row,unfilledInRow)
  # Placing Obstacles:
  if k != 64:
    if not unfilledInRow: # k divisible by 8
      for i in range(8):
        board[row][i] = 2
    else:
      for i in range(unfilledInRow, 8): # Fill unfilled row
        board[row][i] = 2
      if row < 7: # Fill next row
        for j in range(0, unfilledInRow + 1):
          board[row+1][j] = 2
    print(board)
  # Print board
  for i in range(8):
    for j in range(8):
      if board[i][j] == 1:
        print('O', end='')
      elif board[i][j] == 2:
        print('X', end='')
      else:
        print('.', end='')
    print()

  t -= 1
