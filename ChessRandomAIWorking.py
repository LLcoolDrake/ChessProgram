import copy
import random
import time as t
from AI import AIBrain
# used to feed moves if king has to move out of check


class Board:
	      
  Board = [["wR","wK","wB","wQ","wKK","wB","wK","wR"],["--","wP","--","--","wP","wP","--","wP"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","wP"],["wB","--","--","bP","--","bP","bP","bP"],["bQ","--","bB","bKK","bP","bB","bK","bP"]]  
	 
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

    
   # print("Piece moved below:")
   # print(Piece)
   # print("Piece moved to below location")

    current = copy.deepcopy(self.Board[startLet][startNum])
    if(MoveCounter%2==0):
      KingsPosition = self.WhiteKingsPosition
    if(MoveCounter%2==1):
      KingsPosition = self.BlackKingsPosition
   
   
    #print("Kings Posiiton")
    #print(KingsPosition)
    #print("kings check test")
    #print(self.Check(KingsPosition))
    if(self.Check(KingsPosition)==False):
        self.Board[startLet][startNum] = "--"
        #print(self.Check(KingsPosition))
        if(self.Check(KingsPosition)==True):
          self.Board[startLet][startNum] = current
          print("is vld test") 
          
          return False
        else:
          self.Board[startLet][startNum] = current

    # you should make case statments for this if block!duh!

    # Pawn Logic
    if(Piece == "bP" or Piece == "wP"):
      
      #Black Pawn Logic: -> first move 2 squares
      if(Piece == "bP" and (endLet == (startLet - 2)) and startNum == endNum and (startLet == 6)):
        # makes sure nothing is in the way of pawn move

        
        if(self.Board[startLet-1][startNum]=="--" and self.Board[endLet][endNum]=="--"):
          return True
      
        return False

      # White pawn logic
      if(Piece == "wP" and (endLet == (startLet + 2)) and startNum == endNum and (startLet == 1)):
        # makes sure nothing is in the way of pawn move

        
        if(self.Board[startLet+1][startNum]=="--" and self.Board[endLet][endNum]=="--"):
          return True
      
        return False

    # Black Pawn Logic -> any move 1 space up
    if(Piece == "bP" and endLet == (startLet-1) and startNum == endNum):
        # makes sure nothing is in way of pawn space
        if(self.Board[endLet][endNum]=="--"):
          return True


    # White Pawn Logic -> and move 1 space up
    if(Piece == "wP" and endLet == (startLet+1) and startNum == endNum):
      if(self.Board[endLet][endNum]=="--"):
          return True

    #White Pawn Kill Logic 

    if(Piece == "wP" and (startLet == endLet-1) and (abs(startNum-endNum)==1)):
      slice = self.Board[endLet][endNum]
      if(slice[0]=="b"):
        return True

    #Black Pawn Kill Logic
    if(Piece == "bP" and (startLet == (endLet+1)) and (abs(startNum-endNum) == 1)):
      slice = self.Board[endLet][endNum]
      #print("slice")
      #print(slice)
      if(slice[0]=="w"):
        return True


    # Pawn Logic -> En passant
    #not tested
    # to do En pasant Logic 

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

    if(Piece[1:] == "R" ):
      #print("bR testing")
        # handle a capture first then handle a move
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      if(self.OpposingPiece(endLet,endNum,Piece)==True):
          # 
        if((startLet == endLet) or (startNum == endNum)):
          bbb = 2
        else:
          return False

       # print("Primary Rook Check")
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
      
      #  print("secondary rook check")
      
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
         # print("first for loop")
         # print(y - x)
          if(self.Board[startLet-z][endNum]!='--' ):
          #  print("your returning false stupidly")
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
         # print("second for loop")
          if(self.Board[startLet][endNum-m]!="--"):
          #  print("your returning false stupidly 2")
            return False

        # returns true if valid move
        return True

    # Logic for Black Knight
    # Logic for Black Knight

    if(Piece[1:] == "K"):

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
        
       # print("opposing Peice Knight")

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

    if(Piece[1:] == "B" ):     
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # Checks to see if this is a diagonal move

      if(abs(startLet-endLet) == abs(startNum-endNum)):
        bbb = 3
      else:
        return False


      if(self.OpposingPiece(endLet,endNum,Piece)==False):

      # print("Bishop testing")
        # up and to the left diagonally
        if((endLet < startLet) and (startNum > endNum)) :
          for x in range(endLet,startLet,1):
       #     print("second for loop zz")
        #    print(x)
        #    print(endNum + x - endLet)
         #   print(endNum)
            if(self.Board[x][endNum+x-endLet]!='--' ):
          #    print("your returning false stupidly dd")
              return False
        
        # up and to the right diagonally
        if((endLet < startLet) and (startNum < endNum)) :
          backWardsEndNum = endNum
          for x in range(endLet,startLet,1):
        #    print(x)
            
        #    print(backWardsEndNum)
        #    print(" ")
      
            if(self.Board[x][backWardsEndNum]!='--' ):
         #     print("your returning false stupidly dd4")
              return False
            backWardsEndNum = backWardsEndNum - 1


        # this down and to the left
        if((endLet > startLet) and (startNum > endNum)):
          DWardsStartNum = endNum + 1
          for x in range(startLet,endLet,1):
        #    print("second for loop zzy")
        #    print(x+1)
            # this is a really shitty solution to this problem
         #   print(DWardsStartNum)
        #    print(" ")

            if(self.Board[x+1][DWardsStartNum]!='--' ):
         #     print("your returning false stupidly dd")
              return False
            DWardsStartNum = DWardsStartNum - 1


        # down and to the right
        if((endLet > startLet) and startNum < endNum):
          rightWardsEndNum = startNum+1
          for x in range(startLet+1,endLet,1):
       #     print("second for loop zz")
            
        #    print(x)
            # this is a really shitty solution to this problem
         #   print(rightWardsEndNum)
      
            if(self.Board[x][rightWardsEndNum]!='--' ):
          #    print("your returning false stupidly dd7")
              return False
            rightWardsEndNum = rightWardsEndNum + 1

          
     
       

        # returns true if valid move
        return True

      
      if(self.OpposingPiece(endLet,endNum,Piece)==True):

        OpposingPiece = self.Board[endLet][endNum]
        
        if((endLet < startLet) and (startNum > endNum)) :
          for x in range(endLet,startLet,1):
        #    print("second for loop zz")
         #   print(x)
          #  print(endNum + x - endLet)
         #   print(endNum)
            if(self.Board[x][endNum+x-endLet]!='--' and self.Board[x][endNum+x-endLet]!=OpposingPiece):
          #    print("your returning false stupidly dd1")
              return False
        
        # up and to the right diagonally
        if((endLet < startLet) and (startNum < endNum)) :
          backWardsEndNum = endNum
          for x in range(endLet,startLet,1):
     #       print(x)
            
      #      print(backWardsEndNum)
       #     print(" ")
      
            if(self.Board[x][backWardsEndNum]!='--' and self.Board[x][backWardsEndNum]!=OpposingPiece ):
        #      print("your returning false stupidly dd2")
              return False
            backWardsEndNum = backWardsEndNum - 1


        # this down and to the left
        if((endLet > startLet) and (startNum > endNum)):
          DWardsStartNum = endNum + 1
          for x in range(startLet,endLet,1):
       #     print("second for loop zzy")
        #    print(x+1)
            # this is a really shitty solution to this problem
         #   print(DWardsStartNum)
          #  print(" ")

            if(self.Board[x+1][DWardsStartNum]!='--'and self.Board[x+1][DWardsStartNum]!=OpposingPiece):
           #   print("your returning false stupidly dd3")
              return False
            DWardsStartNum = DWardsStartNum - 1


        # down and to the right
        if((endLet > startLet) and startNum < endNum):
          rightWardsEndNum = endNum
          for x in range(startLet,endLet,1):
      #      print("second for loop zz")
            
       #     print(x)
            # this is a really shitty solution to this problem
        #    print(rightWardsEndNum)
      
            if(self.Board[x][rightWardsEndNum]!='--' and self.Board[x][rightWardsEndNum]!=OpposingPiece):
         #     print("your returning false stupidly dd4")
              return False
            rightWardsEndNum = rightWardsEndNum - 1     

          # returns true if valid move
          return True

    if(Piece[1:]=="Q"):
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # Checks to see if this is a diagonal move

      if(abs(startLet-endLet) == abs(startNum-endNum)):
        bbb = 3
      


        if(self.OpposingPiece(endLet,endNum,Piece)==False):

      # print("Bishop testing")
        # up and to the left diagonally
          if((endLet < startLet) and (startNum > endNum)) :
            for x in range(endLet,startLet,1):
       #     print("second for loop zz")
        #    print(x)
        #    print(endNum + x - endLet)
         #   print(endNum)
              if(self.Board[x][endNum+x-endLet]!='--' ):
          #    print("your returning false stupidly dd")
                return False
        
        # up and to the right diagonally
          if((endLet < startLet) and (startNum < endNum)) :
            backWardsEndNum = endNum
            for x in range(endLet,startLet,1):
        #    print(x)
            
        #    print(backWardsEndNum)
        #    print(" ")
      
              if(self.Board[x][backWardsEndNum]!='--' ):
         #     print("your returning false stupidly dd4")
                return False
              backWardsEndNum = backWardsEndNum - 1


        # this down and to the left
          if((endLet > startLet) and (startNum > endNum)):
            DWardsStartNum = endNum + 1
            for x in range(startLet,endLet,1):
        #    print("second for loop zzy")
        #    print(x+1)
            # this is a really shitty solution to this problem
         #   print(DWardsStartNum)
        #    print(" ")

              if(self.Board[x+1][DWardsStartNum]!='--' ):
         #     print("your returning false stupidly dd")
                return False
              DWardsStartNum = DWardsStartNum - 1


        # down and to the right
          if((endLet > startLet) and startNum < endNum):
            rightWardsEndNum = startNum+1
            for x in range(startLet+1,endLet,1):
       #     print("second for loop zz")
            
        #    print(x)
            # this is a really shitty solution to this problem
         #   print(rightWardsEndNum)
      
              if(self.Board[x][rightWardsEndNum]!='--' ):
          #    print("your returning false stupidly dd7")
                return False
              rightWardsEndNum = rightWardsEndNum + 1

          
     
       

        # returns true if valid move
          return True

      
        if(self.OpposingPiece(endLet,endNum,Piece)==True):

          OpposingPiece = self.Board[endLet][endNum]
        
          if((endLet < startLet) and (startNum > endNum)) :
            for x in range(endLet,startLet,1):
        #    print("second for loop zz")
         #   print(x)
          #  print(endNum + x - endLet)
         #   print(endNum)
              if(self.Board[x][endNum+x-endLet]!='--' and self.Board[x][endNum+x-endLet]!=OpposingPiece):
          #    print("your returning false stupidly dd1")
                return False
        
        # up and to the right diagonally
          if((endLet < startLet) and (startNum < endNum)) :
            backWardsEndNum = endNum
            for x in range(endLet,startLet,1):
     #       print(x)
            
      #      print(backWardsEndNum)
       #     print(" ")
      
              if(self.Board[x][backWardsEndNum]!='--' and self.Board[x][backWardsEndNum]!=OpposingPiece ):
        #      print("your returning false stupidly dd2")
                return False
              backWardsEndNum = backWardsEndNum - 1


        # this down and to the left
          if((endLet > startLet) and (startNum > endNum)):
            DWardsStartNum = endNum + 1
            for x in range(startLet,endLet,1):
       #     print("second for loop zzy")
        #    print(x+1)
            # this is a really shitty solution to this problem
         #   print(DWardsStartNum)
          #  print(" ")

              if(self.Board[x+1][DWardsStartNum]!='--'and self.Board[x+1][DWardsStartNum]!=OpposingPiece):
           #   print("your returning false stupidly dd3")
                return False
              DWardsStartNum = DWardsStartNum - 1


        # down and to the right
          if((endLet > startLet) and startNum < endNum):
            rightWardsEndNum = endNum
            for x in range(startLet,endLet,1):
      #      print("second for loop zz")
            
       #     print(x)
            # this is a really shitty solution to this problem
        #    print(rightWardsEndNum)
      
              if(self.Board[x][rightWardsEndNum]!='--' and self.Board[x][rightWardsEndNum]!=OpposingPiece):
         #     print("your returning false stupidly dd4")
                return False
              rightWardsEndNum = rightWardsEndNum - 1     

          # returns true if valid move
            return True

      # start of Rook logic but for queen peice 

      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      if(self.OpposingPiece(endLet,endNum,Piece)==True):
          # 
        if((startLet == endLet) or (startNum == endNum)):
          bbb = 2
        else:
          return False

       # print("Primary Rook Check")
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
      
      #  print("secondary rook check")
      
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
         # print("first for loop")
         # print(y - x)
          if(self.Board[startLet-z][endNum]!='--' ):
          #  print("your returning false stupidly")
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
         # print("second for loop")
          if(self.Board[startLet][endNum-m]!="--"):
          #  print("your returning false stupidly 2")
            return False

        # returns true if valid move
        return True  


 #   print("start of Q logic")
    #Logic for Black Queen and White Queen
    #Logic for Black Queen and White Queen

    # this is just a combination of the bishop and Rook logic
    if(Piece[1:] == "Q"): 
      print("inside queen")
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # Checks to see if this is a diagonal move

      # Bishop Logic
      
      if(abs(startLet-endLet) == abs(startNum-endNum)):
        bbb = 3
     


        if(self.OpposingPiece(endLet,endNum,Piece)==False):

        
        # up and to the left diagonally
          if((endLet < startLet) and (startNum > endNum)) :
            for x in range(endLet,startLet,1):
       #       print("second for loop zz")
        #      print(x)
         #     print(endNum + x - endLet)
          #    print(endNum)
              if(self.Board[x][endNum+x-endLet]!='--' ):
           #     print("your returning false stupidly dd")
                return False
        
          # up and to the right diagonally
          if((endLet < startLet) and (startNum < endNum)) :
            backWardsEndNum = endNum
            for x in range(endLet,startLet,1):
      #        print(x)
            
       #       print(backWardsEndNum)
        #      print(" ")
      
              if(self.Board[x][backWardsEndNum]!='--' ):
         #       print("your returning false stupidly dd")
                return False
              backWardsEndNum = backWardsEndNum - 1


          # this down and to the left
          if((endLet > startLet) and (startNum > endNum)):
            DWardsStartNum = endNum + 1
            for x in range(startLet,endLet,1):
      #        print("second for loop zzy")
       #       print(x+1)
             # this is a really shitty solution to this problem
        #      print(DWardsStartNum)
         #     print(" ")

              if(self.Board[x+1][DWardsStartNum]!='--' ):
        #        print("your returning false stupidly dd")
                return False
              DWardsStartNum = DWardsStartNum - 1


        # down and to the right
          if((endLet > startLet) and startNum < endNum):
            rightWardsEndNum = endNum+1
            for x in range(startLet+1,endLet,1):
        #      print("second for loop zz")
            
         #     print(x)
            # this is a really shitty solution to this problem
         #     print(rightWardsEndNum)
      
              if(self.Board[x][rightWardsEndNum]!='--' ):
          #      print("your returning false stupidly ddQ7")
                return False
              rightWardsEndNum = rightWardsEndNum + 1

          
            # returns true if valid move
            # watch out for the tab
          return True

      
        if(self.OpposingPiece(endLet,endNum,Piece)==True):

          OpposingPiece = self.Board[endLet][endNum]
        
          if((endLet < startLet) and (startNum > endNum)):
            for x in range(endLet,startLet,1):
        #      print("second for loop zz")
         #     print(x)
          #    print(endNum + x - endLet)
           #   print(endNum)
              if(self.Board[x][endNum+x-endLet]!='--' and self.Board[x][endNum+x-endLet]!=OpposingPiece):
          #      print("your returning false stupidly dd1")
                return False
        
        # up and to the right diagonally
          if((endLet < startLet) and (startNum < endNum)):
            backWardsEndNum = endNum
            for x in range(endLet,startLet,1):
          #    print(x)
            
           #   print(backWardsEndNum)
            #  print(" ")
      
              if(self.Board[x][backWardsEndNum]!='--' and self.Board[x][backWardsEndNum]!=OpposingPiece ):
         #     print("your returning false stupidly dd2")
                return False
            backWardsEndNum = backWardsEndNum - 1


        # this down and to the left
          if((endLet > startLet) and (startNum > endNum)):
            DWardsStartNum = endNum + 1
            for x in range(startLet,endLet,1):
         #     print("second for loop zzy")
          #    print(x+1)
              # this is a really shitty solution to this problem
           #   print(DWardsStartNum)
           #   print(" ")

              if(self.Board[x+1][DWardsStartNum]!='--'and self.Board[x+1][DWardsStartNum]!=OpposingPiece ):
            #    print("your returning false stupidly dd3")
                return False
              DWardsStartNum = DWardsStartNum - 1


        # down and to the right
          if((endLet > startLet) and startNum < endNum):
            rightWardsEndNum = endNum
            for x in range(startLet,endLet,1):
         #     print("second for loop zz")
            
          #    print(x)
            # this is a really shitty solution to this problem
           #   print(rightWardsEndNum)

              if(self.Board[x][rightWardsEndNum]!='--' and self.Board[x][rightWardsEndNum]!=OpposingPiece):
          #      print("your returning false stupidly dd4")
                return False
              rightWardsEndNum = rightWardsEndNum - 1
       

            # returns true if valid move
          return True


      #rook logic has to be below bishop logic
      # bishop logic checks for diagonality first
      # then sees if its a valid move

     
      if((startLet == endLet) or (startNum == endNum)):
        
    

        if(self.OpposingPiece(endLet,endNum,Piece)==True):
          # 
         

       #   print("Primary Rook Check")
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
         
          if(self.samePiece(endLet,endNum,Piece)==True):
            return False

       #   print("secondary rook check")
      
      

         # up direction: start let end let
          # down direction: end let start let 
          # this allows us to flip the ranges to reduce code
          # 
          
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
      #     print("first for loop")
       #    print(y - x)
            if(self.Board[startLet-z][endNum]!='--' ):
        #     print("your returning false stupidly")
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
       #   print("second for loop")
            if(self.Board[startLet][endNum-m]!="--"):
        #     print("your returning false stupidly 2")
              return False

          
        
          return True
        # end of Queen logic 
        return False  


    # start of king logic 

    # you need to handle if the king places it self into 
    # check or check mate once it moves into a location. 
 #   print("this should be selected peice")
  #  print(Piece)
    if(Piece[1:] == "KK"):

      if(abs(startLet-endLet)!=1 or abs(startNum-endNum)!=1):
   #     print("inside abs")
        return False

      KingsTest = [endLet,endNum]
  #    print(KingsTest)

      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      if(self.OpposingPiece(endLet,endNum,Piece)==False):
   #     print("Ok space")
    #    print(self.Check(KingsTest))
        if(self.Check(KingsTest)==False):  

          #commented out these two lines
          # white king started moving
          # don't know if it broke anything else  
          #self.KingsPosition[0] = endLet
          #self.KingsPosition[1] = endNum
     #     print("white KK m 1")
          return True
        else:
      #    print("return why false")        
          return False

        return True

      if(self.OpposingPiece(endLet,endNum,Piece)==True):
    #    print("not ok spot")
        if(self.Check(KingsTest)!=True):
          self.KingsPosition[0] = endLet
          self.KingsPosition[1] = endNum
     #     print("white kk m 2")

          return True
        else:
          return False

    #  print("last true")
      return True  

  ## This is the start of Piece testing code
  

  def OpposingPiece(self,endLet,endNum,Piece):
    
    #print("Opposing Piece testing")

    EndLocPiece = self.Board[endLet][endNum]

    if(EndLocPiece[0]==Piece[0] or EndLocPiece[0]=="-"):
      return False
    else:
      return True


  def samePiece(self,endLet,endNum,Piece):
    #print("same piece Testing")

    EndLocPiece = self.Board[endLet][endNum]

    if(EndLocPiece[0]==Piece[0]):
   #   print("can't move there same piece")
      return True
    else:
      return False    

 
  def move(self,startLet,startNum,endLet,endNum):
    
      KingsPositionT = []
      ComparePieceString = self.Board[startLet][startNum] 
      if(ComparePieceString[0]=="b"):
        KingsPositionT = self.BlackKingsPosition
      if(ComparePieceString[0]=="w"):
        KingsPositionT = self.WhiteKingsPosition

      # handle checkmate and move blocking
      #print("self.KingsPositionT positon ")
      #print(KingsPositionT)
      if(self.AvailableMoves=="RestrictedMoves"):
        print("Restricted moves")
        if(KingsPositionT[0]==startLet and KingsPositionT[1]==startNum):
          b = 5
         
          self.AvailableMoves="Empty"
        
          

        
        ## move must be correct
        ## else return false

      Piece = self.Board[startLet][startNum]
      #print("move test")
      #print(" ")
    
      if(self.isValidMove(Piece,startLet,endLet,startNum,endNum)):
    

        #print("call to is valid move")
        #print(self.Check(KingsPositionT))
        previous = copy.deepcopy(self.Board[endLet][endNum])
        #print("prvious")
        #print(previous)
        self.Board[endLet][endNum] = "$$"
        currentPeice = self.Board[startLet][startNum]
        self.Board[startLet][startNum] = "--"
        # handles to see if a peice can block check
        # if there are two peices, checkmate 
        # will pick this up, and retunr game over
        # before move -> is valid move is called again

        #print("inside move")

        #TODO this handles checkmate moving, but 
        # can't tell computer the game is over
        # need to create a variable to signify check by 
        # 1.5 peices on a specific player color 
        if(self.Check(KingsPositionT)==True):
          
          trialKingTemp = [endLet,endNum]
          if(self.Check(trialKingTemp)==False and Piece[1:]=="KK"):          
            # don't do anything, this is a legal move
            self.Board[endLet][endNum] = previous
            self.Board[startLet][startNum] = currentPeice
          
          else:
            print("upper check block ")
            self.Board[endLet][endNum] = previous
            self.Board[startLet][startNum] = currentPeice
            MoveCounter = MoveCounter - 1
            return False
        
        # resets temp Money peice
        self.Board[endLet][endNum] = previous
        
        # tests to see if peice movings puts king back in check
        # regular check, might not pick up on this
        # becuase it could kill one attacking peice but then
        # place king back in check, so it has to test
        # here as well
        
        
          
       
        #print("below second check move test")


        # now that we know this is a valid move
        # do the move 
        
        #print("valid move")
        self.Board[startLet][startNum] = "--"
        self.Board[endLet][endNum] = Piece

        if(Piece == "bKK"):
          self.BlackKingsPosition = [endLet,endNum]
          print(self.BlackKingsPosition)

        if(Piece == "wKK"):
          self.WhiteKingsPosition = [endLet,endNum]
          print(self.WhiteKingsPosition)

    
        self.AvailableMoves=="Empty"


        return True
      else:

        MoveCounter = MoveCounter - 1
        return False
      
      # this return isn't really needed 
      # but I like it for readability 
      return False
    

  ## this is the start of the checkmate testing code
  ## perhaps want to include something in class declaration
  ## that keeps track of the kings position

  def Check(self,KingsPiece):
    
    #print(KingsPiece[0])
    #print(KingsPiece[1])

    ColorOfKing = self.Board[KingsPiece[0]][KingsPiece[1]]
    OppPeices = []
    KK = ""
    Q = ""
    R = ""
    K = ""
    B = ""
    P = ""

    if(MoveCounter%2==0):
      self.WhiteOppPeicesCausingCheck = []
      OppPeices = self.WhiteOppPeicesCausingCheck
      KK = "bKK"
      Q = "bQ"
      R = "bR"
      K = "bK"
      B = "bB"
      P = "bP"
    #0print(ColorOfKing[0])
    if(MoveCounter%2==1):
      self.BlackOppPeicesCausingCheck = []
      OppPeices = self.BlackOppPeicesCausingCheck
      KK = "wKK"
      Q = "wQ"
      R = "wR"
      K = "wK"
      B = "wB"
      P = "wP"

    #print("checking check")
    # add print statement to all returns
    # find the error
    # fix why wQ thinks its in check when its not. 
    
    

    if((KingsPiece[0]+2 )< 0 and (KingsPiece[1]-1)<0 and (KingsPiece[1]-1)>7 and (KingsPiece[0]+2)>7):
       
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]-1]

      if(slice==K):
        OppPeices.append([KingsPiece[0]+2,KingsPiece[1]-1])
        
  


    if((KingsPiece[0]+2 )< 0 and (KingsPiece[1]+1)<0 and (KingsPiece[1]+1)>7 and (KingsPiece[0]+2)>7):
      
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]+1]

      if(slice==K):
        OppPeices.append([KingsPiece[0]+2,KingsPiece[1]+1])
   


    if((KingsPiece[0]+1 )< 0 and (KingsPiece[1]+2)<0 and (KingsPiece[1]+2)>7 and (KingsPiece[0]+1)>7):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]+2]  
      if(slice==K):
        OppPeices.append([KingsPiece[0]+1,KingsPiece[1]+2])
        
   

  

    if((KingsPiece[0]+1 )< 0 and (KingsPiece[1]-2)<0 and (KingsPiece[1]-2)>7 and (KingsPiece[0]+1)>7):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]-2]  

      if(slice==K):
        OppPeices.append([KingsPiece[0]+1,KingsPiece[1]-2])
   



      
    if((KingsPiece[0]-2 )< 0 and (KingsPiece[1]-1)<0 and (KingsPiece[1]-1)>7and (KingsPiece[0]-2)>7):
        
      slice = self.Board[(KingsPiece[0]-2)][(KingsPiece[1]-1)]
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]-1]==K):
        
        OppPeices.append([KingsPiece[0]-2,KingsPiece[1]-1])
  


    if((KingsPiece[0]-2 )< 0 and (KingsPiece[1]+1)<0 and (KingsPiece[1]+1)>7and (KingsPiece[0]-2)>7):
        
      slice = self.Board[KingsPiece[0]-2][KingsPiece[1]+1]

      if(slice==K):
        OppPeices.append([KingsPiece[0]-2,KingsPiece[1]+1])
   


    if((KingsPiece[0]-1 )< 0 and (KingsPiece[1]+2)<0 and (KingsPiece[1]+2)>7and (KingsPiece[0]-1)>7):

      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]+2]  

      if(slice==K):
        OppPeices.append([KingsPiece[0]-1,KingsPiece[1]+2])
    

      
    if((KingsPiece[0]-1 )< 0 and (KingsPiece[1]-2)<0 and (KingsPiece[1]-2)>7 and (KingsPiece[0]-1)>7):
      
      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]-2]

      if(slice==K):
        OppPeices.append([KingsPiece[0]-1,KingsPiece[1]-2])

  
    # might need to switch the 7 to an 8 so that its inclusive

    #print("checking check")

    # searches for rook or queen to the left of king
    for x in range(0,KingsPiece[1],-1):
      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]==Q or self.Board[KingsPiece[0]][x]==R):
          #print("Q 1")
          return True
        else:
          break  


    # searches for rook or queen to the right of king
    for x in range(KingsPiece[1],7,1):
      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]==Q or self.Board[KingsPiece[1]][x]==R):
          #print("Q 2")
          return True
        else:
          break


    # searches for rook or Queen in up position 
    

    for x in range(1,KingsPiece[0]+1,1):  
      if(self.Board[KingsPiece[0]-x][KingsPiece[1]]!="--"):
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]]==Q or self.Board[KingsPiece[0]-x][KingsPiece[1]]==R):
         # print("Q 3")
          return True
        else:
          break 

    # searches for rook or Queen in the down positon
    for x in range(KingsPiece[0],7,1):
      if(self.Board[x][KingsPiece[1]]!="--"):
        if(self.Board[x][KingsPiece[1]]==Q or self.Board[x][KingsPiece[1]]==R):
          #print("Q 4")
          return True
        else:
          break 

    # handles Bishop or Queen Checks 

    # handle Bishop up and to the left

    for x in range(1,KingsPiece[0],1):
      try:
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]!="--"):
          if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]==Q or self.Board[KingsPiece[0]-x][KingsPiece[1]-x]==B):
          
            return True
          else:
            break
      except:
        break
             

    # handles Bishop up and to the right




    for x in range(1,KingsPiece[0],1):
      try:
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]!="--"):
          if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]==Q or self.Board[KingsPiece[0]-x][KingsPiece[1]+x]==B):
            return True
          else:
            break
      except:
        break 
       
        #else:
         # return False 

    # handles Bishop down and to the Right

    for x in range(KingsPiece[0],7,1):

      try:
        if(self.Board[KingsPiece[0]+x][KingsPiece[1]+x]!="--"):
          if(self.Board[KingsPiece[0]+x][KingsPiece[1]+x]==Q or self.Board[KingsPiece[0]+x][KingsPiece[1]+x]==B):
            return True
          else:
            break
      except:
        break

    # handles Bishot down and to the Left

    for x in range(KingsPiece[0],7,1):

      try:
        if(self.Board[KingsPiece[0]+x][KingsPiece[1]-x]!="--"):
          if(self.Board[KingsPiece[0]+x][KingsPiece[1]-x]==Q or self.Board[KingsPiece[0]+x][KingsPiece[1]-x]==B):
            return True
          else:
            break
      except:
        break
    
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
      PCSafeSpace = [1,1,1,0,0,0,0,0]
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
        


    
 #   print("This is PC SafeSpace")
  ##  print(PCSafeSpace)
    
      

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
    tempKingsPieceU[0] = tempKingsPieceU[0]-1
    tempKingsPieceD[0] = tempKingsPieceD[0]+1

    ## you need to get rid of the Returns they will not continue 
    ## the rest of the program

    if(tempKingsPieceR[1] >=0 and tempKingsPieceR[1]<=7):
      if(self.Check(tempKingsPieceR)):
        PCSafeSpace[3]=1
      #return True
    if(tempKingsPieceL[1] >=0 and tempKingsPieceL[1]<=7):
      if(self.Check(tempKingsPieceL)):
        PCSafeSpace[7]=1
      #return True

    if(tempKingsPieceU[0] >=0 and tempKingsPieceU[0]<=7):
      if(self.Check(tempKingsPieceU)):
     
        PCSafeSpace[1] = 1
      #return True
    if(tempKingsPieceD[0] >=0 and tempKingsPieceD[0]<=7):
      if(self.Check(tempKingsPieceD)):
        b=3
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

    print("This is tempkings piece UL")
    print(tempKingsPieceUL)

    if(tempKingsPieceUL[0] >=0 and tempKingsPieceUL[0]<=7 and tempKingsPieceUL[1] >=0 and tempKingsPieceUL[1]<=7):
      print("first inside uppler left")
      if(self.Check(tempKingsPieceUL)==True):
        print("Inside upper left")
        PCSafeSpace[0]=1
      #return True

    if(tempKingsPieceDL[0] >=0 and tempKingsPieceDL[0]<=7 and tempKingsPieceDL[1] >=0 and tempKingsPieceDL[1]<=7):
      if(self.Check(tempKingsPieceDL)):
        PCSafeSpace[6]=1
      #return True
    if(tempKingsPieceUR[0] >=0 and tempKingsPieceUR[0]<=7 and tempKingsPieceUR[1] >=0 and tempKingsPieceUR[1]<=7):
      if(self.Check(tempKingsPieceUR)):
        PCSafeSpace[2]=1
      #return True
    if(tempKingsPieceDR[0] >=0 and tempKingsPieceDR[0]<=7 and tempKingsPieceDR[1] >=0 and tempKingsPieceDR[1]<=7):
      if(self.Check(tempKingsPieceDR)):
        PCSafeSpace[4]=1
      #return True

    #print(PCSafeSpace)

    # After handling squares for check 
    # check to see if a king makes any other moves inaccesable


    print(PCSafeSpace)


    # run through array of open moves around King
    # if no moves return king is dead




    # Check to see if check mate can be avoided with players own peices






    #print(PCSafeSpace)

    # check surrounding available locations to move to

    # this is just spaghetti code right here
    if(sum(PCSafeSpace)==8):
      self.AvailableMoves = "RestrictedMoves"
    else:
      for x in range(len(PCSafeSpace)):
        if(PCSafeSpace[x]==0):

          AvailableKingMoves = PCSafeSpace
        #  print("Restricted moves")
          self.AvailableMoves = "RestrictedMoves"
        # must handle King moving out or avoiding check
        # i elected to build a global array
        # this is dumb, and can anyone propose a solution
        # can you use lambda's here i don't know what im taling about
        # pretty much move is waiting for any move after this returns
        # and it needs to allow the king to only move in a specific location
        # it also has to check to see if blocking a move is ok
        
        #TODO: Handle what ever this is 
          break


        #return False

    
  #  print(sum(PCSafeSpace))

    #handle avoid made if its possible to block and your done 
    #with check makte
    #Jake You stopped here 
    
    if(self.AvoidMate(KingsPiece)==False):
  #    print("inside avoid mate")
      b = 3
      print("PC safe space at avoid mate")
      print(PCSafeSpace)
      if(sum(PCSafeSpace)==8 ):
        # commented out for teams meeting
        b = 3
   #     print("returning true")
        return True
      #else:
        #return False
    
    # if after move checks, king is in check
    # and has no place to move, declare checkmate
    # not really declare it yet tho, then send this information 
    # to CheckMate Block with peice or something
    # obs if it is a knight must block with kill 
    
    return False



  def AvoidMate(self,KingsPiece):

    ColorOfKing = self.Board[KingsPiece[0]][KingsPiece[1]]
    OppPeices = []
    KK = ""
    Q = ""
    R = ""
    K = ""
    B = ""
    P = ""

    # also sets comparator peices 
    if(ColorOfKing[0]=="w"):
      self.WhiteOppPeicesCausingCheck = []
      OppPeices = self.WhiteOppPeicesCausingCheck
      KK = "bKK"
      Q = "bQ"
      R = "bR"
      K = "bK"
      B = "bB"
      P = "bP"
  #  print(ColorOfKing[0])
    if(ColorOfKing[0]=="b"):
      self.BlackOppPeicesCausingCheck = []
      OppPeices = self.BlackOppPeicesCausingCheck
      KK = "wKK"
      Q = "wQ"
      R = "wR"
      K = "wK"
      B = "wB"
      P = "wP"
    


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


    if((KingsPiece[0]+2 )< 0 and (KingsPiece[1]-1)<0 and (KingsPiece[1]-1)>7 and (KingsPiece[0]+2)>7):
       
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]-1]

      if(slice==K):
        OppPeices.append([KingsPiece[0]+2,KingsPiece[1]-1])
        
  


    if((KingsPiece[0]+2 )< 0 and (KingsPiece[1]+1)<0 and (KingsPiece[1]+1)>7 and (KingsPiece[0]+2)>7):
      
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]+1]

      if(slice==K):
        OppPeices.append([KingsPiece[0]+2,KingsPiece[1]+1])
   


    if((KingsPiece[0]+1 )< 0 and (KingsPiece[1]+2)<0 and (KingsPiece[1]+2)>7 and (KingsPiece[0]+1)>7):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]+2]  
      if(slice==K):
        OppPeices.append([KingsPiece[0]+1,KingsPiece[1]+2])
        
   

  

    if((KingsPiece[0]+1 )< 0 and (KingsPiece[1]-2)<0 and (KingsPiece[1]-2)>7 and (KingsPiece[0]+1)>7):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]-2]  

      if(slice==K):
        OppPeices.append([KingsPiece[0]+1,KingsPiece[1]-2])
   



      
    if((KingsPiece[0]-2 )< 0 and (KingsPiece[1]-1)<0 and (KingsPiece[1]-1)>7and (KingsPiece[0]-2)>7):
        
      slice = self.Board[(KingsPiece[0]-2)][(KingsPiece[1]-1)]
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]-1]==K):
        
        OppPeices.append([KingsPiece[0]-2,KingsPiece[1]-1])
  


    if((KingsPiece[0]-2 )< 0 and (KingsPiece[1]+1)<0 and (KingsPiece[1]+1)>7and (KingsPiece[0]-2)>7):
        
      slice = self.Board[KingsPiece[0]-2][KingsPiece[1]+1]

      if(slice==K):
        OppPeices.append([KingsPiece[0]-2,KingsPiece[1]+1])
   


    if((KingsPiece[0]-1 )< 0 and (KingsPiece[1]+2)<0 and (KingsPiece[1]+2)>7and (KingsPiece[0]-1)>7):

      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]+2]  

      if(slice==K):
        OppPeices.append([KingsPiece[0]-1,KingsPiece[1]+2])
    

      
    if((KingsPiece[0]-1 )< 0 and (KingsPiece[1]-2)<0 and (KingsPiece[1]-2)>7 and (KingsPiece[0]-1)>7):
      
      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]-2]

      if(slice==K):
        OppPeices.append([KingsPiece[0]-1,KingsPiece[1]-2])
   
    # might need to switch the 7 to an 8 so that its inclusive

    #print("checking check")



    # searches for rook or queen to the left of king
    for x in range(0,KingsPiece[1],-1):
      if(self.Board[KingsPiece[0]][x]!="--"):

        slice = self.Board[KingsPiece[0]][x]
        if(slice==Q):
          OppPeices.append([KingsPiece[0],x])
          
        elif(slice==R):
          OppPeices.append([KingsPiece[0],x])
        break

    # searches for rook or queen to the right of king
    # the extra plus 1 some how fixed the double queen handling error
    # in the center of the board
    for x in range(KingsPiece[1]+1,7+1,1):
      if(self.Board[KingsPiece[1]][x]!="--"):

        slice = self.Board[KingsPiece[1]][x]
        if(slice==Q):
          OppPeices.append([KingsPiece[1],x])
          
        elif(slice==R):
          OppPeices.append([KingsPiece[1],x])
        #else:
          #return False 
        break

    # searches for rook or Queen in up position 
    
    #print("queen testing")
   # print("stage")
   # print(OppPeices)

    for x in range(1,KingsPiece[0]+1,1):  
      if(self.Board[KingsPiece[0]-x][KingsPiece[1]]!="--"):

        slice = self.Board[KingsPiece[0]-x][KingsPiece[1]]
        
        if(slice==Q): 
     #     print("append queen")
          OppPeices.append([KingsPiece[0]-x,KingsPiece[1]])
        
        elif(slice==R):
          OppPeices.append([KingsPiece[0]-x,KingsPiece[1]])
        #else:
          #return False 
        break
    
    #print("queen end testing") 

    # searches for rook or Queen in the down positon
    for x in range(KingsPiece[0],7,1):
      if(self.Board[x][KingsPiece[1]]!="--"):
        slice = self.Board[x][KingsPiece[1]]
        if(slice==Q): 
    #      print("queen goof")
          OppPeices.append([x,KingsPiece[1]])
        elif(slice==R):
     #     print("goof")
          OppPeices.append([x,KingsPiece[1]])
        break
    # handles Bishop or Queen Checks 

    # handle Bishop up and to the left

    for x in range(1,KingsPiece[0],1):
      if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]!="--"):

        slice = self.Board[KingsPiece[0]-x][KingsPiece[1]-x]
        if(slice==Q): 
          OppPeices.append([KingsPiece[0]-x,KingsPiece[1]-x])
        elif(slice==B):
          OppPeices.append([KingsPiece[0]-x,KingsPiece[1]-x])
        break   
        #else:
          #return False 

    # handles Bishop up and to the right




    for x in range(1,KingsPiece[0],1):
      try:
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]!="--"):

          slice = self.Board[KingsPiece[0]-x][KingsPiece[1]+x]
          if(slice==Q): 
            OppPeices.append([KingsPiece[0]-x,KingsPiece[1]+x])
          elif(slice==B):
            OppPeices.append([KingsPiece[0]-x,KingsPiece[1]+x])
          break

      except: 
        b = 3 
        #else:
         # return False 

    # handles Bishop down and to the Right

    for x in range(KingsPiece[0],7,1):

      try:
        if(self.Board[KingsPiece[0]+x][KingsPiece[1]+x]!="--"):
          
          slice = self.Board[KingsPiece[0]+x][KingsPiece[1]+x] 
          if(slice==Q): 
            OppPeices.append([KingsPiece[0]+x,KingsPiece[1]+x])
          elif(slice==B):
            OppPeices.append([KingsPiece[0]+x,KingsPiece[1]+x])
          break
      except:
        b = 3

    # handles Bishop down and to the Left

    for x in range(KingsPiece[0],7,1):

      try:
        if(self.Board[KingsPiece[0]+x][KingsPiece[1]-x]!="--"):

          slice = self.Board[KingsPiece[0]+x][KingsPiece[1]-x]
          if(slice==Q): 
            OppPeices.append([KingsPiece[0]+x,KingsPiece[1]-x])
          
          elif(slice==B):
            OppPeices.append([KingsPiece[0]+x,KingsPiece[1]-x])
          break
      except:
        b = 3
    
    # I don't think we need this return False statement
    #self.BlackOppPeicesCausingCheck = []
    # there are no ways to block check, return the game is over
    
    if(len(OppPeices)>=2):
  #    print("Can't block 2+ peices")
  #    print(OppPeices)
      return False

   # print("OppPeices")
   # print(OppPeices)
   # print(KingsPiece[0])

    if(len(OppPeices)==1):
      # pulls peice causing check on king 
      TestPeice = OppPeices[0]
      print(TestPeice)
    # if you cant block the check return false
    # this signifys a check mate and the game ends
      if(self.BlockCheck(TestPeice)==False):
        b = 3
        print("block check false")
        return False
   
    
    return False    

  def BlockCheck(self,TestPeice):

    

    OppPeiceString = self.Board[TestPeice[0]][TestPeice[1]]
    OppPeiceColor = OppPeiceString[0]

    if(OppPeiceColor=="w"):
      KingsPiece = self.BlackKingsPosition
    if(OppPeiceColor=="b"):
      KingsPiece = self.WhiteKingsPosition

  #  print("this is opp peice Color")
  #  print(OppPeiceColor)
    OppPeiceType = OppPeiceString[1:]
  #  print(OppPeiceType)

    if(OppPeiceType == "K"):
      if(self.Check(TestPeice)==True):

        

        return True
      else: 
        return False
    
    if(OppPeiceType == "R"):
      if(KingsPiece[0]==TestPeice[0]):
        if(KingsPiece[1]>TestPeice[1]):
          for x in range(TestPeice[1]+1,KingsPiece[1],1):
            if(self.Check([KingsPiece[0],x])==True):
              return True  
          return False

        if(KingsPiece[1]<TestPeice[1]):
          for x in range(KingsPiece[1]+1,TestPeice[1],1):
            if(self.Check([KingsPiece[0],x])==True):
              return True  
          return False

      if(KingsPiece[1]==TestPeice[1]):
        if(KingsPiece[0]>TestPeice[0]):
          for x in range(TestPeice[1]+1,KingsPiece[1],1):
            if(self.Check([x,KingsPiece[0]])==True):
              return True  
          return False

        if(KingsPiece[1]<TestPeice[1]):
          for x in range(KingsPiece[0]+1,TestPeice[0],1):
            if(self.Check([x,KingsPiece[0]])==True):
              return True  
          return False

      
      return False

    if(OppPeiceType == "B"):

      if(KingsPiece[0]>TestPeice[0]):
        # bishop up and to the right
        if(KingsPiece[1]<TestPeice[1]):
          counter = 1
          for x in range(KingsPiece[1]+1,TestPeice[1],1):
            if(self.Check([(KingsPiece[0]-counter),x])):
              return True
            counter = counter + 1
          return False
          
        # bishop up and to the left   
        if(KingsPiece[1]>TestPeice[1]):
          counter = 1
          for x in range(KingsPiece[1]-1,TestPeice[1],-1):
            if(self.Check([(KingsPiece[0]-counter),x])):
              return True
            counter = counter + 1
          return False

      # Bishop logic down and to the left
      if(KingsPiece[0]<TestPeice[0]):
        if(KingsPiece[1]>TestPeice[1]):
          counter = 1
          for x in range(KingsPiece[1]-1,TestPeice[1],-1):
            if(self.Check([(KingsPiece[0]+counter),x])):
              return True
            counter = counter + 1
          return False

        if(KingsPiece[1]<TestPeice[1]):
          counter = 1
          for x in range(KingsPiece[1]+1,TestPeice[1],1):
            if(self.Check([(KingsPiece[0]-counter),x])):
              return True
            return False
      
      return False 

    if(OppPeiceType == "Q"):
      #bishop logic for check block
      if(KingsPiece[0]>TestPeice[0]):
        # bishop up and to the right
        if(KingsPiece[1]<TestPeice[1]):
          counter = 1
          for x in range(KingsPiece[1]+1,TestPeice[1],1):
            if(self.Check([(KingsPiece[0]-counter),x])):
              return True
            counter = counter + 1
          return False
          
        # bishop up and to the left   
        if(KingsPiece[1]>TestPeice[1]):
          counter = 1
          for x in range(KingsPiece[1]-1,TestPeice[1],-1):
            if(self.Check([(KingsPiece[0]-counter),x])):
              return True
            counter = counter + 1
          return False

      # Bishop logic down and to the left
      if(KingsPiece[0]<TestPeice[0]):
        if(KingsPiece[1]>TestPeice[1]):
          counter = 1
          for x in range(KingsPiece[1]-1,TestPeice[1],-1):
            if(self.Check([(KingsPiece[0]+counter),x])):
              return True
            counter = counter + 1
          return False

        if(KingsPiece[1]<TestPeice[1]):
          counter = 1
          for x in range(KingsPiece[1]+1,TestPeice[1],1):
            if(self.Check([(KingsPiece[0]-counter),x])):
              return True
            return False



      #rook logic for check block
      if(KingsPiece[0]==TestPeice[0]):
        if(KingsPiece[1]>TestPeice[1]):
          for x in range(TestPeice[1]+1,KingsPiece[1],1):
            if(self.Check([KingsPiece[0],x])==True):
              return True  
          return False

        if(KingsPiece[1]<TestPeice[1]):
          for x in range(KingsPiece[1]+1,TestPeice[1],1):
            if(self.Check([KingsPiece[0],x])==True):
              return True  
          return False

      if(KingsPiece[1]==TestPeice[1]):
        if(KingsPiece[0]>TestPeice[0]):
          for x in range(TestPeice[1]+1,KingsPiece[1],1):
            if(self.Check([x,KingsPiece[0]])==True):
              return True  
          return False

        if(KingsPiece[1]<TestPeice[1]):
          for x in range(KingsPiece[0]+1,TestPeice[0],1):
            if(self.Check([x,KingsPiece[0]])==True):
              return True  
          return False

      
        return False

    if(OppPeiceString == "bP"):

      try:
        TestRight = TestPeice[TestPeice[0]-1][TestPeice[1]+1]
        if(self.Check(TestRight)==True):
          return True
        else: 
          return False
      except:
        return False

      try:

        TestLeft = TestPeice[TestPeice[0]-1][TestPeice[1]-1]
        if(self.Check(TestLeft)==True):
          return True
        else: 
          return False
      except:
        return False

    if(OppPeiceString == "wP"):

      try:
        TestRight = TestPeice[TestPeice[0]+1][TestPeice[1]+1]
        if(self.Check(TestRight)==True):
          return True
        else: 
          return False
      except:
        return False

      try:
        TestLeft = TestPeice[TestPeice[0]+1][TestPeice[1]-1]
        if(self.Check(TestLeft)==True):
          return True
        else: 
          return False
      except:
        return False


    # this could never happen
    #if(OppPeiceType == "KK"):
     # return

     # this return is part of the end, and not part of the pawn test

    return False
  	
def main():
	 
    # set to one for testing 
    # reset back to 0 for white to go first
    global MoveCounter 
    MoveCounter = 0
    CheckMate = False 
    Chess = Board()
    # brain = AIBrain(Chess, )
    Chess.printBoard()

    while(CheckMate!=True):

   #   print(" ")
     
    #  print(" ")
      if(MoveCounter%2==0):
        CheckMate = Chess.CheckMate(Chess.WhiteKingsPosition)
        oPPKingsCurrentColor = "b"
        
    

      elif(MoveCounter%2==1):
        CheckMate = Chess.CheckMate(Chess.BlackKingsPosition)
        oPPKingsCurrentColor ="w"
      #print(CheckMate)
      if(CheckMate == True):
        print("Check Mate you lose")

        # do you want to play again?
        # add repetative functional play so 
        # RL can play over and over again
        break
      if(MoveCounter%2==0):
        b=3
        #print("Whites turn to move")
      elif(MoveCounter%2==1):
        print("Blacks turn to move")

      # Move counter is not WORKING if a peice puts a king in check
     # print("upper move counter")
      #print(MoveCounter)
      # try:

        if(MoveCounter%2==0):
          userStartLet = int(input("enter start Let (vertical column): "))
          userStartNum  = int(input("enter start num (horizontal column): "))
          userEndLet  = int(input("enter end Let (vertical column: "))
          userEndNum  = int(input("enter end Num (horizontal column): "))

        elif(MoveCounter%2==1):

           # Start of White random AI 
          #print("Whites turn to move")
          #print("White is thinking pretty hard")
          #t.sleep(1)
            bestMove = []
            # bestMove = brain.returnBestMove(Chess)

            userStartLet = bestMove[1]
            userStartNum = bestMove[2]
            userEndLet = bestMove[3]
            userEndNum = bestMove[4]
        
        
        
        
        SelectedPiece = Chess.Board[userStartLet][userStartNum]
        if(MoveCounter%2==0 and SelectedPiece[0]=="b"):
          # move counter decrament is probably causing a problem here
          #MoveCounter = MoveCounter - 1
          raise Exception("cant move that piece")
        if(MoveCounter%2==1 and SelectedPiece[0]=="w"):
          # move counter decrament is probabably 
          # causing a problem here
          #MoveCounter = MoveCounter - 1
          raise Exception("can't move that peice")
      
        if(Chess.move(userStartLet,userStartNum,userEndLet,userEndNum)==True):
          print("\n")
          Chess.printBoard()
          if(MoveCounter%2==0):
            
            print("Blacks turn to make a  move")



        
      # except:
      #
      #   MoveCounter = MoveCounter - 1
        
      

      
      #print("checkmates")
      #print(Chess.CheckMate(Chess.BlackKingsPosition))
      #print(Chess.CheckMate(Chess.WhiteKingsPosition))
      

      MoveCounter = MoveCounter + 1

      # move coutner needs to be reversed 
     

      #Chess.printBoard()
      if(MoveCounter%2==1):
        print("Move counter value ")
        print(MoveCounter)
        print(" \n")

main()  
