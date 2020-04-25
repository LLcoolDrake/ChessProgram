import sys
import pygame

from chessPieces import ChessPieces
from settings import Settings
from CHESSGUISandBox import Board

class GUI:


  GameName = "chess"

  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode((self.settings.width, self.settings.height))
    pygame.display.set_caption("CS 205 Chess")

    self.chess_pieces = ChessPieces(self)
    self.board = Board()
    my_image = pygame.image.load("ChessBoard.png").convert()
    self.screen.blit(my_image,(0,0))


  def play_game(self):
    while True:
      self._check_events()
      self._update_screen()

  # quit with press of q
  def _check_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_q:
          sys.exit()

  def _update_screen(self):
    for row in self.board.Board:
      for piece in row:
        i = 0
        while i < 12:
          if piece == self.chess_pieces.pieces[i].name:
            self.chess_pieces.pieces[i].x = i * 50
            self.chess_pieces.pieces[i].draw_piece()
          i += 1



    # for index, piece in enumerate(self.chess_pieces.pieces[:6]):
    #     piece.x = index * 50
    #     piece.draw_piece()
    #
    # for index, piece in enumerate(self.chess_pieces.pieces[6:]):
    #     piece.x = index * 50
    #     piece.y = 100
    #     piece.draw_piece()
    pygame.display.flip()

if __name__ == '__main__':
  chess_gui = GUI()
  chess_gui.play_game()