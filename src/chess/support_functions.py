
def concat(a,b):
    """
    function to concatenate two integers 8,9 -> 89
    """
    return int(f"{a}{b}")


def de_con_cat(position:int) -> list[int]:
    """
    helper function to deconcatenate a position back into a list of two integers representing the positon of a piece on the board
    """
    #could use mod method but this is easier to read
    pos_list = [int(x) for x in str(position)]
    return pos_list
    

def check_in_bounds(position_as_list: list[int]) -> bool:
    """
    helper function to check if proposed position is indeed on the board
    param position_as_list: the position as a list of integers
    """
    for i in position_as_list:
        if i < 1 or i > 8:
            return False
    return True

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

