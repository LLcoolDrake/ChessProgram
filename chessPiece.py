class chessPiece:
    def __init__(self, chess_gui):
        self.image = None
        self.name = ''

        self.screen = chess_gui.screen

        self.x, self.y = 0.0, 0.0

    def draw_piece(self):
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)