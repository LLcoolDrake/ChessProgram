import sys

import pygame

from chessPieces import ChessPieces
from settings import Settings

class GUI:


  GameName = "chess"

  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("CS 205 Chess")
    self.chess_pieces = ChessPieces(self)

    # my_image = pygame.image.load("ChessBoard.png")
    # screen.blit(my_image,(0,0))

    # pygame.display.flip()

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
    self.screen.fill(self.settings.bg)
    self.chess_pieces.pieces[0].draw_piece()
    pygame.display.flip()

if __name__ == '__main__':
  chess_gui = GUI()
  chess_gui.play_game()