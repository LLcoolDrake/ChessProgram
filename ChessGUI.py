import pygame

class GUI:


  GameName = "chess"

  def __init__(self):
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    my_image = pygame.image.load("ChessBoard.png")  
    screen.blit(my_image,(0,0))
    pygame.display.flip()
