# from ChessRandomAIWorking import Board as b

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

  def returnBestMove(self, Board):
    self.ChessBoard = Board
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
        if self.Board[i][j][0] == 'w':
          for u in range(1,7):
            # print("in u")
            for n in range(1,7):
              # print("in n")
              if self.Board[u][n] == '--' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([1, i,j,u,n])
              elif self.Board[u][n] == 'bP':# and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([2, i,j,u,n])
              elif self.Board[u][n] == 'bB' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([3, i,j,u,n])
              elif self.Board[u][n] == 'bR' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([4, i,j,u,n])
              elif self.Board[u][n] == 'bK' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([5, i,j,u,n])
              elif self.Board[u][n] == 'bQ' :#and self.Board.isValidMove(self.Board[i][j], i,j,u,n):
                moves.append([6, i,j,u,n])
              # elif self.Board.check([u][n]):
              #   moves.append([-1, i,j,u,n])



    bestMove = moves[0]

    for i in range(len(moves)):
      Piece = self.Board[moves[i][1]][moves[i][2]]
      if bestMove[0] < moves[i][0] and self.ChessBoard.isValidMove(Piece, moves[i][1],moves[i][2],moves[i][3],moves[i][4]):
        bestMove = moves[i]



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
