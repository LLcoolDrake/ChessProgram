

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

  def returnBestMove():

    ## do AI Stuff here
    ## add helper functions
    ## create a move list
    ## that is then sent back to main
    ## AI.returnBestMove -> returns move for
    ## white. We can incorporate black later


    ChessStartLet = 2
    ChessEndLet = 3
    ChessStartNum = 4
    ChessEndNum = 5


    ChessMove = []

    ChessMove.append(ChessStartLet)
    ChessMove.append(ChessEndLet)
    ChessMove.append(ChessStartNum)
    ChessMove.append(ChessEndNum)

    return ChessMove
