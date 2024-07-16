import math
from game_functions import make_pieces, format_of_move_valid, concat
import sys
import codecs

# Setting the output encoding to UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, 'strict')
nums_to_letters = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}

#white 1
#black 0

class Board:
    def __init__(self,pieces_white:list,pieces_black:list):
        self._pieces_white = pieces_white
        self._pieces_black = pieces_black
        self._target_pieces = lambda player_turn: self._pieces_black if player_turn else self._pieces_white
        
    
    @property
    def pieces_white(self):
        return self._pieces_white
    
    @property
    def pieces_black(self):
        return self._pieces_black        
    
    def _check_valid_piece(self,given_move,player_turn):
        """
        private method (not static since we need instance specific data)
        0.) check if input has correct format
        1.) check requested piece is on the board
        2.) check requested piece is the correct colour
        3.) check if moving requested piece opens up a check 
        """    
        #check if input has correct format
        query_valid = True if format_of_move_valid(given_move) else False

        #check if requested piece is on the board and of the correct colour
        if player_turn == 1:
            piece_on_board = True if given_move[-2:] in self._pieces_white else False
        else:
            piece_on_board = True if given_move[-2:] in self._pieces_black else False
        
        #look if move reveals check
        not_reveal_check = True #Come back to implementing this 
        
        #check if move end location is on a same coloured piece
        

        #valid check
        if not_reveal_check and piece_on_board and query_valid:
            return True
        
        return False
    
    def _look_for_check(self):
        pass
    
    def _look_for_checkmate(self,player_turn):
        """
        give a certain players turn, check to see if the move carried out renders the oppoenent into a state of checkmate
        """
        #check all 9 surrounding squares to see if any still yield a check 
        #get pos of king
        #get surr 9 squares
        def get_king_pos():
            for i in self._target_pieces(player_turn).values():
                print(i)
            for pos,piece in self._target_pieces(player_turn).items():
                if piece.is_king():
                    return pos
                
        king_pos = get_king_pos()
        print(king_pos,type(king_pos),list(king_pos))
        surr_grid = [[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]]
        
                
        
         
        
        
    def update_board(self,given_move,player_turn):
        """
        pulic method
        1.) use _check_valid
        2.) see is propsed move is valid from piece pov
        3.) carry out the move and update board state
        gives a false if the move is not possible otherwise moves the piece and makes any associated neccesasry changes
        """
        #check if valid move
        if not self._check_valid_piece(given_move,player_turn):
            return False

        #get the piece in question
        piece = self._pieces_white[given_move[:2]] if player_turn  else self._pieces_black[given_move[:2]]
        
        #check if move is valid from the piece POV
        if not piece.move(self.pieces_white,self.pieces_black,start_position=given_move[:2],end_position=given_move[-2:]):
            return False
        else:
            
            #check if move is a capture move 
            capture = False
            if player_turn:
                if given_move[-2:] in self._pieces_black:
                    capture = True
            else:
                if given_move[-2:] in self._pieces_white:
                    capture = True
            
            #delete captured piece from board
            if capture == True:
                del self._target_pieces(player_turn)[given_move[-2:]]

            #move piece to end location
            self._target_pieces(player_turn)[given_move[-2:]] = self._target_pieces(player_turn).pop(given_move[:2])
            
            #look to see if new move renders checkmate

            #look to see if new move renders check
            
            

            
    
    
    def render(self):
        #render state of the board
        board = []
        for i in reversed(range(1,9)):
            row = []
            i = str(i)
            for j in range(1,9):
                if concat(i,j) in self._pieces_white :
                    row.append(self._pieces_white[concat(i,j)])
                elif concat(i,j) in self._pieces_black:
                    row.append(self._pieces_black[concat(i,j)])
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
    print(myBoard._target_pieces(1))
    myBoard._look_for_checkmate(1)
    # myBoard.render()
    