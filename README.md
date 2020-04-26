# CS 205 Final Project Group 7: Jacob Drake, Nick Laware, Ethan Bokelberg, Jake Regele  
For sprint 1, we have the logic for playing chess functioning by running the ChessRandomAIWorking.py, displaying a board printed to the terminal, playing
against the computer by having the computer select random valid moves on its turn.
tkinter_test.py is the beginnings of our more sophisticated GUI, not finished implementation yet.  
# GUI Implemention comments  
Using PyGame, the board is an image, loaded in during the init. The sprites for the pieces are also all saved as individual png files. 
To display them, the update_screen function loops through the board from the Board class, and compares the value in each cell. If it matches a piece, 
then that piece is blitted to the screen in that position, using the chess_to_screen function to convert the chess row/col to pixels on the screen. 
The moveClick function handles user interaction, sending a value of "exit" if the user quits pygame, or records 2 mouse clicks for the piece and its destination,
 and sends the coordinates. In CHESSGUISandbox.py, moveClick is called and will break out of the game loop if it returns "exit", and assigns the coordinates to 
 the appropriate variables otherwise. text_message displays text at the bottom of the window below the board, and is called in init to display messages for the player.
