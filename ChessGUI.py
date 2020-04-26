import sys
import pygame

from chessPieces import ChessPieces

class GUI:


  GameName = "chess"

  def __init__(self, board):
    pygame.init()
    self.screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("CS 205 Chess")

    self.chess_pieces = ChessPieces(self)
    self.board = board
    my_image = pygame.image.load("ChessBoard.png").convert()
    self.screen.blit(my_image,(0,0))


  def play_game(self):
      self.check_events()
      self.update_screen()

  # quit with press of q
  def check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          cords = pygame.mouse.get_pos()
          # cell contains coordinates of last click
          cell = (cords[0] // 50, cords[1] // 50)
          print(cell)
          return cell
      elif event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          sys.exit()


  def update_screen(self):
    for row in range(8):
        for col in range(8):
            if self.board.Board[row][col] == "wP":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[0].x = x
                self.chess_pieces.pieces[0].y = y
                self.chess_pieces.pieces[0].draw_piece()
            elif self.board.Board[row][col] == "wR":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[1].x = x
                self.chess_pieces.pieces[1].y = y
                self.chess_pieces.pieces[1].draw_piece()
            elif self.board.Board[row][col] == "wK":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[2].x = x
                self.chess_pieces.pieces[2].y = y
                self.chess_pieces.pieces[2].draw_piece()
            elif self.board.Board[row][col] == "wB":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[3].x = x
                self.chess_pieces.pieces[3].y = y
                self.chess_pieces.pieces[3].draw_piece()
            elif self.board.Board[row][col] == "wQ":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[4].x = x
                self.chess_pieces.pieces[4].y = y
                self.chess_pieces.pieces[4].draw_piece()
            elif self.board.Board[row][col] == "wKK":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[5].x = x
                self.chess_pieces.pieces[5].y = y
                self.chess_pieces.pieces[5].draw_piece()
            elif self.board.Board[row][col] == "bP":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[6].x = x
                self.chess_pieces.pieces[6].y = y
                self.chess_pieces.pieces[6].draw_piece()
            elif self.board.Board[row][col] == "bR":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[7].x = x
                self.chess_pieces.pieces[7].y = y
                self.chess_pieces.pieces[7].draw_piece()
            elif self.board.Board[row][col] == "bK":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[8].x = x
                self.chess_pieces.pieces[8].y = y
                self.chess_pieces.pieces[8].draw_piece()
            elif self.board.Board[row][col] == "bB":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[9].x = x
                self.chess_pieces.pieces[9].y = y
                self.chess_pieces.pieces[9].draw_piece()
            elif self.board.Board[row][col] == "bQ":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[10].x = x
                self.chess_pieces.pieces[10].y = y
                self.chess_pieces.pieces[10].draw_piece()
            elif self.board.Board[row][col] == "bKK":
                (x, y) = self.chess_to_screen((row, col))
                self.chess_pieces.pieces[11].x = x
                self.chess_pieces.pieces[11].y = y
                self.chess_pieces.pieces[11].draw_piece()

    pygame.display.flip()
  def chess_to_screen(self, chess_coord):
      (row, col) = chess_coord
      x = 12 + col * 50
      y = row * 50
      return (x, y)
  def screen_to_chess(self, screen_coord):
      (x, y) = screen_coord
      row = y/50
      col = x/50
      return (row, col)
