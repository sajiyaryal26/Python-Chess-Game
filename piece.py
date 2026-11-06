last_move = None
class Piece:
    def __init__(self,image,color,position,piece_type):
        self.image = image
        self.color = color
        self.position = position
        self.piece_type = piece_type
        self.has_moved = False
    
    def move_to(self,new_positions,board):
        if new_positions not in self.get_valid_moves(board):
            return False
        else:
            old_row,old_col = self.position
            new_row,new_col = new_positions

            board[old_row][old_col] = None
            board[new_row][new_col] = self

            self.position = new_positions
            self.has_moved = True
        return True

class Pawn(Piece):
    def get_valid_moves(self,board):
        row,column = self.position
        valid_move = []
        if self.color=="White" :
            direction=-1
            start_row=6
        else:
            direction=1
            start_row=1
        
        next_row = row + direction
        if(0 <= next_row < 8 and board[next_row][column] is None):
            valid_move.append((next_row,column))
        
        two_row = row + 2 * direction

        if(self.has_moved is False and row == start_row and board[two_row][column] is None and board[next_row][column] is None):
            valid_move.append((two_row,column))
        
        for next_col in (column-1,column+1):
            if(0<=next_row<8 and 0<=next_col<8):
                target=board[next_row][next_col]
                if target is not None and target.color!=self.color:
                    valid_move.append((next_row,next_col))
        global last_move
        if last_move is not None:
            last_piece,old_position,new_position = last_move
            if(last_piece.piece_type == "Pawn" and last_piece.color!=self.color and abs(new_position[0]-old_position[0])==2 and new_position[0] == row and abs(new_position[1]-column)==1):
                target_row = direction + row
                target_column = new_position[1]
                if(board[target_row][target_column] is None):
                    valid_move.append((target_row,target_column))
        return valid_move

class Rook(Piece):
    def get_valid_moves(self,board):
        r,c=self.position
        valid_moves=[]
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for dr,dc in directions:
            new_r = r + dr
            new_c = c + dc
            while (0 <= new_r < 8 and 0 <= new_c < 8):
                target = board[new_r][new_c]
                if(target is None):
                    valid_moves.append((new_r,new_c))

                elif(target.color != self.color):
                    valid_moves.append((new_r,new_c))
                    break
                
                else:
                    break

                new_r += dr
                new_c += dc
        return valid_moves

class Bishop(Piece):
    def get_valid_moves(self,board):
        (r,c)=self.position
        valid_moves=[]
        direction=[(1,1),(-1,1),(1,-1),(-1,-1)]
        for dr,dc in direction:
            new_row = r + dr
            new_col = c + dc
            while (0 <= new_row < 8 and 0 <= new_col < 8):
                target = board [new_row][new_col]
                if(target is None):
                    valid_moves.append((new_row,new_col))
                elif(target.color != self.color):
                    valid_moves.append((new_row,new_col))
                    break
                else:
                    break
                
                new_row += dr
                new_col += dc
        
        return(valid_moves)

class Knight(Piece):
    def get_valid_moves(self,board):
        (r,c) = self.position 
        valid_moves=[]
        direction=[(2,1),(-2,1),(2,-1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
        for dr,dc in direction:
            new_r = r + dr
            new_c = c + dc

            if(0 <= new_r < 8 and 0 <= new_c < 8):
                target = board[new_r][new_c]

                if(target is None):
                    valid_moves.append((new_r , new_c))

                elif(target.color != self.color):
                    valid_moves.append((new_r , new_c))

        return valid_moves

class Queen(Piece):
    def get_valid_moves(self,board):
        (r,c) = self.position 
        valid_moves=[]
        direction=[(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]
        for dr,dc in direction:
            new_r = r + dr
            new_c = c + dc

            while (0 <= new_r < 8 and 0 <= new_c < 8):
                target = board[new_r][new_c]

                if(target is None):
                    valid_moves.append((new_r , new_c))
                elif (target.color != self.color):
                    valid_moves.append((new_r , new_c))
                    break
                else:
                    break

                new_r += dr
                new_c += dc

        return valid_moves


class King(Piece):
    def get_valid_moves(self,board):
        (r,c) = self.position
        valid_moves = []
        directions=[(1,1),(1,-1),(-1,1),(-1,-1),(0,1),(0,-1),(1,0),(-1,0)]
        for dr,dc in directions:
            new_r = r + dr
            new_c = c + dc
            if(0 <= new_r < 8 and 0 <= new_c < 8):
                target = board[new_r][new_c]
                if(target is None):
                    valid_moves.append((new_r,new_c))
                elif(target.color != self.color):
                    valid_moves.append((new_r,new_c))

        if self.has_moved is False:

            row,col = self.position
            rook = board[row][7]
            if(rook is not None and rook.piece_type == "Rook" and rook.has_moved is False and self.color == rook.color):
                if(board[row][5] is None and board[row][6] is None and not is_check(board,self.color) and not is_square_attacked(board,(row,5),"Black" if self.color == "White" else "White") and not is_square_attacked(board,(row,6),"Black" if self.color == "White" else "White")):
                    valid_moves.append((row,6))

            rook = board[row][0]
            if(rook is not None and rook.piece_type == "Rook" and rook.has_moved == False and self.color == rook.color):
                if(board[row][1] is None and board[row][2] is None and board[row][3] is None and not is_check(board,self.color) and not is_square_attacked(board,(row,3),"Black" if self.color == "White" else "White") and not is_square_attacked(board,(row,2),"Black" if self.color == "White" else "White")):
                    valid_moves.append((row,2))
                
        return valid_moves


def find_king(board,color):
    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            if piece is not None:
                if piece.piece_type == "King"  and piece.color==color:
                    return (row,column)
    return None

def is_square_attacked(board,position,color):
    for row in range(8):
        for column in range(8):
            piece = board[row][column]
            if piece is not None:
                if piece.color == color:
                    if piece.piece_type == "Pawn":
                        if(piece.color == "White"):
                            direction = -1
                        else:
                            direction = 1

                        attack_row = row + direction
                        attack_squares = [(attack_row,column-1),(attack_row,column+1)]
                        if position in attack_squares:
                            return True
                    else:
                        moves=piece.get_valid_moves(board)
                        if position in moves:
                            return True
    return False


def is_check(board,color):
    king_place = find_king(board,color)
    if king_place is None:
        return False
    opponent_color = "Black" if color == "White" else "White"

    return (is_square_attacked(board,king_place,opponent_color))



def get_legal_moves(board,piece):
    legal_moves = []

    old_row,old_col = piece.position
    color = piece.color

    for move in piece.get_valid_moves(board):
        new_row,new_col = move
        captured_piece = board[new_row][new_col]

        if captured_piece is not None and captured_piece == "King" :
            continue

        old_position = piece.position
        old_has_moved = piece.has_moved

        en_passant = (piece.piece_type == "Pawn" and old_col != new_col and captured_piece is None)
        en_passant_piece = None
        if en_passant:
            en_passant_piece = board[old_row][new_col]
            board[old_row][new_col] = None
        
        board[old_row][old_col] = None
        board[new_row][new_col] = piece
        piece.position = move
        piece.has_moved = True

        rook = None
        rook_old_col = None
        rook_new_col = None
        rook_old_position = None

        if(piece.piece_type == "King" and abs(new_col - old_col) == 2):
            if(new_col > old_col):
                rook_old_col = 7
                rook_new_col = 5

            else:
                rook_old_col = 0
                rook_new_col = 3
            
            rook = board[old_row][rook_old_col]
            if rook is not None:
                rook_old_position = rook.position
                board[new_row][rook_new_col] = rook
                board[new_row][rook_old_col] = None

            rook.position = (new_row,rook_new_col)

        still_in_check = is_check(board,color)

        if rook is not None:
            board[new_row][rook_old_col] = rook
            board[new_row][rook_new_col] = None
            rook.position = (new_row , rook_old_col)

        board[old_row][old_col] = piece
        board[new_row][new_col] = captured_piece
        piece.position = old_position
        piece.has_moved = old_has_moved

        if en_passant:
            board[old_row][new_col] = en_passant_piece

        if not still_in_check:
            legal_moves.append(move)
        
    return legal_moves


def has_legal_moves(board,color):
    for row in range(8):
        for column in range(8):
            piece = board[row][column]

            if piece is not None and piece.color == color:
                if get_legal_moves(board,piece):
                    return True

    return False

def is_checkmate(board,color):
    return (is_check(board,color) and not has_legal_moves(board,color))

def is_stalemate(board,color):
    return (not is_check(board,color) and not has_legal_moves(board,color))