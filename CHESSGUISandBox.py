import copy
import random
import pygame
from ChessGUI import GUI
#from AI import AIBrain

class Board:

  # Creates board variable
  # all updates to board are sent here
  # board sends it's data to GUI, Which displays data
  # GUI also handles move clicks, which get sent to logic
  # logic then updates board. Cycle repeats
	      
  Board = [["wR","wK","wB","wKK","wQ","wB","wK","wR"],["wP","wP","wP","wP","wP","wP","wP","wP"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["--","--","--","--","--","--","--","--"],["bP","bP","bP","bP","bP","bP","bP","bP"],["bR","bK","bB","bKK","bQ","bB","bK","bR"]]  
	 
  # keeps trackt of King location
  # This is updated everytime the king is moved

  BlackKingsPosition = [7,3]
  WhiteKingsPosition = [0,3]

  # Variable declaration
  # used for holding available legal moves for king
  # aids in the use of determining checkmate

  whitePCsafe = []
  blackPCsafe = []

  # hash keys cant be lists srs. 0 is top Left
  # 63 is bottom right. use % to find correct location on 
  # board.
  # Hashkeys was potentially needed 
  # we didn't use it. 
  # semi-functional
  # keeps track of individual piece location 

  WhitePieces = {0: "wR", 1: "wK", 2: "wB", 3: "wKK", 4: "wQ", 5: "wB", 6: "wK", 7: "wR", 8: "wP", 9: "wP", 10: "wP", 11: "wP", 12: "wP", 13: "wP", 14: "wP", 15: "wP"}

  #BlackPieces = {48:"bP",49:"bP",50:"bP",51:"bP",52:"bP",53:"bP",54:"bP",55:"bP",56:"bR",57:"bK",58:"bB",59:"bKK",60:"bQ",61:"bB",62:"bK",63:"bR"}

  BlackPieces = {59:"bKK"}

  # Not used anymore
  # should delete

  AvailableKingMoves = [0,0,0,0,0,0,0,0]
  AvailableMoves = "Empty"  

  # variable declaration
  # aids in containing peices causing check for
  # current player

  WhiteOppPeicesCausingCheck = []
  BlackOppPeicesCausingCheck = []

  
  def __init__(self):
    return
	 
  # Prints out board to console 
    
  def printBoard(self):
    
    for x in range(len(self.Board)):
      print(str(x) + " " + str(self.Board[x]))
    
    print("      0     1     2     3     4      5     6      7")
    
    return

  # Checks to see if selected move is valid for chess peice
  # does not handle check, block check, anything else
  # just returns if its a valid move

  def isValidMove(self,Piece,startLet,endLet,startNum,endNum):
  
    #Switchs between BoardPrint mod 2
    # Board print keeps track of what players turn it is
    # 0 = whites turn. 1 = blacks turn 

    # a return True returns a valid move designation

    if(BoardPrint%2==0):
      KingsPosition = copy.deepcopy(self.WhiteKingsPosition)
      KK = "wKK"
      Q = "wQ"
      R = "wR"
      K = "wK"
      B = "wB"
      P = "wP"

    if(BoardPrint%2==1):
      KingsPosition = copy.deepcopy(self.BlackKingsPosition)
      KK = "bKK"
      Q = "bQ"
      R = "bR"
      K = "bK"
      B = "bB"
      P = "bP"

 
      
    #Black Pawn Logic: -> first move 2 squares
    if(Piece == "bP" and (endLet == (startLet - 2)) and startNum == endNum and (startLet == 6)):
        
        # makes sure nothing is in the way of pawn move   
      if(self.Board[startLet-1][startNum]=="--" and self.Board[endLet][endNum]=="--"):
        return True
      
      return False

    # White pawn logic -> first move 2 squares
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
        else:
          return False


    # White Pawn Logic -> and move 1 space up
    if(Piece == "wP" and endLet == (startLet+1) and startNum == endNum):
      if(self.Board[endLet][endNum]=="--"):
          return True
      else:
        return False

    #White Pawn Kill Logic 
    if(Piece == "wP" and (startLet == endLet-1) and (abs(startNum-endNum)==1)):
      slice = self.Board[endLet][endNum]
      if(slice[0]=="b"):
        return True

    #Black Pawn Kill Logic
    if(Piece == "bP" and (startLet == (endLet+1)) and (abs(startNum-endNum) == 1)):
      slice = self.Board[endLet][endNum]
     
      if(slice[0]=="w"):
        return True


    # not incorporated
    # I thought it would be nice to have
    # :(

    # Pawn Logic -> En passant
    #not tested
    # to do En pasant Logic 

    #if(Piece == "bp" and endLet == (startLet-1)):
      
     # if(startNum == (endNum + 1)):
      #  if(self.Board[startLet][endNum+1]=="wP"):
          # handle remove "wP" Right
       #   return True

     # if(startNum == (endNum -1)):
      #  if(self.Board[startLet][endNum-1] =="wP"):
          #handle removal of "wP" Left
       #   return True
      

    # start of rook logic
    # creates if() container if selected piece is a rook

    if(Piece == R ):

      #are you moving this to an ally square, stop
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False
 
      # are you not moving like a Rook, stop
      if((startLet != endLet) and (startNum != endNum)):
        return False
   
      # handles up
      if(startLet>endLet):
        for x in range(startLet-1,endLet,-1):
          if(self.Board[x][endNum]!="--"):
            return False

        # handles down  
      if(startLet<endLet):
        for x in range(startLet+1,endLet,1):
          if(self.Board[x][endNum]!="--"):
            return False

        # handles left    
      if(startNum>endNum):
        for x in range(startNum-1,endNum,-1):
          if(self.Board[endLet][x]!="--"):
            return False

        # handles right    
      if(startNum<endNum):
        for x in range(startNum+1,endNum,1):
          if(self.Board[endLet][x]!="--"):
            return False

      return True

    # Logic for Knight

    if(Piece == K):

      # are you moving this to an ally square, stop
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False
                
      # Are you inside the chess board, if nope, don't
      if((endLet)>=0 and (endLet)<= 7 and (endNum)>=0 and (endNum)<=7):

        # comments for peice moves for K are  incorrect
        # all peices move correctly, I coded this bad 2 months ago.
        # its 1 AM I don't care right now.   

        # 2 up 1 left 
        if((startLet-endLet) == 2 and (startNum-endNum==1)):
          return True;

        # 2 Up and 1 Right
        if((startLet-endLet)==2 and (startNum-endNum==-1)):  
          print("ttt")
          return True

          # 2 left one down
        if((startLet-endLet)==-1 and (startNum-endNum==2)):
          return True

          # 2 left one up
        if((startLet-endLet)==1 and (startNum-endNum)==2 ):
          return True
        
        # 2 up 1 right
        if((startLet-endLet)==-2 and (startNum-endNum)==1 ):
          return True
        
        #2 up one left
        if((startLet-endLet)==-2 and (startNum-endNum)==-1 ):
          return True

        # 2 right 1 down
        if((startLet-endLet)==-1 and (startNum-endNum)==-2 ):
          return True

        # 
        if((startLet-endLet)==1 and (startNum-endNum)==-2 ):
          return True      
    
      return False
      
   
    #Logic for black Bishop

    if(Piece == B ):     
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # Checks to see if this is a diagonal move

      if(abs(startLet-endLet) != abs(startNum-endNum)):
      
        return False
    
        # up and to the left diagonally
      if((endLet < startLet) and (startNum > endNum)) :
        LC = 1
        for x in range(startLet-1,endLet,-1):
       
          if(self.Board[x][startNum-LC]!='--' or (startNum-LC <0)):
          #    print("your returning false stupidly dd")
            return False
          LC = LC + 1
        
        # up and to the right diagonally
      if((endLet < startLet) and (startNum < endNum)) :
        RC = 1
        for x in range(startLet-1,endLet,-1):
      
          if(self.Board[x][startNum+RC]!='--' ):
         #     print("your returning false stupidly dd4")
            return False
          
          RC = RC + 1


        # this down and to the left
      if((startLet < endLet) and (startNum > endNum)):
          
          # this used to be = endNum + 1
        LC = 1
        for x in range(startLet+1,endLet,1):
        #   

          if(self.Board[x][startNum-LC]!='--' ):
         #     print("your returning false stupidly dd")
            return False
          LC = LC + 1


        # down and to the right
      if((startLet < endLet) and startNum < endNum):
        RC = 1
        
        for x in range(startLet+1,endLet,1):
      
          if(self.Board[x][startNum+RC]!='--' ):
          #    print("your returning false stupidly dd7")
            return False
          RC = RC + 1

      return True
       
    # queen logic   

    if(Piece==Q):

      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # Checks to see if this is a diagonal move

      if(abs(startLet-endLet) == abs(startNum-endNum)):


          # up and to the left diagonally
        if((endLet < startLet) and (startNum > endNum)) :
          
          LC = 1
          for x in range(startLet-1,endLet,-1):
       
            if(self.Board[x][startNum-LC]!='--' ):
          #    print("your returning false stupidly dd")
              return False
            
            LC = LC  + 1
        
        # up and to the right diagonally
        if((endLet < startLet) and (startNum < endNum)) :
          
          RC = 1
          for x in range(startLet-1,endLet,-1):
      
            if(self.Board[x][startNum+RC]!='--' ):
         #     print("your returning false stupidly dd4")
              return False
            RC = RC + 1


        # this down and to the left
        if((startLet < endLet) and (startNum > endNum)):
          
          LC = 1 
          for x in range(startLet+1,endLet,1):
        
            if(self.Board[x][startNum-LC]!='--' ):
         
              return False
            LC = LC + 1


          # down and to the right
        if((startLet < endLet) and startNum < endNum):
          
          RC = 1
          for x in range(startLet+1,endLet,1):
      
            if(self.Board[x][startNum+RC]!='--' ):
        
              return False
            RC = RC + 1

      
        return True
        
      # start of Rook logic but for queen peice 

      if((startLet == endLet) or (startNum == endNum)):
          
        # handles up
        if(startLet>endLet):
          for x in range(startLet-1,endLet,-1):
            if(self.Board[x][endNum]!="--"):
              return False

        # handles down  
        if(startLet<endLet):
          for x in range(startLet+1,endLet,1):
            if(self.Board[x][endNum]!="--"):
              return False

        # handles left    
        if(startNum>endNum):
          for x in range(startNum-1,endNum,-1):
            if(self.Board[endLet][x]!="--"):
              return False

        # handles right    
        if(startNum<endNum):
          for x in range(startNum+1,endNum,1):
            if(self.Board[endLet][x]!="--"):
              return False

        return True
        
        # End of Queen Logic
      return False
           

    # start of king logic 
 
    if(Piece == KK):

      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # valid king moves if not a castling
      # castling checks if king is in check or moving through check
      # that would be an illegal move

      if((abs(startLet-endLet)==1 or abs(startLet-endLet)==0 )  and (abs(startNum-endNum)==1 or abs(startNum-endNum)==0)):
        
        return True   

      # Castling for White 
        
      elif(Piece[0]=="w"):
        print("00")
        if(self.Check(self.WhiteKingsPosition)!=True):
          print("11")
          if(startNum == 3 and startLet == 0  and endLet == 0 and endNum == 5 and self.Board[0][7]==R):
            
            
            print("22")
            if(self.Board[startLet][startNum+1]=="--" and self.Board[startLet][startNum+2]=="--" and self.Board[startLet][startNum+3]=="--"):
              
              print("33")
              if(self.Check([startLet,startNum+1])!=True and self.Check([startLet,startNum+2])!=True):
                
                print("44")
                self.Board[0][4]="wR"
                self.Board[0][7]="--"
                return True

          if(startNum == 3 and startLet == 0 and endLet == 0 and endNum == 1 and self.Board[0][0]==R ):
            if(self.Board[startLet][startNum-1]=="--" and self.Board[startLet][startNum-2]=="--"):
              if(self.Check([startLet,startNum-1])!=True and self.Check([startLet,startNum-2])!=True):
                self.Board[0][2]="wR"
                self.Board[0][0]="--"
                return True 

      # Castling for Black
      elif(Piece[0]=="b"):
        print("castle")
        if(self.Check(self.BlackKingsPosition)!=True):
          if(startNum == 3 and startLet == 7  and endLet == 7 and endNum == 5 and self.Board[7][7]==R):
            print("castle 2")
            if(self.Board[startLet][startNum+1]=="--" and self.Board[startLet][startNum+2]=="--" and self.Board[startLet][startNum+3]=="--"):
              
              print("castle 3")
              if(self.Check([startLet,startNum+1])!=True and self.Check([startLet,startNum+2])!=True):
                print("castle 4")
                self.Board[7][4]="bR"
                self.Board[7][7]="--"
                return True 

          if(startNum == 3 and startLet == 7 and endLet == 7 and endNum == 1 and self.Board[7][0]==R ):
            if(self.Board[startLet][startNum-1]=="--" and self.Board[startLet][startNum-2]=="--"):
              if(self.Check([startLet,startNum-1])!=True and self.Check([startLet,startNum-2])!=True):
                self.Board[7][2]="bR"
                self.Board[7][0]="--"
                return True 
      else:  
        
        return False
   
    

    # redundent False incase something ever sliped through
    # which it shouldn't
    return False
  

  # tests for Opp piece, was used a lot, not so much any more

  def OpposingPiece(self,endLet,endNum,Piece):

    EndLocPiece = self.Board[endLet][endNum]

    if(EndLocPiece[0]==Piece[0] or EndLocPiece[0]=="--"):
      return False
    else:
      return True

  # pretty much the same as opp piece function above

  def samePiece(self,endLet,endNum,Piece):

    EndLocPiece = self.Board[endLet][endNum]

    if(EndLocPiece[0]==Piece[0]):
   #   print("can't move there same piece")
      return True
    else:
      return False    

  # used to change board state
  # calls isValid before move is done
  
  def move(self,startLet,startNum,endLet,endNum):
    
    # copy important board position peices for manipulation

    Piece = copy.deepcopy(self.Board[startLet][startNum])
    previous = copy.deepcopy(self.Board[endLet][endNum])  
      
    # grabs king position depending upon piece color

    if(Piece[0]=="b"):
      KingsPositionT = copy.deepcopy(self.BlackKingsPosition)
    elif(Piece[0]=="w"):
      KingsPositionT = copy.deepcopy(self.WhiteKingsPosition)
    
    # if move selected is valid move, stop, ask for new move
    # to test if is valid again
    
    if(self.isValidMove(Piece,startLet,endLet,startNum,endNum)):
   

      # start of added check logic
      # Just because a move is valid
      # doesn't mean the move won't place the king in check.
      # if this happens return move false. Wait for new move
      # there are surprizingly 4 different situations to check for 
      # Look for <end of Check Logic> below for continuation of move logic

      if(self.Check(KingsPositionT)==True and Piece[1:]!="KK"):

        self.Board[endLet][endNum] = "$$"
        self.Board[startLet][startNum] = "--"

        if(self.Check(KingsPositionT)==False):          
            # don't do anything, this is a legal move
         
          self.Board[endLet][endNum] = previous
          self.Board[startLet][startNum] = Piece
          
        elif(self.Check(KingsPositionT)==True):
          # reset pieces to the way they were before
         
          self.Board[endLet][endNum] = previous
          self.Board[startLet][startNum] = Piece
          MoveCounter = MoveCounter - 1
          return False
        
        # if king isn't in check, does the select move then place
        # the king into check test. 
      if(self.Check(KingsPositionT)==False and Piece[1:]!="KK"):
        
        self.Board[endLet][endNum] = "$$"
        self.Board[startLet][startNum] = "--"
        
        if(self.Check(KingsPositionT)==True):          
            # don't do anything, this is a legal move
          self.Board[endLet][endNum] = previous
          self.Board[startLet][startNum] = Piece
          MoveCounter = MoveCounter - 1
          return False
      
      if(self.Check(KingsPositionT)==False and Piece[1:]=="KK"):
              
        if(Piece[0]=="w"):
            
          self.Board[endLet][endNum] = "wKK"
        if(Piece[0]=="b"):
           
          self.Board[endLet][endNum] = "bKK"
          
        MoveIntoLocation = [endLet,endNum]
        self.Board[startLet][startNum] = "--"
          
        if(self.Check(MoveIntoLocation)==True):
              
          if(Piece[0]=="w"):  
           
            self.Board[endLet][endNum] = previous
            self.Board[startLet][startNum] = "wKK"  
            
          if(Piece[0]=="b"):
           
            self.Board[endLet][endNum] = previous
            self.Board[startLet][startNum] = "bKK"
            MoveCounter = MoveCounter - 1
          return False
          
        else:

          if(Piece[0]=="w"):  
           
            self.Board[endLet][endNum] = previous
            self.Board[startLet][startNum] = "wKK"
  
          if(Piece[0]=="b"):
           
            self.Board[endLet][endNum] = previous
            self.Board[startLet][startNum] = "bKK"
                
    
      if(self.Check(KingsPositionT)==True and Piece[1:]=="KK"):
          
        print(Piece[0])
        if(Piece[0]=="w"):
           
          self.Board[endLet][endNum] = "wKK"
        
        if(Piece[0]=="b"):
           
          self.Board[endLet][endNum] = "bKK"
          
        MoveIntoLocation = [endLet,endNum]
        print(MoveIntoLocation)
        self.Board[startLet][startNum] = "--"
          
        if(self.Check(MoveIntoLocation)==True):
          
          print(self.WhiteKingsPosition)
          print(self.BlackKingsPosition)
            
          if(Piece[0]=="w"):  
           
            self.WhiteKingsPosition = [startLet,startNum]
            self.Board[endLet][endNum] = previous
            self.Board[startLet][startNum] = "wKK"
  
          if(Piece[0]=="b"):
           
            self.BlackKingsPosition = [startLet,startNum]
            self.Board[endLet][endNum] = previous
            self.Board[startLet][startNum] = "bKK"
            MoveCounter = MoveCounter - 1
          return False

        elif(self.Check(MoveIntoLocation)==False):

          if(Piece[0]=="w"):  
            self.WhiteKingsPosition = [startLet,startNum]
            self.Board[startLet][startNum] = "wKK"
            self.Board[endLet][endNum] = previous
  
          if(Piece[0]=="b"):
            self.BlackKingsPosition = [startLet,startNum]
            self.Board[startLet][startNum] = "bKK"
            self.Board[endLet][endNum] = previous

      # <end of added check logic>



      # updates the Board
      # Note the check logic above moves peices temporarily and switches
      # them back. This is so check can see through the king if needed.
      self.Board[startLet][startNum] = "--"
      self.Board[endLet][endNum] = Piece

      # if your moving the king update kings postion black
      if(Piece == "bKK"):
        self.BlackKingsPosition = [endLet,endNum]

      if(Piece == "wKK"):
        self.WhiteKingsPosition = [endLet,endNum]
          #print(self.WhiteKingsPosition)


      # Pawn promotion. Does it randomly between Q or K random choice
      if(Piece == "wP" and endLet ==7):

        kORQW = random.randint(0,1)
          
        if(kORQW == 0 ):
          self.Board[endLet][endNum] = "wQ"
        elif(kORQW == 1):
          self.Board[endLet][endNum] = "wK"

      if(Piece == "bP" and endLet ==0):
        kORQB = random.randint(0,1)
        if(kORQB == 0 ):
          self.Board[endLet][endNum] = "bQ"
        elif(kORQB == 1):
          self.Board[endLet][endNum] = "bK" 

      # Hash map code to updated individual peice location
      # tested and is still good. kept for posterity and
      # use in future improvements

      # COMMENT back in after testing 
      # hash map isn't lined up with 
      # testing hash set

      # updates black pieces hash map
      #if(Piece[0]=="b"):
      #  keyValue = (startLet * 8) + startNum
        #PieceString = self.BlackPieces.get(keyValue)
        #handles promotion
      #  PieceString = self.Board[endLet][endNum]
      #  MoveLocation = (endLet * 8) + endNum

        # Handles captures
      #  if(self.WhitePieces.get(MoveLocation)!=None):
      #    self.WhitePieces.pop(MoveLocation)
        
      #  self.BlackPieces.update({MoveLocation:PieceString})
      #  self.BlackPieces.pop(keyValue)

      # updates white pieces hash map
     # if(Piece[0]=="w"):
     #   keyValue = (startLet * 8) + startNum
        #PieceString = self.WhitePieces.get(keyValue)
        # handles promotion
     #   PieceString = self.Board[endLet][endNum]
     #   MoveLocation = (endLet * 8) + endNum

     #   if(self.BlackPieces.get(MoveLocation)!=None):
     #     self.BlackPieces.pop(MoveLocation)

      #  self.WhitePieces.update({MoveLocation:PieceString})
      #  self.WhitePieces.pop(keyValue)
     
      return True
    else:

      # move counter doesn't do anything anymore.
      # im scare to remove it. 
      # it was causing issues

      MoveCounter = MoveCounter - 1
      return False
      
      
    
  

  ## this is the start of the check testing code
 
  def Check(self,KingsPiece):

    # sets comparator peices based on players turn

    if(BoardPrint%2==0):
      self.WhiteOppPeicesCausingCheck = []
      
      KK = "bKK"
      Q = "bQ"
      R = "bR"
      K = "bK"
      B = "bB"
      P = "bP"
    
    if(BoardPrint%2==1):
      self.BlackOppPeicesCausingCheck = []
    
      KK = "wKK"
      Q = "wQ"
      R = "wR"
      K = "wK"
      B = "wB"
      P = "wP"

   
    # folling code handles Kight check
    # I forgot why I used slice...
    # I think i was playing around with readability
    # the lines were getting too long 

    if((KingsPiece[0]+2 )<=7 and (KingsPiece[1]-1)>=0 and (KingsPiece[1]-1)<=7 and (KingsPiece[0]+2)>=0):
       
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]-1]

      if(slice==K):
        print("q1")
        return True
      

    if((KingsPiece[0]+2 )<=7 and (KingsPiece[1]+1)>=0 and (KingsPiece[1]+1)<=7 and (KingsPiece[0]+2)>=0):
      
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]+1]

      if(slice==K):
        print("q2")
        return True

    if((KingsPiece[0]+1 )>=0 and (KingsPiece[1]+2)<=7 and (KingsPiece[1]+2)>=0 and (KingsPiece[0]+1)<=7):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]+2]  
      if(slice==K):
        
        return True
        

    if((KingsPiece[0]+1 )<=7 and (KingsPiece[1]-2)>=0 and (KingsPiece[1]-2)<=7 and (KingsPiece[0]+1)>=0):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]-2]  

      if(slice==K):
        
        return True
   
      
    if((KingsPiece[0]-2 )>= 0 and (KingsPiece[1]-1)>=0 and (KingsPiece[1]-1)<=7 and (KingsPiece[0]-2)<=7):
        
      slice = self.Board[(KingsPiece[0]-2)][(KingsPiece[1]-1)]
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]-1]==K):
        
        return True
  


    if((KingsPiece[0]-2 )>=0 and (KingsPiece[1]+1)<=7 and (KingsPiece[1]+1)>=0 and (KingsPiece[0]-2)<=7):
        
      slice = self.Board[KingsPiece[0]-2][KingsPiece[1]+1]

      if(slice==K):
       
        return True
   


    if((KingsPiece[0]-1 )<=7 and (KingsPiece[1]+2)<=7 and (KingsPiece[1]+2)>=0 and (KingsPiece[0]-1)>=0):

      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]+2]  

      if(slice==K):
        
        return True
    

      
    if((KingsPiece[0]-1 )>=0 and (KingsPiece[1]-2)>=0 and (KingsPiece[1]-2)<=7 and (KingsPiece[0]-1)<=7):
      
      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]-2]

      if(slice==K):
        
        return True

  
    

    # searches for rook or queen to the left of king
    for x in range(KingsPiece[1]-1,-1,-1):
      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]==Q or self.Board[KingsPiece[0]][x]==R):
          
          return True
        else:
          break  


    # searches for rook or queen to the right of king
    for x in range(KingsPiece[1]+1,8,1):
      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]==Q or self.Board[KingsPiece[0]][x]==R):
          
          return True
        else:
          break


    # searches for rook or Queen in up position 
    

    for x in range(KingsPiece[0]-1,0,-1):  
      if(self.Board[x][KingsPiece[1]]!="--"):
        if(self.Board[x][KingsPiece[1]]==Q or self.Board[x][KingsPiece[1]]==R):
         
          return True
        else:
          break 

    # searches for rook or Queen in the down positon
    for x in range(KingsPiece[0]+1,8,1):
      if(self.Board[x][KingsPiece[1]]!="--"):
        if(self.Board[x][KingsPiece[1]]==Q or self.Board[x][KingsPiece[1]]==R):
          
          return True
        else:
          break 

    # Start of handling Bishop or Queen Checks 

    # handle Bishop up and to the left

    HorizontalTracker = KingsPiece[1]
    for x in range(KingsPiece[0]-1,-1,-1):
      
      HorizontalTracker = HorizontalTracker - 1
      if(HorizontalTracker<0):
        break

      if(self.Board[x][HorizontalTracker]!="--" ):
        if(self.Board[x][HorizontalTracker]==Q or self.Board[x][HorizontalTracker]==B):
          
          return True
        else:
          break
      
             

    # handles Bishop up and to the right


    HorizontalTracker = KingsPiece[1]
    for x in range(KingsPiece[0]-1,-1,-1):
      
      HorizontalTracker = HorizontalTracker + 1
      if(HorizontalTracker>7):
        break

      if(self.Board[x][HorizontalTracker]!="--"):
        if(self.Board[x][HorizontalTracker]==Q or self.Board[x][HorizontalTracker]==B):
          
          return True
        else:
          break
     
       
        #else:
         # return False 

    # handles Bishop down and to the Right

    HorizontalTracker = KingsPiece[1]
    for x in range(KingsPiece[0]+1,8,1):
      HorizontalTracker = HorizontalTracker + 1
      if(HorizontalTracker > 7):
        
        break

      
      if(self.Board[x][HorizontalTracker]!="--" ):
        if(self.Board[x][HorizontalTracker]==Q or self.Board[x][HorizontalTracker]==B):
          
          return True
        else:
          break
        
    

    # handles Bishop down and to the Left

    HorizontalTracker = KingsPiece[1]
    for x in range(KingsPiece[0]+1,8,1):
      
      HorizontalTracker = HorizontalTracker - 1 
      if(HorizontalTracker <0):
        break
      
      if(self.Board[x][HorizontalTracker]!="--"):
        if(self.Board[x][HorizontalTracker]==Q or self.Board[x][HorizontalTracker]==B):
          
          return True
        else:
          break
        


    # Check for pawns, that can cause check
    # based on boardprint player turn number
    
    if(BoardPrint%2==0):
      if(KingsPiece[0]+1<=7 and KingsPiece[1]+1<=7):
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]==P):
          
          return True
      if(KingsPiece[0]+1<=7 and KingsPiece[1]-1>=0):
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]-1]==P):
          
          return True
    
    if(BoardPrint%2==1):
      if(KingsPiece[0]-1>=0 and KingsPiece[1]+1<=7):
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]==P):
          
          return True
      if(KingsPiece[0]-1>=0 and KingsPiece[1]-1>=0):
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]==P):
         
          return True

    # check for Opposing King
    # make sure your not violating king cant move into check

    # UL Upper left of king
    if(KingsPiece[0]-1>=0 and KingsPiece[1]-1>=0):
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]==KK):
        print("q21")
        return True

    #U  Up of King
    if(KingsPiece[0]-1>=0 and KingsPiece[1]>=0):
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]]==KK):
        print("q22")
        return True

    #UR Upper Right of king
    if(KingsPiece[0]-1>=0 and KingsPiece[1]+1<=7):
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]==KK):
        print("q23")
        return True
    
    #R Right of king
    if(KingsPiece[0]>=0 and KingsPiece[1]+1<=7):
      if(self.Board[KingsPiece[0]][KingsPiece[1]+1]==KK):
        print("q24")
        return True

    #LR  Lower right of king
    if(KingsPiece[0]+1<=7 and KingsPiece[1]+1<=7):  
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]==KK):
        print("q25")
        return True
    
    #D   Down
    if(KingsPiece[0]+1<=7 and KingsPiece[1]<=7):
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]]==KK):
        print("q26")
        return True


    #DL Down left
    if(KingsPiece[0]+1<=7 and KingsPiece[1]-1>=0):
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]-1]==KK):
        print("q27")
        return True
    
    #L left 
    if(KingsPiece[0]>=0 and KingsPiece[1]-1>=0):
      if(self.Board[KingsPiece[0]][KingsPiece[1]-1]==KK):
        print("q28")
        return True



    return False


  # called before every move, in main while Loop
  # checks to see if game is over
 
  def CheckMate(self,KingsPiece):

    # used to record safe spaces king can move to around

    PCSafeSpace = [0,0,0,0,0,0,0,0]
    #checks if king is in check before checking all 
    # other squares
    
    # moved below this was causing problems with stalemate
    # not being able to calculate PCSafeSpace
    # potential to speed up program here
    # future improvements
    #if(self.Check(KingsPiece)==False):
      #return False


    # start of PCSafeSpace logic
    # fills in a index with a 1 if king can't move there
    # looks for peices occupying square
    # and then if location causes check
    # also handles if peice are next to the edge
    # or corner
    
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
      if(KingsPiece[1]==7):  
        if(self.Board[KingsPiece[0]][KingsPiece[1]-1]!="--"):
          PCSafeSpace[7]=1
        
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]!="--"):
          PCSafeSpace[0]=1

        if(self.Board[KingsPiece[0]-1][KingsPiece[1]]!="--"):
          PCSafeSpace[1]=1
      else:

        
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
        
    
    # create deep copy so you can make 
    # 8 spaces around king to test for 0 or 1

    tempKingsPieceR = copy.deepcopy(KingsPiece)
    tempKingsPieceL = copy.deepcopy(KingsPiece)
    tempKingsPieceU = copy.deepcopy(KingsPiece)
    tempKingsPieceD = copy.deepcopy(KingsPiece)
    tempKingsPieceUL = copy.deepcopy(KingsPiece)
    tempKingsPieceUR = copy.deepcopy(KingsPiece)
    tempKingsPieceDL = copy.deepcopy(KingsPiece)
    tempKingsPieceDR = copy.deepcopy(KingsPiece)

   

    tempKingsPieceR[1] = tempKingsPieceR[1]+1
    tempKingsPieceL[1] = tempKingsPieceL[1]-1
    tempKingsPieceU[0] = tempKingsPieceU[0]-1
    tempKingsPieceD[0] = tempKingsPieceD[0]+1

    

    # make king invisible for check tests 
    # if king is not invisible, it can block
    # incoming checks, and the king can't legally
    # block a check. Following functions also first test if
    # tempKingsPiece is inside the board

    self.Board[KingsPiece[0]][KingsPiece[1]] = "--"

    if(tempKingsPieceR[1] >=0 and tempKingsPieceR[1]<=7 and tempKingsPieceR[0]>=0 and tempKingsPieceR[0]<=7):
      if(self.Check(tempKingsPieceR)):
        PCSafeSpace[3]=1
      
    if(tempKingsPieceL[1] >=0 and tempKingsPieceL[1]<=7 and tempKingsPieceL[0]>=0 and tempKingsPieceL[0]<=7):
      if(self.Check(tempKingsPieceL)):
        PCSafeSpace[7]=1
     
    if(tempKingsPieceU[0] >=0 and tempKingsPieceU[0]<=7 and tempKingsPieceU[0]>=0 and tempKingsPieceU[0]<=7):
      if(self.Check(tempKingsPieceU)):
     
        PCSafeSpace[1] = 1
     
    if(tempKingsPieceD[0] >=0 and tempKingsPieceD[0]<=7 and tempKingsPieceD[0]>=0 and tempKingsPieceD[0]<=7):
      if(self.Check(tempKingsPieceD)):
        
        PCSafeSpace[5]=1
     


    #handles UL and DL   
    
    tempKingsPieceDL[0] = tempKingsPieceDL[0]+1
    tempKingsPieceDL[1] = tempKingsPieceDL[1]-1

    tempKingsPieceUL[0] = tempKingsPieceUL[0]-1
    tempKingsPieceUL[1] = tempKingsPieceUL[1]-1
    
    # handles UR and DR
    tempKingsPieceDR[0] = tempKingsPieceDR[0]+1
    tempKingsPieceDR[1] = tempKingsPieceDR[1]+1

    tempKingsPieceUR[0] = tempKingsPieceUR[0]-1
    tempKingsPieceUR[1] = tempKingsPieceUR[1]+1

    if(tempKingsPieceUL[0] >=0 and tempKingsPieceUL[0]<=7 and tempKingsPieceUL[1] >=0 and tempKingsPieceUL[1]<=7):
     
      if(self.Check(tempKingsPieceUL)==True):
      
        PCSafeSpace[0]=1
     

    if(tempKingsPieceDL[0] >=0 and tempKingsPieceDL[0]<=7 and tempKingsPieceDL[1] >=0 and tempKingsPieceDL[1]<=7):
      if(self.Check(tempKingsPieceDL)):
        PCSafeSpace[6]=1
      
    if(tempKingsPieceUR[0] >=0 and tempKingsPieceUR[0]<=7 and tempKingsPieceUR[1] >=0 and tempKingsPieceUR[1]<=7):
      if(self.Check(tempKingsPieceUR)):
        PCSafeSpace[2]=1
     
    if(tempKingsPieceDR[0] >=0 and tempKingsPieceDR[0]<=7 and tempKingsPieceDR[1] >=0 and tempKingsPieceDR[1]<=7):
      if(self.Check(tempKingsPieceDR)):
        PCSafeSpace[4]=1
      

    # resets king. It was removed a few lines above
    # to test for check
    # this doesn't handle all king "invisilize"
    # so both kings are also both redrawn at start of 
    # move while loop

    if(BoardPrint%2==0):
      self.Board[KingsPiece[0]][KingsPiece[1]] == "wKK"
      self.whitePCsafe = PCSafeSpace


    if(BoardPrint%2==1):
      self.Board[KingsPiece[0]][KingsPiece[1]] == "bKK"
      self.blackPCsafe = PCSafeSpace
    

    if(self.Check(KingsPiece)==False):
      return False

    if(sum(PCSafeSpace)<8):
      return False
    
    if(sum(PCSafeSpace)==8):


      if(self.AvoidMate(KingsPiece)==True):
        
        return False
      else:
        return True
   
    
    # ^^^ if after move checks, king is in check
    # and has no place to move, declare checkmate
    # send this information 
    
    
    return False

  # Almost complete copy of check.
  # tests check in reverse boardprint order
  # helper method for block check
  # also tests to see if pawns can block an imposing check
  # on players king. Tests to see if blocking move also
  # doesn't place king back into check.  

  def RevCheck(self,KingsPiece):

    if(BoardPrint%2==1):
      self.WhiteOppPeicesCausingCheck = []
      CurrentKing = copy.deepcopy(self.BlackKingsPosition)
      KK = "bKK"
      Q = "bQ"
      R = "bR"
      K = "bK"
      B = "bB"
      P = "bP"
    
    if(BoardPrint%2==0):
      self.BlackOppPeicesCausingCheck = []
      CurrentKing = copy.deepcopy(self.WhiteKingsPosition)
      KK = "wKK"
      Q = "wQ"
      R = "wR"
      K = "wK"
      B = "wB"
      P = "wP"


    # looks for kight kills

    if((KingsPiece[0]+2 )<=7 and (KingsPiece[1]-1)>=0 and (KingsPiece[1]-1)<=7 and (KingsPiece[0]+2)>=0):
       
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]-1]

      if(slice==K):

        return True
        
  


    if((KingsPiece[0]+2 )<=7 and (KingsPiece[1]+1)>=0 and (KingsPiece[1]+1)<=7 and (KingsPiece[0]+2)>=0):
      
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]+1]

      if(slice==K):
       
        return True

    if((KingsPiece[0]+1 )>=0 and (KingsPiece[1]+2)<=7 and (KingsPiece[1]+2)>=0 and (KingsPiece[0]+1)<=7):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]+2]  
      if(slice==K):
        
        return True
       

    if((KingsPiece[0]+1 )<=7 and (KingsPiece[1]-2)>=0 and (KingsPiece[1]-2)<=7 and (KingsPiece[0]+1)>=0):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]-2]  

      if(slice==K):
        
        return True
   
      
    if((KingsPiece[0]-2 )>= 0 and (KingsPiece[1]-1)>=0 and (KingsPiece[1]-1)<=7 and (KingsPiece[0]-2)<=7):
        
      slice = self.Board[(KingsPiece[0]-2)][(KingsPiece[1]-1)]
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]-1]==K):
        
        return True


    if((KingsPiece[0]-2 )>=0 and (KingsPiece[1]+1)<=7 and (KingsPiece[1]+1)>=0 and (KingsPiece[0]-2)<=7):
        
      slice = self.Board[KingsPiece[0]-2][KingsPiece[1]+1]

      if(slice==K):
    
        return True

    if((KingsPiece[0]-1 )<=7 and (KingsPiece[1]+2)<=7 and (KingsPiece[1]+2)>=0 and (KingsPiece[0]-1)>=0):

      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]+2]  

      if(slice==K):
        
        return True
      
    if((KingsPiece[0]-1 )>=0 and (KingsPiece[1]-2)>=0 and (KingsPiece[1]-2)<=7 and (KingsPiece[0]-1)<=7):
      
      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]-2]

      if(slice==K):
       
        return True

    # searches for rook or queen to the left of king
    for x in range(KingsPiece[1]-1,-1,-1):     

      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]==Q or self.Board[KingsPiece[0]][x]==R):
         
          # removal logic, checks to see if king is in check
          # by block
          # this code is reused alot but variated from here 
          # down 

          tempPSave = copy.deepcopy(self.Board[KingsPiece[0]][x])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[KingsPiece[0]][x] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
          if(self.Check(CurrentKing)==True):  
            self.Board[KingsPiece[0]][x] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            continue

          self.Board[KingsPiece[0]][x] = tempPSave  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

          return True
        else:
          break  

    # searches for rook or queen to the right of king
    for x in range(KingsPiece[1]+1,8,1):
          
      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]==Q or self.Board[KingsPiece[0]][x]==R):
         
          tempPSave = copy.deepcopy(self.Board[KingsPiece[0]][x])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[KingsPiece[0]][x] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
          if(self.Check(CurrentKing)==True):  
            self.Board[KingsPiece[0]][x] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            continue

          self.Board[KingsPiece[0]][x] = tempPSave  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

          return True
        else:
          break


    # searches for rook or Queen in up position 

    for x in range(KingsPiece[0]-1,0,-1):  
   
      if(self.Board[x][KingsPiece[1]]!="--"):
        if(self.Board[x][KingsPiece[1]]==Q or self.Board[x][KingsPiece[1]]==R):

          tempPSave = copy.deepcopy(self.Board[x][KingsPiece[1]])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[x][KingsPiece[1]] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
          if(self.Check(CurrentKing)==True):  
            self.Board[x][KingsPiece[1]] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            continue

          self.Board[x][KingsPiece[1]] = tempPSave  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

          return True
        else:
          break 

    # searches for rook or Queen in the down positon
    for x in range(KingsPiece[0]+1,8,1):
      if(self.Board[x][KingsPiece[1]]!="--"):
        if(self.Board[x][KingsPiece[1]]==Q or self.Board[x][KingsPiece[1]]==R):
          print("q12")

          tempPSave = copy.deepcopy(self.Board[x][KingsPiece[1]])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[x][KingsPiece[1]] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
          if(self.Check(CurrentKing)==True):  
            self.Board[x][KingsPiece[1]] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            continue

          self.Board[x][KingsPiece[1]] = tempPSave  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

          return True
        else:
          break 

    # handles Bishop or Queen Checks 

    # handle Bishop up and to the left

    HorizontalTracker = KingsPiece[1]
    for x in range(KingsPiece[0]-1,-1,-1):
      
      HorizontalTracker = HorizontalTracker - 1
      if(HorizontalTracker<0):
        break      

      if(self.Board[x][HorizontalTracker]!="--" ):
        if(self.Board[x][HorizontalTracker]==Q or self.Board[x][HorizontalTracker]==B):
          print("q13")

          tempPSave = copy.deepcopy(self.Board[x][HorizontalTracker])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[x][HorizontalTracker] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
          if(self.Check(CurrentKing)==True):  
            self.Board[x][HorizontalTracker] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            continue

          self.Board[x][HorizontalTracker] = tempPSave  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

          return True
        else:
          break
      
    # handles Bishop up and to the right

    HorizontalTracker = KingsPiece[1]
    for x in range(KingsPiece[0]-1,-1,-1):
      
      HorizontalTracker = HorizontalTracker + 1
      if(HorizontalTracker>7):
        break

      if(self.Board[x][HorizontalTracker]!="--"):
        if(self.Board[x][HorizontalTracker]==Q or self.Board[x][HorizontalTracker]==B):

          tempPSave = copy.deepcopy(self.Board[x][HorizontalTracker])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[x][HorizontalTracker] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
          if(self.Check(CurrentKing)==True):  
            self.Board[x][HorizontalTracker] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            continue

          self.Board[x][HorizontalTracker] = tempPSave  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2
          
          return True
        else:
          break

    # handles Bishop down and to the Right
   
    HorizontalTracker = KingsPiece[1]
    print(KingsPiece[0])
    print(HorizontalTracker)
    for x in range(KingsPiece[0]+1,8,1):

      HorizontalTracker = HorizontalTracker + 1  
      if(HorizontalTracker > 7):
        
        break

      if(self.Board[x][HorizontalTracker]!="--" ):
        if(self.Board[x][HorizontalTracker]==Q or self.Board[x][HorizontalTracker]==B):

          tempPSave = copy.deepcopy(self.Board[x][HorizontalTracker])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[x][HorizontalTracker] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
          if(self.Check(CurrentKing)==True):  
            self.Board[x][HorizontalTracker] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            continue

          self.Board[x][HorizontalTracker] = tempPSave  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

          return True
        else:
          break

    # handles Bishop down and to the Left

    HorizontalTracker = KingsPiece[1]
    for x in range(KingsPiece[0]+1,8,1):
      
      HorizontalTracker = HorizontalTracker - 1 
      if(HorizontalTracker <0):
        break
    
      if(self.Board[x][HorizontalTracker]!="--"):
        if(self.Board[x][HorizontalTracker]==Q or self.Board[x][HorizontalTracker]==B):

          tempPSave = copy.deepcopy(self.Board[x][HorizontalTracker])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[x][HorizontalTracker] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
          if(self.Check(CurrentKing)==True):  
            self.Board[x][HorizontalTracker] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            continue

          self.Board[x][HorizontalTracker] = tempPSave  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

          return True
        else:
          break
        
    # Check for pawns jjj
    if(self.Board[KingsPiece[0]][KingsPiece[1]]!="--"):
      if(BoardPrint%2==1):
        if(KingsPiece[0]+1<=7 and KingsPiece[1]+1<=7):
          if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]==P):

            tempPSave = copy.deepcopy(self.Board[KingsPiece[0]+1][KingsPiece[1]+1])
            tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
            self.Board[KingsPiece[0]+1][KingsPiece[1]+1] = "--"  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
            if(self.Check(CurrentKing)==True):  
              self.Board[KingsPiece[0]+1][KingsPiece[1]+1] = tempPSave  
              self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2
            else:
              self.Board[KingsPiece[0]+1][KingsPiece[1]+1] = tempPSave  
              self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2   
              return True
               
        if(KingsPiece[0]+1<=7 and KingsPiece[1]-1>=0):
          if(self.Board[KingsPiece[0]+1][KingsPiece[1]-1]==P):

            tempPSave = copy.deepcopy(self.Board[KingsPiece[0]+1][KingsPiece[1]-1])
            tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
            self.Board[KingsPiece[0]+1][KingsPiece[1]-1] = "--"  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
            if(self.Check(CurrentKing)==True):  
              self.Board[KingsPiece[0]+1][KingsPiece[1]-1] = tempPSave  
              self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2
            else:
              self.Board[KingsPiece[0]+1][KingsPiece[1]-1] = tempPSave  
              self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2   
              return True
  
      if(BoardPrint%2==0):
        if(KingsPiece[0]-1>=0 and KingsPiece[1]+1<=7):
          if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]==P):

            tempPSave = copy.deepcopy(self.Board[KingsPiece[0]-1][KingsPiece[1]+1])
            tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
            self.Board[KingsPiece[0]-1][KingsPiece[1]+1] = "--"  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
            if(self.Check(CurrentKing)==True):  
              self.Board[KingsPiece[0]-1][KingsPiece[1]+1] = tempPSave  
              self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2
            else:
              self.Board[KingsPiece[0]-1][KingsPiece[1]+1] = tempPSave  
              self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2   
              return True

        if(KingsPiece[0]-1>=0 and KingsPiece[1]-1>=0):
          if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]==P):
            
            tempPSave = copy.deepcopy(self.Board[KingsPiece[0]-1][KingsPiece[1]-1])
            tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
            self.Board[KingsPiece[0]-1][KingsPiece[1]-1] = "--"  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave   
          
            if(self.Check(CurrentKing)==True):  
              self.Board[KingsPiece[0]-1][KingsPiece[1]-1] = tempPSave  
              self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2
            else:
              self.Board[KingsPiece[0]-1][KingsPiece[1]-1] = tempPSave  
              self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2   
              return True          

    # check for Opposing King
    # UL
    
    if(KingsPiece[0]-1>=0 and KingsPiece[1]-1>=0):
     
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]==KK):
        
        return True
    #U
    if(KingsPiece[0]-1>=0 and KingsPiece[1]>=0):
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]]==KK):
        
        return True

    #UR
    if(KingsPiece[0]-1>=0 and KingsPiece[1]+1<=7):
      if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]==KK):
        
        return True
    
    #R
    if(KingsPiece[0]>=0 and KingsPiece[1]+1<=7):
      if(self.Board[KingsPiece[0]][KingsPiece[1]+1]==KK):
        
        return True

    #LR
    if(KingsPiece[0]+1<=7 and KingsPiece[1]+1<=7):  
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]==KK):
       
        return True
    
    #D
    if(KingsPiece[0]+1<=7 and KingsPiece[1]<=7):
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]]==KK):
       
        return True

    #DL
    if(KingsPiece[0]+1<=7 and KingsPiece[1]-1>=0):
      if(self.Board[KingsPiece[0]+1][KingsPiece[1]-1]==KK):
        
        return True
    
    #L
    if(KingsPiece[0]>=0 and KingsPiece[1]-1>=0):
      if(self.Board[KingsPiece[0]][KingsPiece[1]-1]==KK):
       
        return True

    if(BoardPrint%2==1):
      
      if(KingsPiece[0]+1<8):

        if(self.Board[KingsPiece[0]+1][KingsPiece[1]]==P):

          tempPSave = copy.deepcopy(self.Board[KingsPiece[0]+1][KingsPiece[1]])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[KingsPiece[0]+1][KingsPiece[1]] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave

          if(self.Check(CurrentKing)==True):
            self.Board[KingsPiece[0]+1][KingsPiece[1]] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2
          else:
            self.Board[KingsPiece[0]+1][KingsPiece[1]] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            return True

    if(BoardPrint%2==0):
     
      if(KingsPiece[0]-1>-1):
 
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]]==P):
        
          tempPSave = copy.deepcopy(self.Board[KingsPiece[0]-1][KingsPiece[1]])
          tempPSave2 = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
          self.Board[KingsPiece[0]-1][KingsPiece[1]] = "--"  
          self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave

          if(self.Check(CurrentKing)==True):
            self.Board[KingsPiece[0]-1][KingsPiece[1]] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2
          else:
            self.Board[KingsPiece[0]-1][KingsPiece[1]] = tempPSave  
            self.Board[KingsPiece[0]][KingsPiece[1]] = tempPSave2

            return True

    return False

  # is it possible to avoid mate
  # creates a list with all peices attacking king
  # then calls block check on opposing peices 

  def AvoidMate(self,KingsPiece):

    # also sets comparator peices 
    if(BoardPrint%2==0):
      self.WhiteOppPeicesCausingCheck = []
      OppPeices = self.WhiteOppPeicesCausingCheck
      KK = "bKK"
      Q = "bQ"
      R = "bR"
      K = "bK"
      B = "bB"
      P = "bP"
  
    if(BoardPrint%2==1):
      self.BlackOppPeicesCausingCheck = []
      OppPeices = self.BlackOppPeicesCausingCheck
      KK = "wKK"
      Q = "wQ"
      R = "wR"
      K = "wK"
      B = "wB"
      P = "wP"
    

    #Search for all opponent peices on board that are attacking king
    # 

    if((KingsPiece[0]+2 )<= 7 and (KingsPiece[1]-1)>=0 and (KingsPiece[1]-1)<=7 and (KingsPiece[0]+2)>=0):
       
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]-1]

      if(slice==K):
        OppPeices.append([KingsPiece[0]+2,KingsPiece[1]-1])
        


    if((KingsPiece[0]+2 )<=7 and (KingsPiece[1]+1)<=7 and (KingsPiece[1]+1)>=0 and (KingsPiece[0]+2)>=0):
      
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]+1]

      if(slice==K):
        OppPeices.append([KingsPiece[0]+2,KingsPiece[1]+1])
   


    if((KingsPiece[0]+1 )<=7 and (KingsPiece[1]+2)<=7 and (KingsPiece[1]+2)>=0 and (KingsPiece[0]+1)>=0):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]+2]  
      if(slice==K):
        OppPeices.append([KingsPiece[0]+1,KingsPiece[1]+2])
        

    if((KingsPiece[0]+1 )<=7 and (KingsPiece[1]-2)<=7 and (KingsPiece[1]-2)>=0 and (KingsPiece[0]+1)>=0):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]-2]  

      if(slice==K):
        OppPeices.append([KingsPiece[0]+1,KingsPiece[1]-2])
   
      
    if((KingsPiece[0]-2 )<=7 and (KingsPiece[1]-1)<=7 and (KingsPiece[1]-1)>=0 and (KingsPiece[0]-2)>=0):
        
      slice = self.Board[(KingsPiece[0]-2)][(KingsPiece[1]-1)]
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]-1]==K):
        
        OppPeices.append([KingsPiece[0]-2,KingsPiece[1]-1])
  

    if((KingsPiece[0]-2 )<=7 and (KingsPiece[1]+1)<=7 and (KingsPiece[1]+1)>=0 and (KingsPiece[0]-2)>=0):
        
      slice = self.Board[KingsPiece[0]-2][KingsPiece[1]+1]

      if(slice==K):
        OppPeices.append([KingsPiece[0]-2,KingsPiece[1]+1])
   

    if((KingsPiece[0]-1 )<=7 and (KingsPiece[1]+2)<=7 and (KingsPiece[1]+2)>=0and (KingsPiece[0]-1)>=0):

      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]+2]  

      if(slice==K):
        OppPeices.append([KingsPiece[0]-1,KingsPiece[1]+2])
    
      
    if((KingsPiece[0]-1 )<=7 and (KingsPiece[1]-2)<=7 and (KingsPiece[1]-2)>=0 and (KingsPiece[0]-1)>=0):
      
      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]-2]

      if(slice==K):
        OppPeices.append([KingsPiece[0]-1,KingsPiece[1]-2])

    # searches for rook or queen to the left of king
    for x in range(KingsPiece[1]-1,-1,-1):
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
    
    for x in range(KingsPiece[1]+1,8,1):
      if(self.Board[KingsPiece[0]][x]!="--"):

        slice = self.Board[KingsPiece[0]][x]
        if(slice==Q):
          OppPeices.append([KingsPiece[0],x])
          
        elif(slice==R):
          OppPeices.append([KingsPiece[0],x])
        
        break

    # searches for rook or Queen in up position 

    for x in range(KingsPiece[0]-1,-1,-1):  
      if(self.Board[x][KingsPiece[1]]!="--"):

        slice = self.Board[x][KingsPiece[1]]
        
        if(slice==Q): 
     
          OppPeices.append([x,KingsPiece[1]])
        
        elif(slice==R):
          OppPeices.append([x,KingsPiece[1]])
       
        break
    
    # searches for rook or Queen in the down positon
    for x in range(KingsPiece[0]+1,8,1):
      if(self.Board[x][KingsPiece[1]]!="--"):
        slice = self.Board[x][KingsPiece[1]]
        if(slice==Q): 
   
          OppPeices.append([x,KingsPiece[1]])
        elif(slice==R):
 
          OppPeices.append([x,KingsPiece[1]])
        break
    
    
    # handles Bishop and Queen Checks 
    # handle Bishop up and to the left

    HorizontalTracker =  KingsPiece[1]
    for x in range(KingsPiece[0]-1,-1,-1):
      
      HorizontalTracker = HorizontalTracker - 1
      if(HorizontalTracker<0):
        break
      
      if(self.Board[x][HorizontalTracker]!="--"):

        slice = self.Board[x][HorizontalTracker]
        if(slice==Q): 
          OppPeices.append([x,HorizontalTracker])
        elif(slice==B):
          OppPeices.append([x,HorizontalTracker])
        break   
   
    # handles Bishop up and to the right

    HorizontalTracker =  KingsPiece[1]
    for x in range(KingsPiece[0]-1,-1,-1):
      HorizontalTracker = HorizontalTracker + 1
      
      if(HorizontalTracker > 7):
        break

      if(self.Board[x][HorizontalTracker]!="--"):

        slice = self.Board[x][HorizontalTracker]
        if(slice==Q): 
          OppPeices.append([x,HorizontalTracker])
        elif(slice==B):
          OppPeices.append([x,HorizontalTracker])
        break

    # handles Bishop down and to the Right

    HorizontalTracker = KingsPiece[1]
    for x in range(KingsPiece[0]+1,8,1):

      HorizontalTracker = HorizontalTracker + 1    
      if(HorizontalTracker > 7):
        break

      if(self.Board[x][HorizontalTracker]!="--"):
          
        slice = self.Board[x][HorizontalTracker] 
        if(slice==Q): 
          OppPeices.append([x,HorizontalTracker])
        elif(slice==B):
          OppPeices.append([x,HorizontalTracker])
        break
      

    # handles Bishop down and to the Left

    HorizontalTracker =  KingsPiece[1]
    for x in range(KingsPiece[0]+1,8,1):

      HorizontalTracker = HorizontalTracker - 1
      if(HorizontalTracker < 0):
        break
      
      if(self.Board[x][HorizontalTracker]!="--"):

        slice = self.Board[x][HorizontalTracker]
        if(slice==Q): 
          OppPeices.append([x,HorizontalTracker])
          
        elif(slice==B):
          OppPeices.append([x,HorizontalTracker])
        break
     

    # HANDLE PAWNS

    if(BoardPrint%2==0):
      
      # down and right pawn check: White king
      if((KingsPiece[0]+1)<=7 and (KingsPiece[1]+1)<=7):
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]==P):
          OppPeices.append(KingsPiece[0]+1,KingsPiece[1]+1)
      
      # down and left pawn check: White King
      if((KingsPiece[0]+1)<=7 and (KingsPiece[1]-1)>=0):
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]-1]==P):
          OppPeices.append(KingsPiece[0]+1,KingsPiece[1]-1)


    if(BoardPrint%2==1):

      # up and right pawn check : Black King  
      if(KingsPiece[0]-1>=0 and KingsPiece[1]+1<=7):
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]==P):
          OppPeices.append([KingsPiece[0]-1,KingsPiece[1]+1])

      # up and left pawn check : Black King
      if(KingsPiece[0]-1>=0 and KingsPiece[1]-1>=0):
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]==P):
          OppPeices.append([KingsPiece[0]-1,KingsPiece[1]-1])
    
    
    
    if(len(OppPeices)>=2 ):
  #    print("Can't block 2+ peices")
      # I think its possible to have 3 checks? look up 
      return False
  

    if(len(OppPeices)==1):
      # pulls peice causing check on king 
      TestPeice = OppPeices[0]
      
    # if you cant block the check return false
    # this signifys a check mate and the game ends
      
      if(self.BlockCheck(TestPeice)==True):
        
        print("Block check True")
        
       
        return True

     
    
    return False    

  
  # see if its possible to block a check by moving a peice

  def BlockCheck(self,TestPeice):

    OppPeiceString = self.Board[TestPeice[0]][TestPeice[1]]
    print(OppPeiceString)
    OppPeiceColor = OppPeiceString[0]

    if(OppPeiceColor=="w"):
      KingsPiece = self.BlackKingsPosition
    if(OppPeiceColor=="b"):
      KingsPiece = self.WhiteKingsPosition

  
    OppPeiceType = OppPeiceString[1:]

    # tests to see if king can kill attacking piece
    if((abs(KingsPiece[0]-TestPeice[0])==1 or abs(KingsPiece[0]-TestPeice[0])==0 ) and (abs(KingsPiece[1]-TestPeice[1])==1 or abs(KingsPiece[1]-TestPeice[1])==0           )):
        
        saveTempPeiceString = copy.deepcopy(self.Board[TestPeice[0]][TestPeice[1]])
        saveKingPeiceString = copy.deepcopy(self.Board[KingsPiece[0]][KingsPiece[1]])
        self.Board[KingsPiece[0]][KingsPiece[1]] == "--"
        self.Board[TestPeice[0]][TestPeice[1]] = saveKingPeiceString

        if(OppPeiceColor=="w"):
          KingsPiece = copy.deepcopy(self.BlackKingsPosition)
          self.BlackKingsPosition = [TestPeice[0],TestPeice[1]]
        if(OppPeiceColor=="b"):
          KingsPiece = copy.deepcopy(self.WhiteKingsPosition)
          self.BlackKingsPosition = [TestPeice[0],TestPeice[1]]
        
        #check is working on the kings position and not the newly
        #upadated one 
        
        # TestPiece is switched to the KingsPiece
        
        if(self.Check(TestPeice)!=True):
          
          self.Board[TestPeice[0]][TestPeice[1]] = saveTempPeiceString
          self.Board[KingsPiece[0]][KingsPiece[1]] = saveKingPeiceString
          
          #reset kings gravity location back to original
          if(OppPeiceColor=="w"):
            
            self.BlackKingsPosition = KingsPiece
          if(OppPeiceColor=="b"):
            
            self.BlackKingsPosition = KingsPiece
          
          return True
        else:

          self.Board[TestPeice[0]][TestPeice[1]] = saveTempPeiceString
          self.Board[KingsPiece[0]][KingsPiece[1]] = saveKingPeiceString  

          #reset kings gravity locaiton back to original
          if(OppPeiceColor=="w"):
            
            self.BlackKingsPosition = KingsPiece
          if(OppPeiceColor=="b"):
            
            self.BlackKingsPosition = KingsPiece
          # removed the return statment not sure if its needed
          # doesn't seem like it needs to be 
          

    # tests if peice is a knight 

    if(OppPeiceType == "K"):
      if(self.RevCheck(TestPeice)==True):
  
        return True
      else: 
        return False

    # tests if peices is Rook 
    
    if(OppPeiceType == "R"):

      # to the left
      if(KingsPiece[0]==TestPeice[0]):
        if(KingsPiece[1]>TestPeice[1]):
     
          for x in range(KingsPiece[1]-1,TestPeice[1]-1,-1):

            # bounds check
            if(x<0):
              return False

            if(self.RevCheck([KingsPiece[0],x])==True):
              return True  
          return False

        # to the right 
        if(KingsPiece[1]<TestPeice[1]):
          for x in range(KingsPiece[1]+1,TestPeice[1]+1,1):
            if(self.RevCheck([KingsPiece[0],x])==True):
              return True  
          return False


      # tests up and down for rook
      if(KingsPiece[1]==TestPeice[1]):

        # tests up
        if(KingsPiece[0]>TestPeice[0]):
          for x in range(KingsPiece[0]-1,TestPeice[0]-1,-1):

            if(x<0):
              return False
            if(self.RevCheck([x,KingsPiece[1]])==True):
              return True  
          return False

        # tests down
        if(KingsPiece[0]<TestPeice[0]):
          for x in range(KingsPiece[0]+1,TestPeice[0]+1,1):
            if(self.RevCheck([x,KingsPiece[1]])==True):
              return True  
          return False
      
      return False


    # test Bishops type piece 
    if(OppPeiceType == "B"):

      if(KingsPiece[0]>TestPeice[0]):
        # bishop up and to the right
        HorizontalTracking = KingsPiece[1]

        if(KingsPiece[1]<TestPeice[1]):

          HorizontalTracking = HorizontalTracking + 1

          for x in range(KingsPiece[0]-1,TestPeice[0]-1,-1):

            if(HorizontalTracking > 7):
              return False
            if(self.RevCheck([x,HorizontalTracking])):
              return True
            HorizontalTracking = HorizontalTracking + 1
          return False
          
        # bishop up and to the left  
        HorizontalTracking = KingsPiece[1]

        if(KingsPiece[1]>TestPeice[1]):
          
          HorizontalTracking = HorizontalTracking - 1

          for x in range(KingsPiece[0]-1,TestPeice[0]-1,-1):

            if(HorizontalTracking<0):
              return False
            
            if(self.RevCheck([x,HorizontalTracking])):
             
              return True
            
            HorizontalTracking = HorizontalTracking - 1
          return False

      # Bishop logic down and to the left

      if(KingsPiece[0]<TestPeice[0]):
        
        # down and to the left 
        HorizontalTracking = KingsPiece[1]

        if(KingsPiece[1]>TestPeice[1]):
          HorizontalTracking = HorizontalTracking - 1

          for x in range(KingsPiece[0]+1,TestPeice[1]+1,1):
            
            if(HorizontalTracking<0):
              return False

            if(self.RevCheck([x,HorizontalTracking])):
              return True
            HorizontalTracking = HorizontalTracking -1
          return False

        # down and to the right 
        HorizontalTracking = KingsPiece[1]

        if(KingsPiece[1]<TestPeice[1]):
          HorizontalTracking = HorizontalTracking + 1
          if(HorizontalTracking>7):
            return False

          for x in range(KingsPiece[0]+1,TestPeice[0]+1,1):
            if(self.RevCheck([x,HorizontalTracking])):
          
              return True
            HorizontalTracking = HorizontalTracking + 1
          
          return False
      
      return False 

    # tests if opp peice is a Queen 

    if(OppPeiceType == "Q"):
      #bishop logic for check block

      if(KingsPiece[0]>TestPeice[0]):
        # bishop up and to the right

        HorizontalTracker = KingsPiece[1]
        if(KingsPiece[1]<TestPeice[1]):
          
          HorizontalTracker = HorizontalTracker + 1
          for x in range(KingsPiece[0]-1,TestPeice[1]-1,-1):

            if(HorizontalTracker>7):
              return False
            if(self.RevCheck([x,HorizontalTracker])):
              return True
            HorizontalTracker = HorizontalTracker + 1
          return False
          
        # bishop up and to the left   
        HorizontalTracker = KingsPiece[1]
        if(KingsPiece[1]>TestPeice[1]):
          
          HorizontalTracker = HorizontalTracker - 1
          if(HorizontalTracker<0):
            return False

          for x in range(KingsPiece[0]-1,TestPeice[0]-1,-1):
            if(self.RevCheck([x,HorizontalTracker])):
              return True
            HorizontalTracker = HorizontalTracker - 1
          return False

      # Bishop logic down and to the left

      HorizontalTracker = KingsPiece[1]
      if(KingsPiece[0]<TestPeice[0]):
        
        if(KingsPiece[1]>TestPeice[1]):
          HorizontalTracker = HorizontalTracker - 1
          if(HorizontalTracker <0):
            return False
          for x in range(KingsPiece[0]+1,TestPeice[0]+1,1):
            if(self.RevCheck([x,HorizontalTracker])):
              return True
            HorizontalTracker = HorizontalTracker - 1
          return False

        # down and to the right
        HorizontalTracker = KingsPiece[1]
        if(KingsPiece[1]<TestPeice[1]):
          HorizontalTracker = HorizontalTracker + 1
          if(HorizontalTracker>7):
            return False
          for x in range(KingsPiece[0]+1,TestPeice[1]+1,1):
            if(self.RevCheck([x,HorizontalTracker])):
              return True
            return False

      #rook logic for check block

      # to the left
      if(KingsPiece[0]==TestPeice[0]):
        if(KingsPiece[1]>TestPeice[1]):
          
          for x in range(KingsPiece[1]-1,TestPeice[1]-1,-1):

            # bounds check
            if(x<0):
              return False

            if(self.RevCheck([KingsPiece[0],x])==True):
              return True  
          return False

        # to the right 
        if(KingsPiece[1]<TestPeice[1]):
          for x in range(KingsPiece[1]+1,TestPeice[1]+1,1):
            if(self.RevCheck([KingsPiece[0],x])==True):
              print("fvf")
              return True  
          return False

      # tests up and down for rook
      if(KingsPiece[1]==TestPeice[1]):

        # tests up
        if(KingsPiece[0]>TestPeice[0]):
          for x in range(KingsPiece[0]-1,TestPeice[0]-1,-1):

            if(x<0):
              return False
            if(self.RevCheck([x,KingsPiece[1]])==True):
              return True  
          return False

        # tests down
        if(KingsPiece[0]<TestPeice[0]):
          for x in range(KingsPiece[0]+1,TestPeice[0]+1,1):
            if(self.RevCheck([x,KingsPiece[1]])==True):
              return True  
          return False
      
      return False    

    # checks if opp peices is a pawn 
    if(OppPeiceString == "bP"):

      if(self.RevCheck(TestPeice)==True):
        return True
      else:
        return False
      
      
     

    if(OppPeiceString == "wP"):

      print("wP test ")
      if(self.RevCheck(TestPeice)==True):
        print("wp was true")
        return True
      else:
        False

    return False

  # This Function is Future Functionality

  def CheckReturnPiece(self, ComparePiece ):

  # Location retuns a
  # of the pieces that can stop a check, form
  # a specific piece.
  # this is needed so that, if a peice can 
  # stop check. But then places the king, in check.
  # this information is needed to be sent back up
  # into block check
  
    
    Location = []


    if(BoardPrint%2==0):
      self.WhiteOppPeicesCausingCheck = []
      
      KK = "bKK"
      Q = "bQ"
      R = "bR"
      K = "bK"
      B = "bB"
      P = "bP"
    #0print(ColorOfKing[0])
    if(BoardPrint%2==1):
      self.BlackOppPeicesCausingCheck = []
    
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
    
    

    if((KingsPiece[0]+2 )<=7 and (KingsPiece[1]-1)>=0 and (KingsPiece[1]-1)<=7 and (KingsPiece[0]+2)>=0):
       
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]-1]

      if(slice==K):
        Location.append([KingsPiece[0]+2,KingsPiece[1]-1])
        
  


    if((KingsPiece[0]+2 )<=7 and (KingsPiece[1]+1)>=0 and (KingsPiece[1]+1)<=7 and (KingsPiece[0]+2)>=0):
      
      slice = self.Board[KingsPiece[0]+2][KingsPiece[1]+1]

      if(slice==K):
        Location.append(KingsPiece[0]+2,KingsPiece[1]+1)
   


    if((KingsPiece[0]+1 )>=0 and (KingsPiece[1]+2)<=7 and (KingsPiece[1]+2)>=0 and (KingsPiece[0]+1)<=7):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]+2]  
      if(slice==K):
        Location.append([KingsPiece[0]+1,KingsPiece[1]+2])
        
   

  

    if((KingsPiece[0]+1 )<=7 and (KingsPiece[1]-2)>=0 and (KingsPiece[1]-2)<=7 and (KingsPiece[0]+1)>=0):
        
      slice = self.Board[KingsPiece[0]+1][KingsPiece[1]-2]  

      if(slice==K):
        Location.append([KingsPiece[0]+1,KingsPiece[1]-2] )
   



      
    if((KingsPiece[0]-2 )>= 0 and (KingsPiece[1]-1)>=0 and (KingsPiece[1]-1)<=7 and (KingsPiece[0]-2)<=7):
        
      slice = self.Board[(KingsPiece[0]-2)][(KingsPiece[1]-1)]
      if(self.Board[KingsPiece[0]-2][KingsPiece[1]-1]==K):
        
        Location.append([KingsPiece[0]-2,KingsPiece[1]-1])
  


    if((KingsPiece[0]-2 )>=0 and (KingsPiece[1]+1)<=7 and (KingsPiece[1]+1)>=0 and (KingsPiece[0]-2)<=7):
        
      slice = self.Board[KingsPiece[0]-2][KingsPiece[1]+1]

      if(slice==K):
        Location.append([KingsPiece[0]-2,KingsPiece[1]+1])
   


    if((KingsPiece[0]-1 )<=7 and (KingsPiece[1]+2)<=7 and (KingsPiece[1]+2)>=0 and (KingsPiece[0]-1)>=0):

      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]+2]  

      if(slice==K):
        Location.append([KingsPiece[0]-1,KingsPiece[1]+2])
    

      
    if((KingsPiece[0]-1 )>=0 and (KingsPiece[1]-2)>=0 and (KingsPiece[1]-2)<=7 and (KingsPiece[0]-1)<=7):
      
      slice = self.Board[KingsPiece[0]-1][KingsPiece[1]-2]

      if(slice==K):
        Location.append([KingsPiece[0]-1,KingsPiece[1]-2])

  
    # might need to switch the 7 to an 8 so that its inclusive

    #print("checking check")

    # searches for rook or queen to the left of king
    for x in range(KingsPiece[1]-1,-1,-1):
      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]==Q or self.Board[KingsPiece[0]][x]==R):
          #print("Q 1")
          Location.append([KingsPiece[0],x])
          break
        else:
          break  
#7777

    # searches for rook or queen to the right of king
    for x in range(KingsPiece[1]+1,8,1):
      if(self.Board[KingsPiece[0]][x]!="--"):
        if(self.Board[KingsPiece[0]][x]==Q or self.Board[KingsPiece[0]][x]==R):
          #print("Q 2")
          Location.append([KingsPiece[0],x])
          break
        else:
          break


    # searches for rook or Queen in up position 
    

    for x in range(KingsPiece[0]-1,0,-1):  
      if(self.Board[x][KingsPiece[1]]!="--"):
        if(self.Board[x][KingsPiece[1]]==Q or self.Board[x][KingsPiece[1]]==R):
         # print("Q 3")
          Location.append([x,KingsPiece[1]])
          break
        else:
          break 

    # searches for rook or Queen in the down positon
    for x in range(KingsPiece[0]+1,8,1):
      if(self.Board[x][KingsPiece[1]]!="--"):
        if(self.Board[x][KingsPiece[1]]==Q or self.Board[x][KingsPiece[1]]==R):
          #print("Q 4")
          Location.append([x,KingsPiece[1]])
          break
        else:
          break 

    # handles Bishop or Queen Checks 

    # handle Bishop up and to the left

    for x in range(1,KingsPiece[0]+1,1):
      try:
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]!="--" and (KingsPiece[1]-x)>=0 and (KingsPiece[0]-x>=0)):
          if(self.Board[KingsPiece[0]-x][KingsPiece[1]-x]==Q or self.Board[KingsPiece[0]-x][KingsPiece[1]-x]==B):
          
            Location.append([KingsPiece[0]-x,KingsPiece[1]-x])
            break
          else:
            break
      except:
        break
             

    # handles Bishop up and to the right



    for x in range(1,KingsPiece[0]+1,1):
      try:
        if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]!="--" and (KingsPiece[1]-x)>=0 and (KingsPiece[0]-x>=0)):
          if(self.Board[KingsPiece[0]-x][KingsPiece[1]+x]==Q or self.Board[KingsPiece[0]-x][KingsPiece[1]+x]==B):
            
            Location.append([KingsPiece[0]-x][KingsPiece[1]+x])

            break
          else:
            break
      except:
        break 
       
        #else:
         # return False 

    # handles Bishop down and to the Right

    for x in range(KingsPiece[0]+1,8,1):
      LC = 1
      try:
        if(self.Board[x][KingsPiece[1]+LC]!="--" ):
          if(self.Board[x][KingsPiece[1]+LC]==Q or self.Board[x][KingsPiece[1]+LC]==B):
            Location.append([x,KingsPiece[1]+LC])
            break
          else:
            break
        LC = LC + 1
      except:
        break

    # handles Bishot down and to the Left

    for x in range(KingsPiece[0]+1,8,1):
      RC = 1
      try:
        if(self.Board[x][KingsPiece[1]-RC]!="--" and KingsPiece[1]):
          if((self.Board[x][KingsPiece[1]-RC]==Q or self.Board[x][KingsPiece[1]-RC]==B) and KingsPiece[1]-RC >=0):
            
            Location.append([x,KingsPiece[1]-RC])
            break
          else:
            break
        RC = RC + 1
      except:
        break


    # Check for pawns
    
    if(BoardPrint%2==0):
      if(KingsPiece[0]+1<=7 and KingsPiece[1]+1<=7):
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]+1]==P):
          Location.append([KingsPiece[0]+1,KingsPiece[1]+1])
      
      if(KingsPiece[0]+1<=7 and KingsPiece[1]-1>=0):
        if(self.Board[KingsPiece[0]+1][KingsPiece[1]-1]==P):
          Location.append([KingsPiece[0]+1,KingsPiece[1]-1])
    
    if(BoardPrint%2==1):
      if(KingsPiece[0]-1>=0 and KingsPiece[1]+1<=7):
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]+1]==P):
          Location.append([KingsPiece[0]-1,KingsPiece[1]+1])
      
      if(KingsPiece[0]-1>=0 and KingsPiece[1]-1>=0):
        if(self.Board[KingsPiece[0]-1][KingsPiece[1]-1]==P):
          Location.append([KingsPiece[0]-1,KingsPiece[1]-1])

    # check for Opposing King
    # Left out I don't think its really needed
    
    return Location

  # does a basic test for stale mate 

  def StaleMateCalculate(self):
   
    if(BoardPrint%2==0):
      if(len(self.WhitePieces)==1):
        if(sum(self.whitePCsafe)==8):
          return True

    if(BoardPrint%2==1):
     
      if(len(self.BlackPieces)==1):
     
        if(sum(self.blackPCsafe)==8):
       
          return True
  
  def returnBestMove(self):
    # self.ChessBoard = board
    moves = []
    ## do AI Stuff here
    ## add helper functions
    ## create a move list
    ## that is then sent back to main
    ## AI.returnBestMove -> returns move for
    ## white. We can incorporate black later

    for startLet in range(0, 8):
      # print("in i")
      for startNum in range(0,8):
        # print("in j")
        # print(self.Board)
        if self.Board[startLet][startNum][0] == 'w':
          for endLet in range(0,8):
            # print("in u")
            for endNum in range(0,8):
              # print("in n")
              if self.Board[endLet][endNum] == '--':
                if self.isValidMove2(self.Board[startLet][startNum], startLet,endLet,startNum,endNum):
                  moves.append([1, startLet,startNum,endLet,endNum])
              elif self.Board[endLet][endNum] == 'bP':
                if self.isValidMove2(self.Board[startLet][startNum], startLet,endLet,startNum,endNum):
                  moves.append([2, startLet,startNum,endLet,endNum])
              elif self.Board[endLet][endNum] == 'bB':
                if self.isValidMove2(self.Board[startLet][startNum], startLet,endLet,startNum,endNum):
                  moves.append([3, startLet,startNum,endLet,endNum])
              elif self.Board[endLet][endNum] == 'bR':
                if self.isValidMove2(self.Board[startLet][startNum], startLet,endLet,startNum,endNum):
                  moves.append([4, startLet,startNum,endLet,endNum])
              elif self.Board[endLet][endNum] == 'bK':
                if self.isValidMove2(self.Board[startLet][startNum], startLet,endLet,startNum,endNum):
                  moves.append([5, startLet,startNum,endLet,endNum])
              elif self.Board[endLet][endNum] == 'bQ':
                if self.isValidMove2(self.Board[startLet][startNum], startLet,endLet,startNum,endNum):
                  moves.append([6, startLet,startNum,endLet,endNum])
              elif self.Board[endLet][endNum] == 'bKK':
                if self.isValidMove2(self.Board[startLet][startNum], startLet,endLet,startNum,endNum):
                  moves.append([7, startLet,startNum,endLet,endNum])


    random.shuffle(moves)
    bestMove = moves[0]

    for i in range(len(moves)):
      if bestMove[0] < moves[i][0]:
        bestMove = moves[i]
    # if bestMove[0] == 1:
    #   ran = random.randint(len(moves))
    #   bestMove = moves[ran]
    print(bestMove)

    return bestMove
 

  def isValidMove2(self,Piece,startLet,endLet,startNum,endNum):
  
    #print(Piece)
    if Piece[0] == 'w':
      KingsPosition = copy.deepcopy(self.WhiteKingsPosition)
      KK = "wKK"
      Q = "wQ"
      R = "wR"
      K = "wK"
      B = "wB"
      P = "wP"

    if Piece[0] == 'b':
      KingsPosition = copy.deepcopy(self.BlackKingsPosition)
      KK = "bKK"
      Q = "bQ"
      R = "bR"
      K = "bK"
      B = "bB"
      P = "bP"

 
      
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
        else:
          return False


    # White Pawn Logic -> and move 1 space up
    if(Piece == "wP" and endLet == (startLet+1) and startNum == endNum):
      if(self.Board[endLet][endNum]=="--"):
          return True
      else:
        return False

    #White Pawn Kill Logic 

    if(Piece == "wP" and (startLet == endLet-1) and (abs(startNum-endNum)==1)):
      slice = self.Board[endLet][endNum]
      if(slice[0]=="b"):
        return True

    #Black Pawn Kill Logic
    if(Piece == "bP" and (startLet == (endLet+1)) and (abs(startNum-endNum) == 1)):
      slice = self.Board[endLet][endNum]
     
      if(slice[0]=="w"):
        return True


    # Pawn Logic -> En passant
    #not tested
    # to do En pasant Logic 

    #if(Piece == "bp" and endLet == (startLet-1)):
      
     # if(startNum == (endNum + 1)):
      #  if(self.Board[startLet][endNum+1]=="wP"):
          # handle remove "wP" Right
       #   return True

     # if(startNum == (endNum -1)):
      #  if(self.Board[startLet][endNum-1] =="wP"):
          #handle removal of "wP" Left
       #   return True
      

    # start of rook logic

    if(Piece == R ):

      
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False
 
      if((startLet != endLet) and (startNum != endNum)):
        return False
   
      # handles up
      if(startLet>endLet):
        for x in range(startLet-1,endLet,-1):
          if(self.Board[x][endNum]!="--"):
            return False

        # handles down  
      if(startLet<endLet):
        for x in range(startLet+1,endLet,1):
          if(self.Board[x][endNum]!="--"):
            return False

        # handles left    
      if(startNum>endNum):
        for x in range(startNum-1,endNum,-1):
          if(self.Board[endLet][x]!="--"):
            return False

        # handles right    
      if(startNum<endNum):
        for x in range(startNum+1,endNum,1):
          if(self.Board[endLet][x]!="--"):
            return False

      return True

    # Logic for Knight

    if(Piece == K):

      print("kkk")

      if(self.samePiece(endLet,endNum,Piece)==True):
        return False
                
        # 2 up 1 left
      print("yyy")
      if((endLet)>=0 and (endLet)<= 7 and (endNum)>=0 and (endNum)<=7):


        
          
        if((startLet-endLet) == 2 and (startNum-endNum==1)):
          return True;

        # 2 Up and 1 Right
        if((startLet-endLet)==2 and (startNum-endNum==-1)):  
          print("ttt")
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

          # 2 right 1 down
        if((startLet-endLet)==-1 and (startNum-endNum)==-2 ):
          return True

        if((startLet-endLet)==1 and (startNum-endNum)==-2 ):
          return True      
    
      return False
      
   
    #Logic for black Bishop

    if(Piece == B ):     
      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # Checks to see if this is a diagonal move

      if(abs(startLet-endLet) != abs(startNum-endNum)):
      
        return False
    
        # up and to the left diagonally
      if((endLet < startLet) and (startNum > endNum)) :
        LC = 1
        for x in range(startLet-1,endLet,-1):
       
          if(self.Board[x][startNum-LC]!='--' or (startNum-LC <0)):
          #    print("your returning false stupidly dd")
            return False
          LC = LC + 1
        
        # up and to the right diagonally
      if((endLet < startLet) and (startNum < endNum)) :
        RC = 1
        for x in range(startLet-1,endLet,-1):
      
          if(self.Board[x][startNum+RC]!='--' ):
         #     print("your returning false stupidly dd4")
            return False
          
          RC = RC + 1


        # this down and to the left
      if((startLet < endLet) and (startNum > endNum)):
          
          # this used to be = endNum + 1
        LC = 1
        for x in range(startLet+1,endLet,1):
        #   

          if(self.Board[x][startNum-LC]!='--' ):
         #     print("your returning false stupidly dd")
            return False
          LC = LC + 1


        # down and to the right
      if((startLet < endLet) and startNum < endNum):
        RC = 1
        
        for x in range(startLet+1,endLet,1):
      
          if(self.Board[x][startNum+RC]!='--' ):
          #    print("your returning false stupidly dd7")
            return False
          RC = RC + 1

      return True
       

    if(Piece==Q):

      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      # Checks to see if this is a diagonal move

      if(abs(startLet-endLet) == abs(startNum-endNum)):


          # up and to the left diagonally
        if((endLet < startLet) and (startNum > endNum)) :
          
          LC = 1
          for x in range(startLet-1,endLet,-1):
       
            if(self.Board[x][startNum-LC]!='--' ):
          #    print("your returning false stupidly dd")
              return False
            
            LC = LC  + 1
        
        # up and to the right diagonally
        if((endLet < startLet) and (startNum < endNum)) :
          
          RC = 1
          for x in range(startLet-1,endLet,-1):
      
            if(self.Board[x][startNum+RC]!='--' ):
         #     print("your returning false stupidly dd4")
              return False
            RC = RC + 1


        # this down and to the left
        if((startLet < endLet) and (startNum > endNum)):
          
          LC = 1 
          for x in range(startLet+1,endLet,1):
        
            if(self.Board[x][startNum-LC]!='--' ):
         #     print("your returning false stupidly dd")
              return False
            LC = LC + 1


          # down and to the right
        if((startLet < endLet) and startNum < endNum):
          
          RC = 1
          for x in range(startLet+1,endLet,1):
      
            if(self.Board[x][startNum+RC]!='--' ):
          #    print("your returning false stupidly dd7")
              return False
            RC = RC + 1

      
        # returns true if valid move
        return True
        
      # start of Rook logic but for queen peice 

      if((startLet == endLet) or (startNum == endNum)):
          
        # Handles Up
        # handles up
        if(startLet>endLet):
          for x in range(startLet-1,endLet,-1):
            if(self.Board[x][endNum]!="--"):
              return False

        # handles down  
        if(startLet<endLet):
          for x in range(startLet+1,endLet,1):
            if(self.Board[x][endNum]!="--"):
              return False

        # handles left    
        if(startNum>endNum):
          for x in range(startNum-1,endNum,-1):
            if(self.Board[endLet][x]!="--"):
              return False

        # handles right    
        if(startNum<endNum):
          for x in range(startNum+1,endNum,1):
            if(self.Board[endLet][x]!="--"):
              return False

        return True
        
        # End of Queen Logic
      return False
           

    # start of king logic 
 
    if(Piece == KK):

      if(self.samePiece(endLet,endNum,Piece)==True):
        return False

      if((abs(startLet-endLet)==1 or abs(startLet-endLet)==0 )  and (abs(startNum-endNum)==1 or abs(startNum-endNum)==0)):
        print("inside abs")
        print(str(startLet) + str(startNum) + str(endLet) + str(endNum))
        return True
        
      else:  
        
        return False
   
    

    # redundent False incase something ever sliped through
    # which it shouldn't
    return False



def main():
	 


    

    global MoveCounter 
    global BoardPrint 
    BoardPrint = 0
    MoveCounter = 0
    CheckMate = False 
    Chess = Board()

    CHESSGUI = GUI()
    CHESSGUI.update_screen(Chess)


    # Call to Chess AIBrain creation.
    #CHESSAI = AIBrain(Chess.Board,BoardPrint);

    Chess.printBoard()

    while(CheckMate!=True):

   
      if(BoardPrint%2==0):
        CheckMate = Chess.CheckMate(Chess.WhiteKingsPosition)
        Chess.Board[Chess.WhiteKingsPosition[0]][Chess.WhiteKingsPosition[1]] = "wKK"
      elif(BoardPrint%2==1):
        CheckMate = Chess.CheckMate(Chess.BlackKingsPosition)
        Chess.Board[Chess.BlackKingsPosition[0]][Chess.BlackKingsPosition[1]] = "bKK"
        
      if(CheckMate == True):
        # if(BoardPrint%2==0):
        #   print("Check Mate, white you lose")
        # elif(BoardPrint%2==1):
        #   print("Check mate black you lose")

        # TO DISPLAY CHECKMATE MESSAGE UNCOMMENT THIS, COMMENT EXISTING break
        # AND COMMENT OUT THE IF/ELIF above
        # Will display the message at bottom then allow user to close window and exit program

        if (BoardPrint % 2 == 0):
          print("Check Mate, white you lose")
          CHESSGUI.text_message("Checkmate! Black Wins", 100, 445)
          exit = None
          while exit != "exit":
            exit = CHESSGUI.moveClick()
          break
        elif (BoardPrint % 2 == 1):
          print("Check mate black you lose")
          CHESSGUI.text_message("Checkmate! White Wins", 100, 445)
          exit = None
          while exit != "exit":
            exit = CHESSGUI.moveClick()
          break

        # do you want to play again?
        # add repetative functional play so 
        # RL can play over and over again
        # break
     
      try:

        if(BoardPrint%2==1):

           #GUI team this is where your gui.moveclick
           # function outputs its clicked ValueError

          move = CHESSGUI.moveClick()
          if move == "exit":
              break
          userStartNum = move[0]
          userStartLet = move[1]
          print(str(userStartLet) + " " + str(userStartNum))

          userEndNum = move[2]
          userEndLet = move[3]




          # userStartLet = int(input("enter start Let (vertical column): "))
          # userStartNum  = int(input("enter start num (horizontal column): "))
          # userEndLet  = int(input("enter end Let (vertical column: "))
          # userEndNum  = int(input("enter end Num (horizontal column): "))

        elif(BoardPrint%2==0):
           # Start of White random AI 
          #print("Whites turn to move")
          #print("White is thinking pretty hard")
          #t.sleep(1)

          # HELPFUL CAPS LOCK: THIS IS WHERE AI GETS CALLED

          # CHESSAI.UpDateBoardData(Chess.Board)
          # Chess.printBoard()

          WhiteAttemptedAIMove = Chess.returnBestMove()

          userStartLet = WhiteAttemptedAIMove[1]
          userEndLet = WhiteAttemptedAIMove[3]
          userStartNum = WhiteAttemptedAIMove[2]
          userEndNum = WhiteAttemptedAIMove[4]
          print(WhiteAttemptedAIMove)
          # userStartLet = random.randint(0, 7)
          # userStartNum = random.randint(0, 7)
          # userEndLet = random.randint(0, 7)
          # userEndNum = random.randint(0, 7)
          # print(str(userStartLet) + " " +str(userStartNum) + " "+str(userEndLet) + " " + str(userEndNum))
        
        
        
        SelectedPiece = Chess.Board[userStartLet][userStartNum]
        if(BoardPrint%2==0 and (SelectedPiece[0]=="b" or SelectedPiece[0]=="-") ):
          # move counter decrament is probably causing a problem here
          #MoveCounter = MoveCounter - 1
          raise Exception("cant move that piece")
        if(BoardPrint%2==1 and (SelectedPiece[0]=="w" or SelectedPiece[0]=="-")):
          # move counter decrament is probabably 
          # causing a problem here
          #MoveCounter = MoveCounter -1
          raise Exception("can't move that peice")

        print(MoveCounter)
        if(Chess.move(userStartLet,userStartNum,userEndLet,userEndNum)==True):
          print("\n")
          BoardPrint = BoardPrint + 1
          print(BoardPrint)
          print(str(userStartLet) + " " +str(userStartNum) + " "+str(userEndLet) + " " + str(userEndNum))
          print(Chess.WhiteKingsPosition)
          print(Chess.BlackKingsPosition)
          Chess.printBoard()

          CHESSGUI.update_screen(Chess)

          #t.sleep(2)
          if(BoardPrint%2==1):
            print("Blacks turn to make a  move")
        else:
          raise Exception("Not legal move try again")
        #userwait = input("press enter for next move")

      except:
        
        MoveCounter = MoveCounter - 1

      MoveCounter = MoveCounter + 1

main()
