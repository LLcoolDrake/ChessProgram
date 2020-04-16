# Not done yet, this will be the tkinter gui implementation


import tkinter as gui


class BoardGUI(gui.Frame):

    def __init__(self, parent, rows=8, columns=8, size=32, color1="white", color2="black"):
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}

        canvas_width = columns * size
        canvas_height = rows * size

        gui.Frame.__init__(self, parent)
        self.canvas = gui.Canvas(self, borderwidth=0, highlightthickness=0, width=canvas_width, height=canvas_height,
                                 background="white")
        self.canvas.pack(side="top", fill="both", expand=True, padx=1, pady=1)

        self.canvas.bind("<Configure>", self.refresh)

    def refresh(self, event):
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2

    # def click(self, event):
        # event.x & y return coordinates, narrow down to row/column combo
        # this will likely need to be changed... what is tkiniter
        # current_col = event.x/8
        # current_row = event.y/8

        # selected = [current_col, current_row]

        # send selected to move function from Board in Chess.py
        # TODO: implement move function
        # visual feedback of selection?

    # use board functions
    # def move(self):


if __name__ == "__main__":
    root = gui.Tk()
    board = BoardGUI(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()
