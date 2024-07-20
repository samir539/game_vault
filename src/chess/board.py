import math
from game_functions import make_pieces
from support_functions import concat, format_of_move_valid
import sys
import codecs

# Setting the output encoding to UTF-8
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, 'strict')
nums_to_letters = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}
letters_to_nums = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8}


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
        start_pos, end_pos = concat(given_move[0],given_move[1]), concat(given_move[2],given_move[3])
        
        #check if input has correct format
        query_valid = True if format_of_move_valid(given_move) else False

        #check if requested piece is on the board and of the correct colour
        if player_turn == 1:
            piece_on_board = True if start_pos in self._pieces_white else False
        else:
            piece_on_board = True if start_pos in self._pieces_black else False
            
        
        #look if move reveals check
        not_reveal_check = False if self._inspect_reveal_check(start_pos,end_pos,player_turn) else True
        

        if not_reveal_check and piece_on_board and query_valid:
            return True
        
        return False
    
    def _inspect_reveal_check(self,start_pos,end_pos,player_turn) -> bool:
        #make a new state of board with proposed move and check if it opens up a check
        friendly_pieces, enemy_pieces = (self._pieces_white.deepcopy(), self._pieces_black.deepcopy()) if player_turn == 1 else (self._pieces_black.deepcopy(), self._pieces_white.deepcopy())
        #update friendly positions with proposed move
        if end_pos in enemy_pieces:
            del enemy_pieces[end_pos]
            
        #piece_to_move
        piece_to_move = friendly_pieces[start_pos]
        friendly_pieces.update_key(piece_to_move,end_pos)
        #check if the changed state leads to check on the friendly king
        if self.look_for_check(player_turn,friendly_pieces,enemy_pieces):
            return True
        else:
            return False
        
        
    
    def look_for_check(self,player_turn,friendly_pieces=None,enemy_pieces=None):
        """
        given the state of the board from a set perspective of player_turn (white or black) then we need 
        """
        # print("before look for check", self.pieces_white)
        if friendly_pieces == None and enemy_pieces == None:
            friendly_pieces, enemy_pieces = (self.pieces_white, self.pieces_black) if player_turn == 1 else (self.pieces_black, self.pieces_white)
        #get position of friendly king
        
        for pos,piece in friendly_pieces.items():
            if piece.is_king():
                king_pos = pos
        
        #see if position is in the set of postions which enemy pieces can reach
        enemy_attack_positions_set = set()
        for piece in enemy_pieces.values():
            enemy_attack_positions_set |= piece.valid_destinations(friendly_pieces,enemy_pieces)
        # print("after look for check", self.pieces_white)
        if king_pos in enemy_attack_positions_set:
            return True
        else:
            return False
             
            
        

        friendly_pieces, enemy_pieces = (white_pieces, black_pieces) if player_move == 1 else (black_pieces, white_pieces)
    
    def look_for_checkmate(self,friendly_pieces, enemy_pieces,player_turn):
        """
        give a certain players turn, check to see if the move carried out renders the oppoenent into a state of checkmate
        """
        #check all 9 surrounding squares to see if any still yield a check 
        #get pos of king
        #get surr 9 squares
        friendly_pieces_copy = friendly_pieces.copy()
        
        for pos,piece in friendly_pieces.items():
            if piece.is_king():
                king_piece, king_pos = piece, pos
        
        valid_moves_of_king = king_piece.valid_destinations(friendly_pieces,enemy_pieces)
        for valid_move in valid_moves_of_king:
            friendly_pieces_copy.update_key(king_piece,valid_move)
            if self.look_for_check(player_turn,friendly_pieces_copy,enemy_pieces):
                return True

        return False
                      


        
                
         
        
        
    def update_board(self,given_move,player_turn,simulated_update=False):
        """
        pulic method
        1.) use _check_valid
        2.) see is propsed move is valid from piece pov
        3.) carry out the move and update board state
        gives a false if the move is not possible otherwise moves the piece and makes any associated neccesasry changes and returns true
        """
        
        if simulated_update == True:
            friendly_pieces, enemy_pieces = (self.pieces_white.copy(), self.pieces_black.copy()) if player_turn == 1 else (self.pieces_black.copy(), self.pieces_white.copy())
        else:
            friendly_pieces, enemy_pieces = (self.pieces_white, self.pieces_black) if player_turn == 1 else (self.pieces_black, self.pieces_white)
        #cehck if move is valid (pieice is correct colour, on board, destination is on board)
        #check if opens up check 
        #check if end loc is in the set of potential moves 
        #if all checks pass move piece, update positions and remove pieces as neccessary
        
        # #convert given move from alphanumeric to just numeric (str -> list[int])
        # processed_move = []
        # for i in given_move:
        #     i = int(i)
        #     if i in nums_to_letters:
        #         processed_move.append(i)
        #     elif i in letters_to_nums:
                # processed_move.append(letters_to_nums[i])
        start_pos, end_pos = concat(given_move[0],given_move[1]), concat(given_move[2],given_move[3])
        
        
        piece_moved = friendly_pieces[start_pos]
        
        #check if valid move
        if not self._check_valid_piece(given_move,player_turn):
            return False

        #get the piece in question
        piece_moved = friendly_pieces[start_pos]
        
        #check if move is valid from the piece POV
        print("this is end pos",end_pos)
        print("THIS IS THE PIECE MOVED",piece_moved.position)
        print("this is desinations",piece_moved.valid_destinations(friendly_pieces,enemy_pieces))
        if end_pos not in piece_moved.valid_destinations(friendly_pieces,enemy_pieces):
            print("THIS HAPPENED")
            return False
        
        #if all these pass update position of piece and remove any neccessary pieces
        #delete pieces which are captures
        if end_pos in enemy_pieces:
            del enemy_pieces[end_pos]
            
        #move pieces
        print("this is the end pos",end_pos)
        friendly_pieces.update_key(piece_moved,end_pos)
        
        if simulated_update == True:
            return True, friendly_pieces, enemy_pieces
        else:
            
            return True 
            

            
    
    
    def render(self):
        print(self.pieces_white)
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
    