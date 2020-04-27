import pygame
import pygame.freetype


class GUI:


  GameName = "chess"
  screen = None

  def __init__(self):
    pygame.init()
    self.font = pygame.freetype.SysFont(None, 18)
    self.screen = pygame.display.set_mode((400, 465))
    self.screen.fill([255, 255, 255])
    pygame.display.set_caption("CS 205 Chess")

    self.my_image = pygame.image.load("ChessBoard.png").convert()
    self.screen.blit(self.my_image,(0,0))
    self.text_message("You play as black", 125, 405)
    self.text_message("Click on a piece then click where to move it to", 5, 425)


  def moveClick(self):
      move_cords = []
      while len(move_cords) < 4:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            pygame.quit()
            move_cords = "exit"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            cords = pygame.mouse.get_pos()
            move_cords.append(cords[0] // 50)
            move_cords.append(cords[1] // 50)
            print(move_cords)
      return move_cords

  def update_screen(self, board):
    self.screen.blit(self.my_image, (0, 0))

    for row in range(8):
        for col in range(8):
            if board.Board[row][col] == "wP":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("whitePawn.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "wR":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("whiteRook.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "wK":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("whiteKnight.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "wB":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("whiteBishop.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "wQ":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("whiteQueen.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "wKK":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("whiteKing.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "bP":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("blackPawn.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "bR":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("blackRook.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "bK":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("blackKnight.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "bB":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("blackBishop.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "bQ":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("blackQueen.png")
                self.screen.blit(img, (x, y))
            elif board.Board[row][col] == "bKK":
                (x, y) = self.chess_to_screen((row, col))
                img = pygame.image.load("blackKing.png")
                self.screen.blit(img, (x, y))

        pygame.display.update()
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

  def text_message(self, message, x, y):
      text_display, rect = self.font.render(message, (0, 0, 0))
      self.screen.blit(text_display, (x, y))
      pygame.display.flip()
