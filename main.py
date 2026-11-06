from pieces import white_pieces
from pieces import black_pieces
from piece import Piece,Pawn,Rook,King,Bishop,Knight,Queen,get_legal_moves,is_checkmate,is_stalemate
from board import draw_rect, create_board
from pieces import white_queen_obj,white_king_obj,white_rook_left_obj,white_rook_right_obj,white_knight_left_obj,white_knight_right_obj,white_bishop_left_obj,white_bishop_right_obj,white_pawns,black_king_obj,black_queen_obj,black_rook_left_obj,black_rook_right_obj,black_knight_left_obj,black_knight_right_obj,black_bishop_left_obj,black_bishop_right_obj,black_pawns
import pygame
import piece as piece_module
from sys import exit
pygame.init()
screen = pygame.display.set_mode((640,640))
board=create_board()
piece_module.last_move = None
selected_piece = None
valid_moves = []
turn = "White"
game_over = False
game_message = ""
promotion_pending = None
promotion_classes = {
    "Queen" : Queen,
    "Rook" : Rook,
    "Bishop" : Bishop,
    "Knight" : Knight
}
promotion_images = {
    "White" : {
        "Queen" : white_queen_obj.image,
        "Rook" : white_rook_left_obj.image,
        "Bishop" : white_bishop_left_obj.image,
        "Knight" : white_knight_left_obj.image
    },
    "Black" : {
        "Queen" : black_queen_obj.image,
        "Rook" : black_rook_left_obj.image,
        "Bishop" : black_bishop_left_obj.image,
        "Knight" : black_knight_left_obj.image
    }
}
def get_promotion_piece(piece_type,color,position):
    image = promotion_images[color][piece_type]
    promoted_piece = promotion_classes[piece_type](image,color,position,piece_type)
    promoted_piece.has_moved = True
    return promoted_piece


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # RESTART GAME
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r and promotion_pending is None:
            board = create_board()
            piece_module.last_move = None
            selected_piece = None
            valid_moves = []
            turn = "White"
            game_over = False
            game_message = ""
            promotion_pending = None

        # PAWN PROMOTION CHOICE
        if event.type == pygame.KEYDOWN and promotion_pending is not None:
            choices = {
                pygame.K_q: "Queen",
                pygame.K_r: "Rook",
                pygame.K_b: "Bishop",
                pygame.K_n: "Knight"
            }

            if event.key in choices:
                chosen_piece = choices[event.key]
                row, column = promotion_pending.position
                color = promotion_pending.color

                promoted_piece = get_promotion_piece(
                    chosen_piece, color, (row, column)
                )

                board[row][column] = promoted_piece
                promotion_pending = None

                if turn == "White":
                    turn = "Black"
                else:
                    turn = "White"

                if is_checkmate(board, turn):
                    game_over = True
                    winner = "White" if turn == "Black" else "Black"
                    game_message = winner + " wins! Checkmate!"

                elif is_stalemate(board, turn):
                    game_over = True
                    game_message = "Draw! Stalemate!"


        if (event.type == pygame.MOUSEBUTTONDOWN and not game_over and promotion_pending is None):
            x,y = pygame.mouse.get_pos()
            row = y // 80
            column = x // 80
            clicked_piece = board[row][column]

            
            if selected_piece is None:
                if clicked_piece is not None and clicked_piece.color == turn:
                    selected_piece = clicked_piece
                    valid_moves = get_legal_moves(board, selected_piece)

            else:
                destination = (row, column)

                if destination in valid_moves:
                    old_row,old_col = selected_piece.position
                    new_row,new_col = destination
                    en_passant = selected_piece.piece_type == "Pawn" and new_col != old_col and board[new_row][new_col] is None

                    selected_piece.move_to(destination, board)

                    if en_passant:
                        board[old_row][new_col] = None

                    piece_module.last_move = (selected_piece , (old_row,old_col), destination)

                    if(selected_piece.piece_type == "King"):
                        new_row,new_col = destination
                    
                        if(abs(new_col - old_col)) == 2:
                            if(new_col > old_col):
                                rook = board[new_row][7]
                                if rook is not None:
                                    board[new_row][5] = rook
                                    board[new_row][7] = None
                                    rook.position = (new_row,5)
                                    rook.has_moved = True
                            else:
                                rook = board[new_row][0]
                                if rook is not None:
                                    board[new_row][3] = rook
                                    board[new_row][0] = None
                                    rook.position = (new_row,3)
                                    rook.has_moved = True
                    promotion_row = 0 if selected_piece.color == "White" else 7
                    if(selected_piece.piece_type == "Pawn" and new_row == promotion_row):
                        promotion_pending = selected_piece
                    else:
                        if turn == "White":
                            turn = "Black"
                        else:
                            turn = "White"

                        if is_checkmate(board, turn):
                            game_over = True
                            winner = "White" if turn == "Black" else "Black"
                            game_message = winner + " wins! Checkmate!"

                        elif is_stalemate(board, turn):
                            game_over = True
                            game_message = "Draw! Stalemate!"

                    selected_piece = None
                    valid_moves = []

                elif clicked_piece is not None and clicked_piece.color == turn:
                    selected_piece = clicked_piece
                    valid_moves = get_legal_moves(board, selected_piece)

                else:
                    selected_piece = None
                    valid_moves = []


    draw_rect(screen)
    for row,col in valid_moves:
        x = col * 80
        y = row * 80
        pygame.draw.circle(screen, (0,255,0) , (x+40, y+40), 12)
    for i in range(8):
        for j in range(8):
            piece=board[i][j]
            if piece is not None:
                x=j*80
                y=i*80
                screen.blit(piece.image,(x,y))
    if game_over:
        font = pygame.font.SysFont(None,48)
        text = font.render(game_message,True,(255,0,0))
        text_rect = text.get_rect(center=(320,320))
        screen.blit(text,text_rect)
    
    if promotion_pending is not None:
        font = pygame.font.SysFont(None,40)
        text = font.render("Promote: Q - Queen , N - Knight , B - Bishop, R - Rook",True,(255,255,255))
        screen.blit(text,(20,300))
    pygame.display.update()

