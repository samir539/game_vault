
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
    
    white_pieces = {}
    black_pieces = {}
    
    #add pawns
    for i in board_width:
        white_pieces[f"{i}{pawn_row_list[0]}"] = Pawn("white",f"{i}{pawn_row_list[0]}",True)
        black_pieces[f"{i}{pawn_row_list[1]}"] = Pawn("black",f"{i}{pawn_row_list[1]}",True)
        
    #add rooks
    for i in rook_starting_files:
        white_pieces[f"{i}{starting_row_list[0]}"] = Rook("white",f"{i}{starting_row_list[0]}",True)
        black_pieces[f"{i}{starting_row_list[1]}"] = Rook("white",f"{i}{starting_row_list[1]}",True)
        
    #add knights
    for i in knight_starting_files:
        white_pieces[f"{i}{starting_row_list[0]}"] = Knight("white",f"{i}{starting_row_list[0]}",True)
        black_pieces[f"{i}{starting_row_list[1]}"] = Knight("white",f"{i}{starting_row_list[1]}",True)
      
    #add bishops
    for i in bishop_starting_files:
        white_pieces[f"{i}{starting_row_list[0]}"] = Bishop("white",f"{i}{starting_row_list[0]}",True)
        black_pieces[f"{i}{starting_row_list[1]}"] = Bishop("white",f"{i}{starting_row_list[1]}",True)  
        
    #add queens
    white_pieces[f"d{starting_row_list[0]}"]  = Queen("white",f"d{starting_row_list[0]}",True)
    black_pieces[f"d{starting_row_list[1]}"] = Queen("black",f"d{starting_row_list[1]}",True)
    
    #add kings
    white_pieces[f"e{starting_row_list[0]}"] = King("white",f"e{starting_row_list[0]}",True)
    black_pieces[f"e{starting_row_list[1]}"] = King("black",f"e{starting_row_list[1]}",True)
    
    return white_pieces,black_pieces

if __name__ == "__main__":
    a,b = make_pieces()
    print(a)
    
    print(a["f1"])