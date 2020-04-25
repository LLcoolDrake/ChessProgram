from spritesheet import spritesheet

class ChessPieces:
    def __init__(self, chess_gui):
        self.chess_gui = chess_gui
        self.pieces = []
        self._load_pieces()

    def _load_pieces(self):
        filename = 'chessSprites.gif'
        piece_sprites = spritesheet(filename)

        piece_images = piece_sprites.load_all_images(2, 6)

        piece_names = ["wP", "wR", "wK", "wB", "wQ", "wKK", "bP", "bR", "bK", "bB", "bQ", "bKK"]
        piece_num = 0

        for name in piece_names:
            piece = chessPiece(self.chess_gui)
            piece.name = name
            piece.image = piece_images[piece_num]
            self.pieces.append(piece)
            piece_num += 1


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