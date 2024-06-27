
from pieces import AbstractChessPiece,Pawn,Rook,Knight,Bishop,Queen,King
import sys
import codecs

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
    
    white_pieces = {}
    black_pieces = {}
    
    #add pawns
    for i in board_width:
        white_pieces[concat(pawn_row_list[0],i)] = Pawn("white",concat(pawn_row_list[0],i),True)
        black_pieces[concat(pawn_row_list[1],i)] = Pawn("black",concat(pawn_row_list[1],i),True)
        
    #add rooks
    for i in rook_starting_files:
        white_pieces[concat(starting_row_list[0],i)] = Rook("white",concat(starting_row_list[0],i),True)
        black_pieces[concat(starting_row_list[1],i)] = Rook("black",concat(starting_row_list[1],i),True)
        
    #add knights
    for i in knight_starting_files:
        white_pieces[concat(starting_row_list[0],i)] = Knight("white",concat(starting_row_list[0],i),True)
        black_pieces[concat(starting_row_list[1],i)] = Knight("black",concat(starting_row_list[1],i),True)
      
    #add bishops
    for i in bishop_starting_files:
        white_pieces[concat(starting_row_list[0],i)] = Bishop("white",concat(starting_row_list[0],i),True)
        black_pieces[concat(starting_row_list[1],i)] = Bishop("black",concat(starting_row_list[1],i),True)  
        
    #add queens
    white_pieces[concat(starting_row_list[0],queen_starting_file)]  = Queen("white",concat(starting_row_list[0],queen_starting_file),True)
    black_pieces[concat(starting_row_list[1],queen_starting_file)] = Queen("black",concat(starting_row_list[1],queen_starting_file),True)
    
    #add kings
    white_pieces[concat(starting_row_list[0],king_starting_file)] = King("white",concat(starting_row_list[0],king_starting_file),True)
    black_pieces[concat(starting_row_list[1],king_starting_file)] = King("black",concat(starting_row_list[1],king_starting_file),True)
    
    return white_pieces,black_pieces

if __name__ == "__main__":
    a,b = make_pieces()
    print(a)
    print(b)
    print(type(concat(1,2)))
    print(a[11])
    
    
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