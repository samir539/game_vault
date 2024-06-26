import math
from game_functions import make_pieces, format_of_move_valid
import sys
import codecs

# Setting the output encoding to UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, 'strict')
nums_to_letters = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}

#white 1
#black

class Board:
    def __init__(self,pieces_white:list,pieces_black:list):
        self._pieces_white = pieces_white
        self._pieces_black = pieces_black
        
    
    @property
    def pieces_white(self):
        return self._pieces_white
    
    @property
    def pieces_balck(self):
        return self._pieces_black        
    
    def _check_valid_piece(self,given_move,player_turn):
        """
        private method (not static since we need instance specific data)
        0.) check if input has correct format
        1.) check requested piece is on the board
        2.) check requested piece is the correct colour
        3.) check if moving requested piece opens up a check 
        """    
        query_valid = True if format_of_move_valid(given_move) else False
        if player_turn == 1:
            piece_on_board = True if given_move[-2:] in self._pieces_white else False
        else:
            piece_on_board = True if given_move[-2:] in self._pieces_black else False
        not_reveal_check = True #Come back to implementing this 
        
        if not_reveal_check and piece_on_board and query_valid:
            return True
        
        return False
         
        
        
    def move(self,given_move):
        """
        pulic method
        1.) use _check_valid
        2.) see is propsed move is valid from piece pov
        3.) carry out the move and update board state
        
        """
        if not self._check_valid_piece(given_move):
            return False

        
        
        #if valid ->  make move and return True
        #if not valid -> return False
        #move piece, if piece captures another remove captured piece
        #identify the piece in question
        #check it has the colour required
        #check if it can be moved (check considerations)
        pass
    
    
    def render(self):
        #render state of the board
        board = []
        for i in reversed(range(1,9)):
            row = []
            i = str(i)
            for j in range(1,9):
                if nums_to_letters[j]+i in self._pieces_white :
                    row.append(self._pieces_white[nums_to_letters[j]+i])
                elif nums_to_letters[j]+i in self._pieces_black:
                    row.append(self._pieces_black[nums_to_letters[j]+i])
                else:
                    row.append(".")
            board.append(row)
            
            #print art
            art = """
    
=====================================================================================
    _                     
    | |                    
___ | |__    ___  ___  ___ 
/ __|| '_ \  / _ \/ __|/ __|
| (__ | | | ||  __/\__ \\__ \\
\___||_| |_| \___||___/|___/
=====================================================================================
        """
        print(art)
        
        # Print board
        print("    a b c d e f g h")
        for index, row in enumerate(board, 1):
            print(f"{9 - index} | " + " ".join(str(piece) for piece in row) + f" | {9 - index}")
        print("    a b c d e f g h")
            
if __name__ == "__main__":
    white_pieces,black_pieces = make_pieces()
    myBoard = Board(white_pieces,black_pieces)
    myBoard.render()
    