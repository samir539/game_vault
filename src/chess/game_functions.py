
from pieces import AbstractChessPiece,Pawn,Rook,Knight,Bishop,Queen,King
import sys
import codecs
from support_functions import DynamicKeyDict
# Setting the output encoding to UTF-8
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, 'strict')

def concat(a,b):
    """
    function to concatenate two integers 8,9 -> 89
    """
    return int(f"{a}{b}")

def make_pieces():
    """
    make pieces 
    """
    # board_width = ["a","b","c","d","e","f","g","h"]
    board_width = [i for i in range(1,9)]
    starting_row_list = [1,8]
    pawn_row_list = [2,7]
    
    rook_starting_files = [1,8]
    bishop_starting_files = [3,6]
    knight_starting_files = [2,7]
    queen_starting_file = 4
    king_starting_file = 5
    
    white_pieces = DynamicKeyDict()
    black_pieces = DynamicKeyDict()
    
    #add pawns
    for i in board_width:
        white_pieces.add(Pawn("white",concat(pawn_row_list[0],i),True)) 
        black_pieces.add(Pawn("black",concat(pawn_row_list[1],i),True)) 
        

        
    #add rooks
    for i in rook_starting_files:
        white_pieces.add(Rook("white",concat(starting_row_list[0],i),True))  
        black_pieces.add(Rook("black",concat(starting_row_list[1],i),True)) 
        
    #add knights
    for i in knight_starting_files:
        white_pieces.add(Knight("white",concat(starting_row_list[0],i),True))  
        black_pieces.add(Knight("black",concat(starting_row_list[1],i),True)) 
      
    #add bishops
    for i in bishop_starting_files:
        white_pieces.add(Bishop("white",concat(starting_row_list[0],i),True)) 
        black_pieces.add(Bishop("black",concat(starting_row_list[1],i),True))
        
    #add queens
    white_pieces.add(Queen("white",concat(starting_row_list[0],queen_starting_file),True)) 
    black_pieces.add(Queen("black",concat(starting_row_list[1],queen_starting_file),True))  
    
    #add kings
    white_pieces.add(King("white",concat(starting_row_list[0],king_starting_file),True)) 
    black_pieces.add(King("black",concat(starting_row_list[1],king_starting_file),True)) 
    
    return white_pieces,black_pieces


    

    
    

if __name__ == "__main__":
    a,b = make_pieces()
    print(a)
    print(b)
