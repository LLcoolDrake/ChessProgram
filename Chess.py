import copy

# used to feed moves if king has to move out of check


class Board:
	      
  Board = [["wR","wK","wB","wQ","wKK","wB","wK","wR"],["wP","wP","wP","--","wP","wP","--","wP"],["--","--","--","--","--","bB","--","--"],["--","--","--","--","--","--","--","--"],["bR","--","--","--","--","--","--","--"],["--","--","--","--","wK","--","--","wP"],["--","bP","bP","--","--","bP","bP","bP"],["--","bK","bB","bKK","bQ","bB","bK","bP"]]  
	 
  BlackKingsPosition = [7,3]
  WhiteKingsPosition = [0,4]

  AvailableKingMoves = [0,0,0,0,0,0,0,0]
  AvailableMoves = "Empty"  

  WhiteOppPeicesCausingCheck = []
  BlackOppPeicesCausingCheck = []

  
  def __init__(self):
    return
	 
  
    
  def printBoard(self):
    for x in range(len(self.Board)):
      print(int(x) ," " , self.Board[x])
    
    print("      0     1     2     3     4      5     6      7")
    return


  def isValidMove(self,Piece,startLet,endLet,startNum,endNum):

    # you should make case statments for this if block!duh!

    # Pawn Logic
    if(Piece == "bP" or Piece == "wP"):
      
      # Pawn Logic: -> first move 2 squares
      if(Piece == "bP" and (endLet == (startLet - 2)) and startNum == endNum):
        # makes sure nothing is in the way of pawn move

        
        if(self.Board[startLet-1][startNum]=="--" and self.Board[endLet][endNum]=="--"):
          return True
      
        return False

    # Pawn Logic -> any move 1 space up
    if(Piece == "bP" and endLet == (startLet-1) and startNum == endNum):
        # makes sure nothing is in way of pawn space
        if(self.Board[endLet][endNum]=="--"):
          return True

    # Pawn Logic -> En passant
    #not tested

    if(Piece == "bp" and endLet == (startLet-1)):
      
      if(startNum == (endNum + 1)):
        if(self.Board[startLet][endNum+1]=="wP"):
          # handle remove "wP" Right
          return True

      if(startNum == (endNum -1)):
        if(self.Board[startLet][endNum-1] =="wP"):
          #handle removal of "wP" Left
          return True
      
     

    # end of handling pawn logic

    # start of rook logic
    # start of rook logic
    # rook logic 

    if(Piece == "bR"):
      print("bR testing")
        # handle a capture first then handle a move
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      if(self.OpposingPiece(endLet,endNum,Piece)==True):
          # 
        if((startLet == endLet) or (startNum == endNum)):
          bbb = 2
        else:
          return False

        print("Primary Rook Check")
          # checks if move is valid up to capture square
        for x in range(startLet,endLet-1):
          if(self.Board[startLet+x][endNum]!="--" ):
            return False

        for x in range(startNum,endNum-1):
          if(self.Board[startLet][startNum+x]!="--"):
            return False
          
          # returns true if possible capture 
        return True

      if(self.OpposingPiece(endLet,endNum,Piece)==False):
      
        print("secondary rook check")
      
        if((startLet == endLet) or (startNum == endNum)):
          bbb=2
        else:
          return False
  

        # up direction: start let end let
        # down direction: end let start let 
        # this allows us to flip the ranges to reduce code
        # 
        z = 0
        y = 0
        if(endLet>startLet):
          z = endLet
          y = startLet
        else:
          z = startLet
          y = endLet


        for x in range(y,z,1):
          print("first for loop")
          print(y - x)
          if(self.Board[startLet-z][endNum]!='--' ):
            print("your returning false stupidly")
            return False
        n = 0
        m = 0
        # Right direction: end start
        # Left direction: start end
        if(endNum>startNum):
          n = endNum
          m = startNum
        else:
          n = startNum
          m = endNum

        for x in range(m,n,1):
          print("second for loop")
          if(self.Board[startLet][endNum-m]!="--"):
            print("your returning false stupidly 2")
            return False

        # returns true if valid move
        return True

    # Logic for Black Knight
    # Logic for Black Knight

    if(Piece == "bK"):

      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      if(self.OpposingPiece(endLet,endNum,Piece)==False):
        # 2 Up and 1 left
        if((startLet-endLet) == 2 and (startNum-endNum==1)):
          return True;

        # 2 Up and 1 Right
        if((startLet-endLet)==2 and (startNum-endNum==-1)):  
          return True

        # 2 left one down
        if((startLet-endLet)==-1 and (startNum-endNum==2)):
          return True

        # 2 left one up
        if((startLet-endLet)==1 and (startNum-endNum)==2 ):
          return True

        if((startLet-endLet)==-2 and (startNum-endNum)==1 ):
          return True
        
        if((startLet-endLet)==-2 and (startNum-endNum)==-1 ):
          return True


        ###
        # 2 right 1 down
        if((startLet-endLet)==-1 and (startNum-endNum)==-2 ):
          return True

        if((startLet-endLet)==1 and (startNum-endNum)==-2 ):
          return True  
    


      if(self.OpposingPiece(endLet,endNum,Piece)==True):
        ## we're not reaching this if statement
        ## but the program is still playing correctly
        ## so im moving on and will fix this later maybe
        
        print("opposing Peice Knight")

        if((startLet-endLet) == 2 and (startNum-endNum==1)):
          return True;

        # 2 Up and 1 Right
        if((startLet-endLet)==2 and (startNum-endNum==-1)):  
          return True

        # 2 left one down
        if((startLet-endLet)==-1 and (startNum-endNum==2)):
          return True

        # 2 left one up
        if((startLet-endLet)==1 and (startNum-endNum)==2 ):
          return True

        if((startLet-endLet)==-2 and (startNum-endNum)==1 ):
          return True
        
        if((startLet-endLet)==-2 and (startNum-endNum)==-1 ):
          return True


        ###
        # 2 right 1 down
        if((startLet-endLet)==-1 and (startNum-endNum)==-2 ):
          return True

        if((startLet-endLet)==1 and (startNum-endNum)==-2 ):
          return True  
      

      # don't think about deleting this false statement
      # its hanging out and useful
      # you can't place on the if statement above to make things better.
      return False
      
    #Logic for black Bishop
    #Logic for black Bishop

    if(Piece == "bB"):     
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # Checks to see if this is a diagonal move

      if(abs(startLet-endLet) == abs(startNum-endNum)):
        bbb = 3
      else:
        return False


      if(self.OpposingPiece(endLet,endNum,Piece)==False):

        
        # up and to the left diagonally
        if((endLet < startLet) and (startNum > endNum)) :
          for x in range(endLet,startLet,1):
            print("second for loop zz")
            print(x)
            print(endNum + x - endLet)
            print(endNum)
            if(self.Board[x][endNum+x-endLet]!='--' ):
              print("your returning false stupidly dd")
              return False
        
        # up and to the right diagonally
        if((endLet < startLet) and (startNum < endNum)) :
          backWardsEndNum = endNum
          for x in range(endLet,startLet,1):
            print(x)
            
            print(backWardsEndNum)
            print(" ")
      
            if(self.Board[x][backWardsEndNum]!='--' ):
              print("your returning false stupidly dd")
              return False
            backWardsEndNum = backWardsEndNum - 1


        # this down and to the left
        if((endLet > startLet) and (startNum > endNum)):
          DWardsStartNum = endNum + 1
          for x in range(startLet,endLet,1):
            print("second for loop zzy")
            print(x+1)
            # this is a really shitty solution to this problem
            print(DWardsStartNum)
            print(" ")

            if(self.Board[x+1][DWardsStartNum]!='--' ):
              print("your returning false stupidly dd")
              return False
            DWardsStartNum = DWardsStartNum - 1


        # down and to the right
        if((endLet > startLet) and startNum < endNum):
          rightWardsEndNum = endNum
          for x in range(startLet,endLet,1):
            print("second for loop zz")
            
            print(x)
            # this is a really shitty solution to this problem
            print(rightWardsEndNum)
      
            if(self.Board[x][rightWardsEndNum]!='--' ):
              print("your returning false stupidly dd")
              return False
            rightWardsEndNum = rightWardsEndNum - 1

          
     
       

        # returns true if valid move
        return True

      
      if(self.OpposingPiece(endLet,endNum,Piece)==True):

        OpposingPiece = self.Board[endLet][endNum]
        
        if((endLet < startLet) and (startNum > endNum)) :
          for x in range(endLet,startLet,1):
            print("second for loop zz")
            print(x)
            print(endNum + x - endLet)
            print(endNum)
            if(self.Board[x][endNum+x-endLet]!='--' and self.Board[x][endNum+x-endLet]!=OpposingPiece):
              print("your returning false stupidly dd1")
              return False
        
        # up and to the right diagonally
        if((endLet < startLet) and (startNum < endNum)) :
          backWardsEndNum = endNum
          for x in range(endLet,startLet,1):
            print(x)
            
            print(backWardsEndNum)
            print(" ")
      
            if(self.Board[x][backWardsEndNum]!='--' and self.Board[x][backWardsEndNum]!=OpposingPiece ):
              print("your returning false stupidly dd2")
              return False
            backWardsEndNum = backWardsEndNum - 1


        # this down and to the left
        if((endLet > startLet) and (startNum > endNum)):
          DWardsStartNum = endNum + 1
          for x in range(startLet,endLet,1):
            print("second for loop zzy")
            print(x+1)
            # this is a really shitty solution to this problem
            print(DWardsStartNum)
            print(" ")

            if(self.Board[x+1][DWardsStartNum]!='--'and self.Board[x+1][DWardsStartNum]!=OpposingPiece):
              print("your returning false stupidly dd3")
              return False
            DWardsStartNum = DWardsStartNum - 1


        # down and to the right
        if((endLet > startLet) and startNum < endNum):
          rightWardsEndNum = endNum
          for x in range(startLet,endLet,1):
            print("second for loop zz")
            
            print(x)
            # this is a really shitty solution to this problem
            print(rightWardsEndNum)
      
            if(self.Board[x][rightWardsEndNum]!='--' and self.Board[x][rightWardsEndNum]!=OpposingPiece):
              print("your returning false stupidly dd4")
              return False
            rightWardsEndNum = rightWardsEndNum - 1

          
     
       

        # returns true if valid move
        return True



    #Logic for Black Queen
    #Logic for Black Queen

    # this is just a combination of the bishop and Rook logic

    if(Piece == "bQ"):  
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # Checks to see if this is a diagonal move

      # Bishop Logic
      
      if(abs(startLet-endLet) == abs(startNum-endNum)):
        bbb = 3
      else:
        return False


      if(self.OpposingPiece(endLet,endNum,Piece)==False):

        
        # up and to the left diagonally
        if((endLet < startLet) and (startNum > endNum)) :
          for x in range(endLet,startLet,1):
            print("second for loop zz")
            print(x)
            print(endNum + x - endLet)
            print(endNum)
            if(self.Board[x][endNum+x-endLet]!='--' ):
              print("your returning false stupidly dd")
              return False
        
        # up and to the right diagonally
        if((endLet < startLet) and (startNum < endNum)) :
          backWardsEndNum = endNum
          for x in range(endLet,startLet,1):
            print(x)
            
            print(backWardsEndNum)
            print(" ")
      
            if(self.Board[x][backWardsEndNum]!='--' ):
              print("your returning false stupidly dd")
              return False
            backWardsEndNum = backWardsEndNum - 1


        # this down and to the left
        if((endLet > startLet) and (startNum > endNum)):
          DWardsStartNum = endNum + 1
          for x in range(startLet,endLet,1):
            print("second for loop zzy")
            print(x+1)
            # this is a really shitty solution to this problem
            print(DWardsStartNum)
            print(" ")

            if(self.Board[x+1][DWardsStartNum]!='--' ):
              print("your returning false stupidly dd")
              return False
            DWardsStartNum = DWardsStartNum - 1


        # down and to the right
        if((endLet > startLet) and startNum < endNum):
          rightWardsEndNum = endNum
          for x in range(startLet,endLet,1):
            print("second for loop zz")
            
            print(x)
            # this is a really shitty solution to this problem
            print(rightWardsEndNum)
      
            if(self.Board[x][rightWardsEndNum]!='--' ):
              print("your returning false stupidly dd")
              return False
            rightWardsEndNum = rightWardsEndNum - 1

          
     
       

        # returns true if valid move
        return True

      
      if(self.OpposingPiece(endLet,endNum,Piece)==True):

        OpposingPiece = self.Board[endLet][endNum]
        
        if((endLet < startLet) and (startNum > endNum)) :
          for x in range(endLet,startLet,1):
            print("second for loop zz")
            print(x)
            print(endNum + x - endLet)
            print(endNum)
            if(self.Board[x][endNum+x-endLet]!='--' and self.Board[x][endNum+x-endLet]!=OpposingPiece):
              print("your returning false stupidly dd1")
              return False
        
        # up and to the right diagonally
        if((endLet < startLet) and (startNum < endNum)) :
          backWardsEndNum = endNum
          for x in range(endLet,startLet,1):
            print(x)
            
            print(backWardsEndNum)
            print(" ")
      
            if(self.Board[x][backWardsEndNum]!='--' and self.Board[x][backWardsEndNum]!=OpposingPiece ):
              print("your returning false stupidly dd2")
              return False
            backWardsEndNum = backWardsEndNum - 1


        # this down and to the left
        if((endLet > startLet) and (startNum > endNum)):
          DWardsStartNum = endNum + 1
          for x in range(startLet,endLet,1):
            print("second for loop zzy")
            print(x+1)
            # this is a really shitty solution to this problem
            print(DWardsStartNum)
            print(" ")

            if(self.Board[x+1][DWardsStartNum]!='--'and self.Board[x+1][DWardsStartNum]!=OpposingPiece ):
              print("your returning false stupidly dd3")
              return False
            DWardsStartNum = DWardsStartNum - 1


        # down and to the right
        if((endLet > startLet) and startNum < endNum):
          rightWardsEndNum = endNum
          for x in range(startLet,endLet,1):
            print("second for loop zz")
            
            print(x)
            # this is a really shitty solution to this problem
            print(rightWardsEndNum)
      
            if(self.Board[x][rightWardsEndNum]!='--' and self.Board[x][rightWardsEndNum]!=OpposingPiece):
              print("your returning false stupidly dd4")
              return False
            rightWardsEndNum = rightWardsEndNum - 1

          
     
       

        # returns true if valid move
        return True


      #rook logic has to be below bishop logic
      # bishop logic checks for diagonality first
      # then sees if its a valid move

      if(self.OpposingPiece(endLet,endNum,Piece)==True):
          # 
        if((startLet == endLet) or (startNum == endNum)):
          bbb = 2
        else:
          return False

        print("Primary Rook Check")
          # checks if move is valid up to capture square
        for x in range(startLet,endLet-1):
          if(self.Board[startLet+x][endNum]!="--" ):
            return False

        for x in range(startNum,endNum-1):
          if(self.Board[startLet][startNum+x]!="--"):
            return False
          
          # returns true if possible capture 
        return True

      if(self.OpposingPiece(endLet,endNum,Piece)==False):
      
        print("secondary rook check")
      
        if((startLet == endLet) or (startNum == endNum)):
          bbb=2
        else:
          return False
  

        # up direction: start let end let
        # down direction: end let start let 
        # this allows us to flip the ranges to reduce code
        # 
        z = 0
        y = 0
        if(endLet>startLet):
          z = endLet
          y = startLet
        else:
          z = startLet
          y = endLet


        for x in range(y,z,1):
          print("first for loop")
          print(y - x)
          if(self.Board[startLet-z][endNum]!='--' ):
            print("your returning false stupidly")
            return False
        n = 0
        m = 0
        # Right direction: end start
        # Left direction: start end
        if(endNum>startNum):
          n = endNum
          m = startNum
        else:
          n = startNum
          m = endNum

        for x in range(m,n,1):
          print("second for loop")
          if(self.Board[startLet][endNum-m]!="--"):
            print("your returning false stupidly 2")
            return False
      
      # end of Queen logic 


      # start of king logic 

    # you need to handle if the king places it self into 
    # check or check mate once it moves into a location. 

    if(Piece == "bKK"):

      if(abs(startLet-endLet)!=1 or abs(startNum-endNum)!=1):
        return False

      KingsTest = [endLet,endNum]

      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      if(self.OpposingPiece(endLet,endNum,Piece)==False):
        
        if(self.Check(KingsTest)!=True):
          self.BlackKingsPosition[0] = endLet
          self.BlackKingsPosition[1] = endNum
          return True
        else:
          return False

        return True

      if(self.OpposingPiece(endLet,endNum,Piece)==True):
        if(self.Check(KingsTest)!=True):
          self.BlackKingsPosition[0] = endLet
          self.BlackKingsPosition[1] = endNum

          return True
        else:
          return False

      return True  

  ## This is the start of Piece testing code
  

  def OpposingPiece(self,endLet,endNum,Piece):
    
    print("Opposing Piece testing")

    EndLocPiece = self.Board[endLet][endNum]

    if(EndLocPiece[0]==Piece[0] or EndLocPiece[0]=="-"):
      return False
    else:
      return True


  def samePiece(self,endLet,endNum,Piece):
    print("same piece Testing")

    EndLocPiece = self.Board[endLet][endNum]

    if(EndLocPiece[0]==Piece[0]):
      print("can't move there same piece")
      return True
    else:
      return False    

 
  def move(self,startLet,startNum,endLet,endNum):
    

      # handle checkmate and move blocking
      print(self.BlackKingsPosition)
      if(self.AvailableMoves=="RestrictedMoves"):
        
        if(self.BlackKingsPosition[0]==startLet and self.BlackKingsPosition[1]==startNum):
          b = 5
          self.AvailableMoves="Empty"
        else:
          return False

        
        ## move must be correct
        ## else return false

      Piece = self.Board[startLet][startNum]
      print("move test")
      print(" ")
    
      if(self.isValidMove(Piece,startLet,endLet,startNum,endNum)):
    
        

        print("valid move")
        self.Board[startLet][startNum] = "--"
        self.Board[endLet][endNum] = Piece

        if(Piece == "bKK"):
          BlackKingsPosition = [endLet,endNum]
          print(BlackKingsPosition)

        if(Piece == "wKK"):
          WhiteKingsPosition = [endLet,endNum]
          print(BlackKingsPosition)

    
        self.AvailableMoves=="Empty"


        return True

    

  ## this is the start of the checkmate testing code
  ## perhaps want to include something in class declaration
  ## that keeps track of the kings position

  def Check(self,KingsPiece):
    
    #print("checking check")
    # handling Knight 
    # not complete yet, should handle kings position in class
    try:
      if(self.Board[KingsPiece[0]+2][KingsPiece[1]-1]=="wK"):
        return True
    except:
      bbb = 3
    try:
      if(self.Board[KingsPiece[0]+2][KingsPiece[1]+1]=="wK"):
        return True
    except:
      bbb = 3


    try:
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]+2]=="wK"):
        return True
    except:
      bbb = 3

    try:
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]-2]=="wK"):
        return True
    except:
      bbb = 3

    try:  
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]-1]=="wK"):
        print("checked knight")
        return True
    except:
      bbb = 3

    try:  
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]+1]=="wK"):
        return True
    except:
      bbb = 3

    try:  
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]+2]=="wK"):
        return True
    except:
      bbb = 3

    try:  
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]-2]=="wK"):
        return True
    except: 
      bbb = 3
    # might need to switch the 7 to an 8 so that its inclusive

    print("checking check")

    # searches for rook or queen to the left of king
    for x in range(0,KingsPiece[1],-1):
      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]=="wQ" or self.Board[KingsPiece[0]][x]=="wR"):
          return True
        else:
          return False  


    # searches for rook or queen to the right of king
    for x in range(KingsPiece[1],7,1):
      if(self.Board[KingsPiece[1]][x]!="--"):
        if(self.Board[KingsPiece[1]][x]=="wQ" or self.Board[KingsPiece[1]][x]=="wR"):
          return True
        else:
          return False 


    # searches for rook or Queen in up position 
    

    for x in range(1,KingsPiece[0]+1,1):  
      if(self.Board[KingsPiece[0]-x][KingsPiece[1]]!="--"):
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]]=="wQ" or self.Board[KingsPiece[0]-x][KingsPiece[1]]=="wR"):
          return True
        else:
          return False 

    # searches for rook or Queen in the down positon
    for x in range(KingsPiece[0],7,1):
      if(self.Board[x][KingsPiece[1]]!="--"):
        if(self.Board[x][KingsPiece[1]]=="wQ" or self.Board[x][KingsPiece[1]]=="wR"):
          return True
        else:
          return False 

    # handles Bishop or Queen Checks 

    # handle Bishop up and to the left

    for x in range(1,KingsPiece[0],1):
      if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]!="--"):
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]=="wQ" or self.Board[KingsPiece[0]-x][KingsPiece[1]-x]=="wB"):
          return True
        #else:
          #return False 

    # handles Bishop up and to the right




    for x in range(1,KingsPiece[0],1):
      try:
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]!="--"):
          if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]=="wQ" or self.Board[KingsPiece[0]-x][KingsPiece[1]+x]=="wB"):
            return True
      except: 
        b = 3 
        #else:
         # return False 

    # handles Bishop down and to the Right

    for x in range(KingsPiece[0],7,1):

      try:
        if(self.Board[KingsPiece[0]+x][KingsPiece[1]+x]!="--"):
          if(self.Board[KingsPiece[0]+x][KingsPiece[1]+x]=="wQ" or self.Board[KingsPiece[0]+x][KingsPiece[1]+x]=="wB"):
            return True
      except:
        b = 3

    # handles Bishot down and to the Left

    for x in range(KingsPiece[0],7,1):

      try:
        if(self.Board[KingsPiece[0]+x][KingsPiece[1]-x]!="--"):
          if(self.Board[KingsPiece[0]+x][KingsPiece[1]-x]=="wQ" or self.Board[KingsPiece[0]+x][KingsPiece[1]-x]=="wB"):
            return True
      except:
        b = 3
    
    # I don't think we need this return False statement

    return False


  # Kings piece is the Black or whiteKingsPostion
  # declared at the very top of the class under the board creation
  def CheckMate(self,KingsPiece):

    PCSafeSpace = [0,0,0,0,0,0,0,0]
    #checks if king is in check before checking all 
    # other squares
    if(self.Check(KingsPiece)):
      bbb = 3
    else:
      return False

    # starts from top left, clockwise
    #PCSafeSpace = [0,0,0,0,0,0,0,0]


    # also handle if peice are next to king on the edge
    if(KingsPiece[0]==7):
      PCSafeSpace = [0,0,0,0,1,1,1,0]
      if(KingsPiece[1]==0):
        PCSafeSpace = [1,0,0,0,1,1,1,1]

        # Handles king at bottom left
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]!="--"]):
          PCSafeSpace[1]=1
        
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]!="--"):
          PCSafeSpace[2]=1

        if(self.Board[KingsPiece[0]][KingsPiece[1]-1]!="--"):
          PCSafeSpace[3]=1

        # handles king at bottom right
      elif(KingsPiece[1]==7):  
        if(self.Board[KingsPiece[0]][KingsPiece[1]-1]!="--"):
          PCSafeSpace[7]=1
        
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]!="--"):
          PCSafeSpace[0]=1

        if(self.Board[KingsPiece[0]-1][KingsPiece[1]]!="--"):
          PCSafeSpace[1]=1
      else:

        # have to handle peices in the way, 5 space to check on edge
        PCSafeSpace =[0,0,0,0,1,1,1,0]
        if(self.Board[KingsPiece[0]][KingsPiece[1]-1]!="--"):
          PCSafeSpace[7]=1

        if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]!="--"):
          PCSafeSpace[0]=1
        
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]]!="--"):
          PCSafeSpace[1]=1

        if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]!="--"):
          PCSafeSpace[2]=1

        if(self.Board[KingsPiece[0]][KingsPiece[1]+1]!="--"):
          PCSafeSpace[3]=1    


    elif(KingsPiece[0]==0):
      PCSafeSpace = [1,0,0,0,0,0,1,1]
      if(KingsPiece[1]==0):
        PCSafeSpace = [1,1,1,0,0,0,1,1]

        # handles king in the top left
        if(self.Board[KingsPiece[0]][KingsPiece[1]+1]!="--"):
          PCSafeSpace[3] = 1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]!="--"):
          PCSafeSpace[4]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]]!="--"):
          PCSafeSpace[5]=1   
          
          # handles king in top right

      elif(KingsPiece[1]==7):
        if(self.Board[KingsPiece[0]][KingsPiece[1]-1]!="--"):
          PCSafeSpace[7] = 1
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]!="--"):
          PCSafeSpace[6]=1
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]]!="--"):
          PCSafeSpace[5]=1 
      
      else:
        # have to handle 5 spaces on top column
        if(self.Board[KingsPiece[0]][KingsPiece[1]-1]!="--"):
          PCSafeSpace[7]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]-1]!="--"):
          PCSafeSpace[6]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]]!="--"):
          PCSafeSpace[5]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]!="--"):
          PCSafeSpace[4]=1
        if(self.Board[KingsPiece[0]][KingsPiece[1]+1]!="--"):
          PCSafeSpace[3]=1

    # handle king on the left side edge

    elif(KingsPiece[1]==0 and KingsPiece[0]!=0 and KingsPiece[0]!=7):
        PCSafeSpace = [1,0,0,0,0,0,1,1]
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]]!="--"):
          PCSafeSpace[1]=1
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]!="--"):
          PCSafeSpace[2]=1
        if(self.Board[KingsPiece[0]][KingsPiece[1]+1]!="--"):
          PCSafeSpace[3]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]!="--"):
          PCSafeSpace[4]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]]!="--"):
          PCSafeSpace[5]=1

    elif(KingsPiece[1]==7 and KingsPiece[0]!=0 and KingsPiece[0]!=7):
        PCSafeSpace = [0,0,1,1,1,0,0,0]
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]]!="--"):
          PCSafeSpace[1]=1
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]!="--"):
          PCSafeSpace[0]=1
        if(self.Board[KingsPiece[0]][KingsPiece[1]-1]!="--"):
          PCSafeSpace[7]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]-1]!="--"):
          PCSafeSpace[6]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]]!="--"):
          PCSafeSpace[5]=1      
    
      # handle king on the inside of the board
    else:

        PCSafeSpace = [0,0,0,0,0,0,0,0]

        if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]!="--"):
          PCSafeSpace[0]=1
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]]!="--"):
          PCSafeSpace[1]=1
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]!="--"):
          PCSafeSpace[2]=1
        if(self.Board[KingsPiece[0]][KingsPiece[1]+1]!="--"):
          PCSafeSpace[3]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]!="--"):
          PCSafeSpace[4]=1 
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]]!="--"):
          PCSafeSpace[5]=1
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]-1]!="--"):
          PCSafeSpace[6]=1
        if(self.Board[KingsPiece[0]][KingsPiece[1]-1]!="--"):
          PCSafeSpace[7]=1
        


    
    print("This is PC SafeSpace")
    print(PCSafeSpace)
    
      

    # Check if kings position is in check?

    # test if check on king

    # test how many possible squares to move to
    

    # make king available squares function to produce an array if kings is on the
    # edge
   


    #BadSquares = 8

    # needs a deep coyp else it would change the recorded position of the king
    tempKingsPieceR = copy.deepcopy(KingsPiece)
    tempKingsPieceL = copy.deepcopy(KingsPiece)
    tempKingsPieceU = copy.deepcopy(KingsPiece)
    tempKingsPieceD = copy.deepcopy(KingsPiece)
    tempKingsPieceUL = copy.deepcopy(KingsPiece)
    tempKingsPieceUR = copy.deepcopy(KingsPiece)
    tempKingsPieceDL = copy.deepcopy(KingsPiece)
    tempKingsPieceDR = copy.deepcopy(KingsPiece)

    # your dumb this is not a 2 d matrix its an array

    tempKingsPieceR[1] = tempKingsPieceR[1]+1
    tempKingsPieceL[1] = tempKingsPieceL[1]-1
    tempKingsPieceU[0] = tempKingsPieceU[0]+1
    tempKingsPieceD[0] = tempKingsPieceD[0]-1

    ## you need to get rid of the Returns they will not continue 
    ## the rest of the program

    if(self.Check(tempKingsPieceR)):
      PCSafeSpace[3]=1
      #return True

    if(self.Check(tempKingsPieceL)):
      PCSafeSpace[7]=1
      #return True

    if(self.Check(tempKingsPieceU)):
      PCSafeSpace[1] = 1
      #return True

    if(self.Check(tempKingsPieceD)):
      PCSafeSpace[5]=1
      #return True


    #handles UL and DL   This is atrociously coded, fix to make more understandable
    # your cheating by not deep copying the variables again.
    tempKingsPieceDL[0] = tempKingsPieceDL[0]+1
    tempKingsPieceDL[1] = tempKingsPieceDL[1]-1

    tempKingsPieceUL[0] = tempKingsPieceUL[0]-1
    tempKingsPieceUL[1] = tempKingsPieceUL[1]-1
    
    # handles UR and DR
    tempKingsPieceDR[0] = tempKingsPieceDR[0]+1
    tempKingsPieceDR[1] = tempKingsPieceDR[1]+1

    tempKingsPieceUR[0] = tempKingsPieceUR[0]-1
    tempKingsPieceUR[1] = tempKingsPieceUR[1]+1

    if(self.Check(tempKingsPieceUL)):
      PCSafeSpace[0]=1
      #return True

    if(self.Check(tempKingsPieceDL)):
      PCSafeSpace[6]=1
      #return True

    if(self.Check(tempKingsPieceUR)):
      PCSafeSpace[2]=1
      #return True

    if(self.Check(tempKingsPieceDR)):
      PCSafeSpace[4]=1
      #return True


    # After handling squares for check 
    # check to see if a king makes any other moves inaccesable





    # run through array of open moves around King
    # if no moves return king is dead




    # Check to see if check mate can be avoided with players own peices






    print(PCSafeSpace)

    # check surrounding available locations to move to

    for x in range(len(PCSafeSpace)):
      if(PCSafeSpace[x]==0):

        AvailableKingMoves = PCSafeSpace
        self.AvailableMoves = "RestrictedMoves"
        # must handle King moving out or avoiding check
        # i elected to build a global array
        # this is dumb, and can anyone propose a solution
        # can you use lambda's here i don't know what im taling about
        # pretty much move is waiting for any move after this returns
        # and it needs to allow the king to only move in a specific location
        # it also has to check to see if blocking a move is ok
        break


        #return False

    
    print(sum(PCSafeSpace))

    #handle avoid made if its possible to block and your done 
    #with check makte
    #Jake You stopped here 
    
    if(self.AvoidMate(KingsPiece)==True):
      print("inside avoid mate")
      b = 3

      if(sum(PCSafeSpace)==8 ):
        # commented out for teams meeting
        b = 3
        return True
    
    # if after move checks, king is in check
    # and has no place to move, declare checkmate
    # not really declare it yet tho, then send this information 
    # to CheckMate Block with peice or something
    # obs if it is a knight must block with kill 
    
    return False



  def AvoidMate(self,KingsPiece):

    ColorOfKing = self.Board[KingsPiece[0]][KingsPiece[1]]

    if(KingsPiece[0]=="w"):
      self.WhiteOppPeicesCausingCheck = []
    else:
      self.BlackOppPeicesCausingCheck = []

    # This is just a rehash of the check function but it checks 
    # for all checks on the kings position
    # there can never be 3 peices checking the king at one time
    # there can be 2 peices checking the king at one time
    # So I'm recording check on king. 
    # then we have to check every peice on the board to see if it stop
    # the check, this is going to be very time consuming
    # if check is unblockable, then checkmate has occured 
    # and the game is over 



    #Search for all opponent peices on board that are attacking king
    # 

    try:
      if(self.Board[KingsPiece[0]+2][KingsPiece[1]-1]=="wK"):
        self.BlackOppPeicesCausingCheck.append([KingsPiece[0]+2,KingsPiece[1]-1])
        
    except:
      bbb = 3

    try:
      if(self.Board[KingsPiece[0]+2][KingsPiece[1]+1]=="wK"):
        self.BlackOppPeicesCausingCheck.append([KingsPiece[0]+2,KingsPiece[1]+1])
    except:
      bbb = 3


    try:
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]+2]=="wK"):
        self.BlackOppPeicesCausingCheck.append([KingsPiece[0]+1,KingsPiece[1]+2])
        
    except:
      bbb = 3

    try:
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]-2]=="wK"):
        self.BlackOppPeicesCausingCheck.append([KingsPiece[0]+1,KingsPiece[1]-2])
    except:
      bbb = 3

    try:  
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]-1]=="wK"):
        self.BlackOppPeicesCausingCheck.append([KingsPiece[0]-2,KingsPiece[1]-1])
    except:
      bbb = 3

    try:  
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]+1]=="wK"):
        self.BlackOppPeicesCausingCheck.append([KingsPiece[0]-2,KingsPiece[1]+1])
    except:
      bbb = 3

    try:  
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]+2]=="wK"):
        self.BlackOppPeicesCausingCheck.append([KingsPiece[0]-1,KingsPiece[1]+2])
    except:
      bbb = 3

    try:  
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]-2]=="wK"):
        self.BlackOppPeicesCausingCheck.append([KingsPiece[0]-1,KingsPiece[1]-2])
    except: 
      bbb = 3
    # might need to switch the 7 to an 8 so that its inclusive

    print("checking check")



    # searches for rook or queen to the left of king
    for x in range(0,KingsPiece[1],-1):
      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]=="wQ"):
          self.BlackOppPeicesCausingCheck.append(KingsPiece[0],x)
        if(self.Board[KingsPiece[0]][x]=="wR"):
          self.BlackOppPeicesCausingCheck.append(KingsPiece[0],x)
        break

    # searches for rook or queen to the right of king
    for x in range(KingsPiece[1],7,1):
      if(self.Board[KingsPiece[1]][x]!="--"):
        if(self.Board[KingsPiece[1]][x]=="wQ"):
          self.BlackOppPeicesCausingCheck.append(KingsPiece[1],x)
        
        if(self.Board[KingsPiece[1]][x]=="wR"):
          self.BlackOppPeicesCausingCheck.append(KingsPiece[1],x)
        #else:
          #return False 
        break

    # searches for rook or Queen in up position 
    
    #print("queen testing")

    for x in range(1,KingsPiece[0]+1,1):  
      if(self.Board[KingsPiece[0]-x][KingsPiece[1]]!="--"):
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]]=="wQ"): 
          self.BlackOppPeicesCausingCheck.append([KingsPiece[0]-x,KingsPiece[1]])
        
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]]=="wR"):
          self.BlackOppPeicesCausingCheck.append(KingsPiece[0]-x,KingsPiece[1])
        #else:
          #return False 
        break
    
    #print("queen end testing") 

    # searches for rook or Queen in the down positon
    for x in range(KingsPiece[0],7,1):
      if(self.Board[x][KingsPiece[1]]!="--"):
        if(self.Board[x][KingsPiece[1]]=="wQ"): 
          self.BlackOppPeicesCausingCheck.append(x,KingsPiece[1])
        if(self.Board[x][KingsPiece[1]]=="wR"):
          self.BlackOppPeicesCausingCheck.append(x,KingsPiece[1])
        break
    # handles Bishop or Queen Checks 

    # handle Bishop up and to the left

    for x in range(1,KingsPiece[0],1):
      if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]!="--"):
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]=="wQ"): 
          self.BlackOppPeicesCausingCheck.append(KingsPiece[0]-x,KingsPiece[1]-x)
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]=="wB"):
          self.BlackOppPeicesCausingCheck.append(KingsPiece[0]-x,KingsPiece[1]-x)
        break   
        #else:
          #return False 

    # handles Bishop up and to the right




    for x in range(1,KingsPiece[0],1):
      try:
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]!="--"):
          if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]=="wQ"): 
            self.BlackOppPeicesCausingCheck.append(KingsPiece[0]-x,KingsPiece[1]+x)
          if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]=="wB"):
            self.BlackOppPeicesCausingCheck.append(KingsPiece[0]-x,KingsPiece[1]+x)
          break

      except: 
        b = 3 
        #else:
         # return False 

    # handles Bishop down and to the Right

    for x in range(KingsPiece[0],7,1):

      try:
        if(self.Board[KingsPiece[0]+x][KingsPiece[1]+x]!="--"):
          if(self.Board[KingsPiece[0]+x][KingsPiece[1]+x]=="wQ"): 
            self.BlackOppPeicesCausingCheck.append(KingsPiece[0]+x,KingsPiece[1]+x)
          if(self.Board[KingsPiece[0]+x][KingsPiece[1]+x]=="wB"):
            self.BlackOppPeicesCausingCheck.append(KingsPiece[0]+x,KingsPiece[1]+x)
          break
      except:
        b = 3

    # handles Bishot down and to the Left

    for x in range(KingsPiece[0],7,1):

      try:
        if(self.Board[KingsPiece[0]+x][KingsPiece[1]-x]!="--"):
          if(self.Board[KingsPiece[0]+x][KingsPiece[1]-x]=="wQ"): 
            self.BlackOppPeicesCausingCheck.append(KingsPiece[0]+x,KingsPiece[1]-x)
          
          if(self.Board[KingsPiece[0]+x][KingsPiece[1]-x]=="wB"):
            self.BlackOppPeicesCausingCheck.append(KingsPiece[0]+x,KingsPiece[1]-x)
          break
      except:
        b = 3
    
    # I don't think we need this return False statement
    #self.BlackOppPeicesCausingCheck = []
    # there are no ways to block check, return the game is over
    
    if(len(self.BlackOppPeicesCausingCheck)==0):
      print("none")
      return False

    print("BlackOppPeice")
    print(self.BlackOppPeicesCausingCheck)
   
    
    return True    

	
def main():
	 
    CheckMate = False 
    Chess = Board()

    while(CheckMate!=True):

      print(" ")
      Chess.printBoard()
      print(" ")
      CheckMate = Chess.CheckMate(Chess.BlackKingsPosition)
      print(CheckMate)
      if(CheckMate == True):
        print("Check Make you lose")

        # do you want to play again?
        # add repetative functional play so 
        # RL can play over and over again
        break

      try:
        userStartLet = int(input("enter start Let (vertical column): "))
        userStartNum  = int(input("enter start num (horizontal column): "))
        userEndLet  = int(input("enter end Let (vertical column: "))
        userEndNum  = int(input("enter end Num (horizontal column): "))

      
        Chess.move(userStartLet,userStartNum,userEndLet,userEndNum)
      except:
        print("Make a valid move")


   
main()  
