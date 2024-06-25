
from pieces import AbstractChessPiece,Pawn,Rook,Knight,Bishop,Queen,King
from board import Board

def make_pieces():
    """
    make pieces 
    """
    board_width = ["a","b","c","d","e","f","g","h"]
    starting_row_list = [1,8]
    pawn_row_list = [2,7]
    
    rook_starting_files = ["a","h"]
    bishop_starting_files = ["c","f"]
    knight_starting_files = ["b","g"]
    
    white_pieces = []
    black_pieces = []
    
    #add pawns
    for i in board_width:
        white_pieces.append(Pawn("white",f"{i}{pawn_row_list[0]}",True))
        black_pieces.append(Pawn("black",f"{i}{pawn_row_list[1]}",True))
        
    #add rooks
    for i in rook_starting_files:
        white_pieces.append(Rook("white",f"{i}{starting_row_list[0]}",True))
        black_pieces.append(Rook("white",f"{i}{starting_row_list[1]}",True))
        
    #add knights
    for i in knight_starting_files:
        white_pieces.append(Knight("white",f"{i}{starting_row_list[0]}",True))
        black_pieces.append(Knight("white",f"{i}{starting_row_list[1]}",True))
      
    #add bishops
    for i in bishop_starting_files:
        white_pieces.append(Bishop("white",f"{i}{starting_row_list[0]}",True))
        black_pieces.append(Bishop("white",f"{i}{starting_row_list[1]}",True))  
        
    #add queens
    white_pieces.append(Queen("white",f"d{starting_row_list[0]}",True))
    black_pieces.append(Queen("black",f"d{starting_row_list[1]}",True))
    
    #add kings
    white_pieces.append(King("white",f"e{starting_row_list[0]}",True))
    black_pieces.append(King("black",f"e{starting_row_list[1]}",True))
    
    return white_pieces,black_pieces