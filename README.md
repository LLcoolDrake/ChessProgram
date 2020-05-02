NOTE To  TA: 
  The Master branch is our finished project. It includes the AI and GUI. It might be dificult for you to test the game
 and set up test scenarios if the AI is turned on. There is a second branch, Easy-logic-test. It is the same file, except the AI is switched off and the user has control of white and blacks moves. If you would like to set up your own test board, augment the variable, Board = [<chess board positioning>] to your liking and test away. Note if you move the black or white
 king to a different starting position, update the variable, WhiteKingsPosition =[], or BlackKingsPosition = []. The game updates the kings position and if it's set up to the wrong location, it wont behave like you want it to. These two variables are right below the board variable. The first value in KingsPosition, is the row value, (0 = top row, 7 = bottom row). The second variable is the column. (0 = left column, 7 = right column)   


# CS 205 Final Project Group 7: Jacob Drake, Nick Laware, Ethan Bokelberg, Jake Regele  
For sprint 2, the main() to run is in CHESSGUISandBox.py. It calls the ChessGUI to create a GUI object, and uses that to run the games. Comments about the 
GUI class are below. 
# GUI Implemention comments  
Using PyGame, the board is an image, loaded in during the init. The sprites for the pieces are also all saved as individual png files. 
To display them, the update_screen function loops through the board from the Board class, and compares the value in each cell. If it matches a piece, 
then that piece is blitted to the screen in that position, using the chess_to_screen function to convert the chess row/col to pixels on the screen. 
The moveClick function handles user interaction, sending a value of "exit" if the user quits pygame, or records 2 mouse clicks for the piece and its destination,
 and sends the coordinates. In CHESSGUISandbox.py, moveClick is called and will break out of the game loop if it returns "exit", and assigns the coordinates to 
 the appropriate variables otherwise. text_message displays text at the bottom of the window below the board, and is called in init to display messages for the player.
 Also, inside the if CheckMate == True in CHESSGUISandbox, a message will be printed to the window displaying who won, and the window will stay open until the player closes
 it, which will end the program.
