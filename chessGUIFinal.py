import pygame

file = "chessSprites.gif"

COLORS = ((119, 103, 103), (255, 255, 255))

CELL_HEIGHT = 50
CELL_WIDTH = 50

SPRITE_WIDTH = 28
SPRITE_HEIGHT = 44


# returns a Surface object containing a sprite
def get_sprite(location, sprite_sheet):
    location = pygame.Rect(location)
    sprite = pygame.Surface((SPRITE_WIDTH, SPRITE_HEIGHT)).convert()
    sprite.blit(sprite_sheet, (0, 0), location)
    sprite.set_colorkey((0, 0, 0, 255), pygame.RLEACCEL)

    return sprite


# returns pixel location of a chess piece
def get_location(piece):
    # list used for pixel calculations
    sprite_list = ['P', 'R', 'K', 'B', 'Q', 'KK']

    if piece[0] == 'w':
        y = 0
    else:
        y = SPRITE_HEIGHT

    x = sprite_list.index(piece[1::]) * SPRITE_WIDTH

    return [x, y, x + SPRITE_WIDTH, y + SPRITE_HEIGHT]


# test board
board = [["wP", "wK", "wR", "wB", "wQ", "wKK", "", ""],
         ["wP", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["", "", "", "", "", "", "", ""],
         ["bP", "bK", "bR", "bB", "bQ", "bKK", "", ""]]

pygame.init()

screen = pygame.display.set_mode([CELL_HEIGHT * 8, CELL_WIDTH * 8])

refresh = pygame.time.Clock()

sprite_file = pygame.image.load(file).convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            cords = pygame.mouse.get_pos()
            # cell contains coordinates of last click
            cell = (cords[0] // CELL_WIDTH, cords[1] // CELL_HEIGHT)
            print(cell)
            # send to chess engine

    for row in range(8):
        for col in range(8):
            # draw the chess board
            pygame.draw.rect(screen, COLORS[(row + col) % 2],
                             [CELL_WIDTH * col, CELL_HEIGHT * row, CELL_WIDTH, CELL_HEIGHT])
            # get board from chess engine
            # draw pieces over the chess board
            if board[row][col]:
                drawable = get_sprite(get_location(board[row][col]), sprite_file)
                screen.blit(drawable, [CELL_WIDTH * col + (CELL_WIDTH - SPRITE_WIDTH) // 2,
                                       CELL_HEIGHT * row + (CELL_HEIGHT - SPRITE_HEIGHT) // 2])

    refresh.tick(60)
    pygame.display.flip()
