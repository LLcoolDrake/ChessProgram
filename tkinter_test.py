# Not done yet, this will be the tkinter gui implementation

import Chess
import tkinter as gui


class Board_GUI(gui.Frame):
    # variables
    pieces= {}
    selected = None
    selected_piece = None
    rows = 8
    cols = 8

    def __init__(self, board):
        self.board = board

        # I'm not sure about displaying the board because I don't know tkinter
        # TODO: Jake, can you get the display and etc working?

    def click(self, event):
        # event.x & y return coordinates, narrow down to row/column combo
        # this will likely need to be changed... what is tkiniter
        current_col = event.x/8
        current_row = event.y/8

        selected = [current_col, current_row]

        # send selected to move function from Board in Chess.py
        # TODO: implement move function
        # visual feedback of selection?


    # use board functions
    # def move(self):