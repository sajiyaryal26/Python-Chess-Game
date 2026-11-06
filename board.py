import pygame
from pieces import white_queen_obj,white_king_obj,white_rook_left_obj,white_rook_right_obj,white_knight_left_obj,white_knight_right_obj,white_bishop_left_obj,white_bishop_right_obj,white_pawns,black_king_obj,black_queen_obj,black_rook_left_obj,black_rook_right_obj,black_knight_left_obj,black_knight_right_obj,black_bishop_left_obj,black_bishop_right_obj,black_pawns
def draw_rect(screen):
    SQ=640//8
    for r in range(8):
        for c in range(8):
            x = SQ * c
            y = SQ * r
            if ((r+c) % 2 == 0):
                color=(222,235,247)
            else:
                color=(75,105,150)
            pygame.draw.rect(screen,color,(x,y,SQ,SQ))

def create_board():
    board=[]
    for i in range(8):
        row=[]
        for j in range(8):
            row.append(None)
        board.append(row)
    board[7][3] = white_queen_obj
    board[7][4] = white_king_obj
    board[7][0] = white_rook_left_obj
    board[7][7] = white_rook_right_obj
    board[7][1] = white_knight_left_obj
    board[7][6] = white_knight_right_obj
    board[7][2] = white_bishop_left_obj
    board[7][5] = white_bishop_right_obj
    board[0][3] = black_queen_obj
    board[0][4] = black_king_obj
    board[0][0] = black_rook_left_obj
    board[0][7] = black_rook_right_obj
    board[0][1] = black_knight_left_obj
    board[0][6] = black_knight_right_obj
    board[0][2] = black_bishop_left_obj
    board[0][5] = black_bishop_right_obj
    for c in range(8):
        board[6][c] = white_pawns[c]
        board[1][c] = black_pawns[c]
    return board
