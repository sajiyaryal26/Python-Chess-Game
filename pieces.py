import pygame
from piece import Piece,Pawn,Rook,King,Knight,Queen,Bishop
# Load white piece images
white_king = pygame.transform.scale(
    pygame.image.load("pieces/white_king.png"), (60, 60)
)
white_queen = pygame.transform.scale(
    pygame.image.load("pieces/white_queen.png"), (60, 60)
)
white_rook = pygame.transform.scale(
    pygame.image.load("pieces/white_rook.png"), (60, 60)
)
white_bishop = pygame.transform.scale(
    pygame.image.load("pieces/white_bishop.png"), (60, 60)
)
white_knight = pygame.transform.scale(
    pygame.image.load("pieces/white_knight.png"), (60, 60)
)
white_pawn = pygame.transform.scale(
    pygame.image.load("pieces/white_pawn.png"), (60, 60)
)

# Starting positions: White's back row is rank 1
white_pieces = [
    (white_rook, (0, 560)),
    (white_knight, (80, 560)),
    (white_bishop, (160, 560)),
    (white_queen, (240, 560)),
    (white_king, (320, 560)),
    (white_bishop, (400, 560)),
    (white_knight, (480, 560)),
    (white_rook, (560, 560)),
]

# Eight pawns in rank 2
for x in range(0, 640, 80):
    white_pieces.append((white_pawn, (x, 480)))


#LOAD BLACK PIECES
black_bishop=pygame.transform.scale(
    pygame.image.load("pieces/black_bishop.png"),(60,60)
    )
black_king=pygame.transform.scale(
    pygame.image.load("pieces/black_king.png"),(60,60)
)
black_knight=pygame.transform.scale(
    pygame.image.load("pieces/black_knight.png"),(60,60)
)
black_pawn=pygame.transform.scale(
    pygame.image.load("pieces/black_pawn.png"),(60,60)
)
black_queen=pygame.transform.scale(
    pygame.image.load("pieces/black_queen.png"),(60,60)
)
black_rook=pygame.transform.scale(
    pygame.image.load("pieces/black_rook.png"),(60,60)
)
black_pieces=[
    (black_rook,(0,0)),
    (black_knight,(80,0)),
    (black_bishop,(160,0)),
    (black_queen,(240,0)),
    (black_king,(320,0)),
    (black_bishop,(400,0)),
    (black_knight,(480,0)),
    (black_rook,(560,0)),
]
for saj in range(0,640,80):
    black_pieces.append((black_pawn,(saj,80)))

white_king_obj = King(white_king, "White", (7, 4), "King")
white_queen_obj = Queen(white_queen, "White", (7,3), "Queen")
white_rook_left_obj = Rook(white_rook, "White", (7,0),"Rook")
white_rook_right_obj = Rook(white_rook, "White", (7,7), "Rook")
white_knight_left_obj = Knight(white_knight, "White", (7,1), "Knight")
white_knight_right_obj = Knight(white_knight, "White" , (7,6), "Knight")
white_bishop_left_obj = Bishop(white_bishop, "White" , (7,2), "Bishop")
white_bishop_right_obj = Bishop(white_bishop, "White" , (7,5) , "Bishop")
white_pawns = []
for col in range(8):
    white_pawn_obj = Pawn(white_pawn, "White" , (6,col), "Pawn")
    white_pawns.append(white_pawn_obj)

black_king_obj = King(black_king, "Black", (0, 4), "King")
black_queen_obj = Queen(black_queen, "Black", (0,3), "Queen")
black_rook_left_obj = Rook(black_rook, "Black", (0,0),"Rook")
black_rook_right_obj = Rook(black_rook, "Black", (0,7), "Rook")
black_knight_left_obj = Knight(black_knight, "Black", (0,1), "Knight")
black_knight_right_obj = Knight(black_knight, "Black" , (0,6), "Knight")
black_bishop_left_obj = Bishop(black_bishop, "Black" , (0,2), "Bishop")
black_bishop_right_obj = Bishop(black_bishop, "Black" , (0,5) , "Bishop")
black_pawns = []
for col in range(8):
    black_pawn_obj = Pawn(black_pawn, "Black" , (1,col), "Pawn")
    black_pawns.append(black_pawn_obj)


print(len(white_pawns))
print(len(black_pawns))
print(white_king_obj.position)
print(black_king_obj.position)