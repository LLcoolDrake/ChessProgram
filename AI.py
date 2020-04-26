import copy
# from CHESSGUISandBox import Board
class AIBrain:
  ChessBoard = []
  ChessTurn = 0

  #ChessBlackPeiceLocation = []
  #ChessWhitePeiceLocation = []
  
  # can add the above information
  # and pass it from main down into here 


  def __init__(self,Board,ChessTurn):
    self.ChessBoard = Board
    self.ChessTurn = ChessTurn

  def UpdateBoardData(self,ChessBoardT):
    self.ChessBoard = ChessBoardT

  def returnBestMove(self, board):
    self.ChessBoard = board
    print(type(self.ChessBoard))
    moves = []
    ## do AI Stuff here
    ## add helper functions
    ## create a move list
    ## that is then sent back to main
    ## AI.returnBestMove -> returns move for
    ## white. We can incorporate black later

    for i in range(1, 7):
      # print("in i")
      for j in range(1,7):
        # print("in j")
        # print(self.Board)
        if self.ChessBoard[i][j][0] == 'w':
          for u in range(1,7):
            # print("in u")
            for n in range(1,7):
              # print("in n")
              if self.ChessBoard[u][n] == '--' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([1, i,j,u,n])
              elif self.ChessBoard[u][n] == 'bP':# and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([2, i,j,u,n])
              elif self.ChessBoard[u][n] == 'bB' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([3, i,j,u,n])
              elif self.ChessBoard[u][n] == 'bR' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([4, i,j,u,n])
              elif self.ChessBoard[u][n] == 'bK' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([5, i,j,u,n])
              elif self.ChessBoard[u][n] == 'bQ' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([6, i,j,u,n])
              # elif self.Board.check([u][n]):
              #   moves.append([-1, i,j,u,n])



    bestMove = moves[0]

    for i in range(len(moves)):
      Piece = self.ChessBoard[moves[i][1]][moves[i][2]]
      if bestMove[0] < moves[i][0] and self.ChessBoard.isValidMove(Piece, moves[i][1],moves[i][2],moves[i][3],moves[i][4]):
        bestMove = moves[i]

    print(bestMove)

    # ChessStartLet = 2
    # ChessEndLet = 3
    # ChessStartNum = 4
    # ChessEndNum = 5
    #
    #
    # ChessMove = []
    #
    # ChessMove.append(ChessStartLet)
    # ChessMove.append(ChessEndLet)
    # ChessMove.append(ChessStartNum)
    # ChessMove.append(ChessEndNum)

    return bestMove

  def isValidMove(self, Piece, startLet, endLet, startNum, endNum):

    # if (MoveCounter % 2 == 0):
    #   KingsPosition = copy.deepcopy(self.WhiteKingsPosition)
    #   KK = "wKK"
    #   Q = "wQ"
    #   R = "wR"
    #   K = "wK"
    #   B = "wB"
    #   P = "wP"
    #
    # if (MoveCounter % 2 == 1):
    #   KingsPosition = copy.deepcopy(self.BlackKingsPosition)
    #   KK = "bKK"
    #   Q = "bQ"
    #   R = "bR"
    #   K = "bK"
    #   B = "bB"
    #   P = "bP"

      # Black Pawn Logic: -> first move 2 squares
    if (Piece == "bP" and (endLet == (startLet - 2)) and startNum == endNum and (startLet == 6)):
      # makes sure nothing is in the way of pawn move

      if (self.Board[startLet - 1][startNum] == "--" and self.Board[endLet][endNum] == "--"):
        return True

      return False

      # White pawn logic
    if (Piece == "wP" and (endLet == (startLet + 2)) and startNum == endNum and (startLet == 1)):
      # makes sure nothing is in the way of pawn move

      if (self.Board[startLet + 1][startNum] == "--" and self.Board[endLet][endNum] == "--"):
        return True

      return False

    # Black Pawn Logic -> any move 1 space up
    if (Piece == "bP" and endLet == (startLet - 1) and startNum == endNum):
      # makes sure nothing is in way of pawn space
      if (self.Board[endLet][endNum] == "--"):
        return True
      else:
        return False

    # White Pawn Logic -> and move 1 space up
    if (Piece == "wP" and endLet == (startLet + 1) and startNum == endNum):
      if (self.Board[endLet][endNum] == "--"):
        return True
      else:
        return False

    # White Pawn Kill Logic

    if (Piece == "wP" and (startLet == endLet - 1) and (abs(startNum - endNum) == 1)):
      slice = self.Board[endLet][endNum]
      if (slice[0] == "b"):
        return True

    # Black Pawn Kill Logic
    if (Piece == "bP" and (startLet == (endLet + 1)) and (abs(startNum - endNum) == 1)):
      slice = self.Board[endLet][endNum]

      if (slice[0] == "w"):
        return True

    # Pawn Logic -> En passant
    # not tested
    # to do En pasant Logic

    # if(Piece == "bp" and endLet == (startLet-1)):

    # if(startNum == (endNum + 1)):
    #  if(self.Board[startLet][endNum+1]=="wP"):
    # handle remove "wP" Right
    #   return True

    # if(startNum == (endNum -1)):
    #  if(self.Board[startLet][endNum-1] =="wP"):
    # handle removal of "wP" Left
    #   return True

    # start of rook logic

    if (Piece == R):

      if (self.samePiece(endLet, endNum, Piece) == True):
        return False

      if ((startLet != endLet) and (startNum != endNum)):
        return False

      # handles up
      if (startLet > endLet):
        for x in range(startLet - 1, endLet, -1):
          if (self.Board[x][endNum] != "--"):
            return False

        # handles down
      if (startLet < endLet):
        for x in range(startLet + 1, endLet, 1):
          if (self.Board[x][endNum] != "--"):
            return False

        # handles left
      if (startNum > endNum):
        for x in range(startNum - 1, endNum, -1):
          if (self.Board[endLet][x] != "--"):
            return False

        # handles right
      if (startNum < endNum):
        for x in range(startNum + 1, endNum, 1):
          if (self.Board[endLet][x] != "--"):
            return False

      return True

    # Logic for Knight

    if (Piece == K):

      if (self.samePiece(endLet, endNum, Piece) == True):
        return False

        # 2 up 1 left

      if ((startLet - endLet) >= 0 and (startLet - endLet) <= 7 and (startNum - endNum) >= 0 and (
              startNum - endNum) <= 7):

        if ((startLet - endLet) == 2 and (startNum - endNum == 1)):
          return True;

        # 2 Up and 1 Right
        if ((startLet - endLet) == 2 and (startNum - endNum == -1)):
          return True

          # 2 left one down
        if ((startLet - endLet) == -1 and (startNum - endNum == 2)):
          return True

          # 2 left one up
        if ((startLet - endLet) == 1 and (startNum - endNum) == 2):
          return True

        if ((startLet - endLet) == -2 and (startNum - endNum) == 1):
          return True

        if ((startLet - endLet) == -2 and (startNum - endNum) == -1):
          return True

          # 2 right 1 down
        if ((startLet - endLet) == -1 and (startNum - endNum) == -2):
          return True

        if ((startLet - endLet) == 1 and (startNum - endNum) == -2):
          return True

      return False

    # Logic for black Bishop

    if (Piece == B):
      if (self.samePiece(endLet, endNum, Piece) == True):
        return False

      # Checks to see if this is a diagonal move

      if (abs(startLet - endLet) != abs(startNum - endNum)):
        return False

        # up and to the left diagonally
      if ((endLet < startLet) and (startNum > endNum)):
        LC = 1
        for x in range(startLet - 1, endLet, -1):

          if (self.Board[x][startNum - LC] != '--' or (startNum - LC < 0)):
            #    print("your returning false stupidly dd")
            return False
          LC = LC + 1

        # up and to the right diagonally
      if ((endLet < startLet) and (startNum < endNum)):
        RC = 1
        for x in range(startLet - 1, endLet, -1):

          if (self.Board[x][startNum + RC] != '--'):
            #     print("your returning false stupidly dd4")
            return False

          RC = RC + 1

        # this down and to the left
      if ((startLet < endLet) and (startNum > endNum)):

        # this used to be = endNum + 1
        LC = 1
        for x in range(startLet + 1, endLet, 1):
          #

          if (self.Board[x][startNum - LC] != '--'):
            #     print("your returning false stupidly dd")
            return False
          LC = LC + 1

        # down and to the right
      if ((startLet < endLet) and startNum < endNum):
        RC = 1

        for x in range(startLet + 1, endLet, 1):

          if (self.Board[x][startNum + RC] != '--'):
            #    print("your returning false stupidly dd7")
            return False
          RC = RC + 1

      return True

    if (Piece == Q):

      if (self.samePiece(endLet, endNum, Piece) == True):
        return False

      # Checks to see if this is a diagonal move

      if (abs(startLet - endLet) == abs(startNum - endNum)):

        # up and to the left diagonally
        if ((endLet < startLet) and (startNum > endNum)):

          LC = 1
          for x in range(startLet - 1, endLet, -1):

            if (self.Board[x][startNum - LC] != '--'):
              #    print("your returning false stupidly dd")
              return False

            LC = LC + 1

        # up and to the right diagonally
        if ((endLet < startLet) and (startNum < endNum)):

          RC = 1
          for x in range(startLet - 1, endLet, -1):

            if (self.Board[x][startNum + RC] != '--'):
              #     print("your returning false stupidly dd4")
              return False
            RC = RC + 1

        # this down and to the left
        if ((startLet < endLet) and (startNum > endNum)):

          LC = 1
          for x in range(startLet + 1, endLet, 1):

            if (self.Board[x][startNum - LC] != '--'):
              #     print("your returning false stupidly dd")
              return False
            LC = LC + 1

          # down and to the right
        if ((startLet < endLet) and startNum < endNum):

          RC = 1
          for x in range(startLet + 1, endLet, 1):

            if (self.Board[x][startNum + RC] != '--'):
              #    print("your returning false stupidly dd7")
              return False
            RC = RC + 1

        # returns true if valid move
        return True

      # start of Rook logic but for queen peice

      if ((startLet == endLet) or (startNum == endNum)):

        # Handles Up
        # handles up
        if (startLet > endLet):
          for x in range(startLet - 1, endLet, -1):
            if (self.Board[x][endNum] != "--"):
              return False

        # handles down
        if (startLet < endLet):
          for x in range(startLet + 1, endLet, 1):
            if (self.Board[x][endNum] != "--"):
              return False

        # handles left
        if (startNum > endNum):
          for x in range(startNum - 1, endNum, -1):
            if (self.Board[endLet][x] != "--"):
              return False

        # handles right
        if (startNum < endNum):
          for x in range(startNum + 1, endNum, 1):
            if (self.Board[endLet][x] != "--"):
              return False

        return True

        # End of Queen Logic
      return False

    # start of king logic

    if (Piece == KK):

      if (self.samePiece(endLet, endNum, Piece) == True):
        return False

      if ((abs(startLet - endLet) == 1 or abs(startLet - endLet) == 0) and (
              abs(startNum - endNum) == 1 or abs(startNum - endNum) == 0)):
        print("inside abs")
        print(str(startLet) + str(startNum) + str(endLet) + str(endNum))
        return True

      else:

        return False

    # redundent False incase something ever sliped through
    # which it shouldn't
    return False
