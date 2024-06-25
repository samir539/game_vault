
from pieces import AbstractChessPiece,Pawn,Rook,Knight,Bishop,Queen,King


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
        black_pieces[f"{i}{starting_row_list[1]}"] = Rook("black",f"{i}{starting_row_list[1]}",True)
        
    #add knights
    for i in knight_starting_files:
        white_pieces[f"{i}{starting_row_list[0]}"] = Knight("white",f"{i}{starting_row_list[0]}",True)
        black_pieces[f"{i}{starting_row_list[1]}"] = Knight("black",f"{i}{starting_row_list[1]}",True)
      
    #add bishops
    for i in bishop_starting_files:
        white_pieces[f"{i}{starting_row_list[0]}"] = Bishop("white",f"{i}{starting_row_list[0]}",True)
        black_pieces[f"{i}{starting_row_list[1]}"] = Bishop("black",f"{i}{starting_row_list[1]}",True)  
        
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
    
    
def format_of_move_valid(move):
    """
    check if proposed move could be valid (still does not mean it is necessarily valid)
    """
    if len(move) != 4:
        return False
    
    start_file = move[0]
    start_rank = move[1]
    end_file = move[2]
    end_rank = move[3]
    
    # check between 'a' and 'h'
    if start_file not in 'abcdefgh' or end_file not in 'abcdefgh':
        return False
    
    # check '1' and '8'
    if start_rank not in '12345678' or end_rank not in '12345678':
        return False

    return True