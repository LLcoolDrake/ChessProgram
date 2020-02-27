class Board:
	    
      
      
  Board = [["wR","wK","wB","wQ","wKK","wB","wK","wR"],["wP","wP","wP","wP","wP","wP","wP","wP"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["bP","bP","bP","bP","bP","bP","bP","bP"],["bR","bK","bB","bKK","bQ","bB","bK","bR"]]  
	 
  
  
  
  def __init__(self):
    return
	 
  
    
  def printBoard(self):
    for x in range(len(self.Board)):
      print(self.Board[x])
    return


         
	 
  def move(self,startLocationLet,startLocationNum,endLocationLet,endLocationNum):

    Piece = self.Board[startLocationLet][startLocationNum]
    
   
    
    self.Board[startLocationLet][startLocationNum] = "--"
    self.Board[endLocationLet][endLocationNum] = Piece



    return
	
def main():
	 
    notCheckMate = True 
    Chess = Board()

    while(notCheckMate):

      print(" ")
      Chess.printBoard()
      print(" ")

      userStartLet = int(input("enter start Let: "))
      userStartNum  = int(input("enter start num: "))
      userEndLet  = int(input("enter end Let: "))
      userEndNum  = int(input("enter end Num: "))

      Chess.move(userStartLet,userStartNum,userEndLet,userEndNum)
      
   
main()  
