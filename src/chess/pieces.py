import math
from abc import ABC, abstractmethod
from game_functions import concat
chess_pieces = {
    "black_King": "♔",    
    "black_Queen": "♕",  
    "black_Rook": "♖",   
    "black_Bishop": "♗",  
    "black_Knight": "♘",
    "black_Pawn": "♙",   
    "white_King": "♚",   
    "white_Queen": "♛",   
    "white_Rook": "♜",    
    "white_Bishop": "♝",  
    "white_Knight": "♞",  
    "white_Pawn": "♟"     
}



class AbstractChessPiece(ABC):
    def __init__(self,colour:str,position:int,active_status:bool):
        self._colour = colour
        self._position = position
        self._active_status = active_status
    
    def __str__(self):
        return chess_pieces[self._colour + "_" + self.__class__.__name__]
    
    @abstractmethod
    def move(self):
        pass
    
    @property
    def colour(self):
        return self._colour
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self,new_pos):
        self._position = new_pos
        
    @property
    def active_status(self):
        return self._active_status
    
    @staticmethod
    def check_pos_on_board(pos:int):
        pos_list = [int(x) for x in str(pos)]
        for cord in pos_list:
            if cord > 8 or cord < 1:
                return False
        return True        
        
        

class Pawn(AbstractChessPiece):
    def __init__(self,colour:str,position:int,active_status:bool):
        super().__init__(colour,position,active_status)
    

    def move(self,white_pieces:list, black_pieces:list, start_position:int, given_end_position:int):
        """
        compute valid moves
        check if end_position is in list of valid moves
        """
        valid_end_pos = set()
        possible_dirs = {"attack_left":[1,-1],"move_forward":[0,1],"attack_right":[1,1]} #diag left, forward , diag right
        start_pos_list = [int(x) for x in str(start_position)]
        
        
        #attack left
        end_pos = [a+b for a,b in zip(possible_dirs["attack_left"],start_pos_list)]
        if (self.check_pos_on_board(end_pos)) and (end_pos in black_pieces if self._colour == "white" else end_pos in white_pieces):
            valid_end_pos.add(end_pos)
            
        #attack right
        end_pos = [a+b for a,b in zip(possible_dirs["attack_right"],start_pos_list)]
        if (self.check_pos_on_board(end_pos)) and (end_pos in black_pieces if self._colour == "white" else end_pos in white_pieces):
            valid_end_pos.add(end_pos)
        
        #move forward
        end_pos = [a+b for a,b in zip(possible_dirs["move_forward"],start_pos_list)]
        if (self.check_pos_on_board(end_pos)) and (end_pos not in (black_pieces or white_pieces)):
            valid_end_pos.add(end_pos)
            
        if given_end_position in valid_end_pos:
            return True
        else:
            return False
        

        
    

        

class Rook(AbstractChessPiece):
    def __init__(self,colour:str,position:int,active_status:bool):
        super().__init__(colour,position,active_status)
        
    def move(self,white_pieces:list, black_pieces:list, start_position:str, end_position:str):
        pass

class Knight(AbstractChessPiece):
    def __init__(self,colour:str,position:int,active_status:bool):
        super().__init__(colour,position,active_status)
        
    def move(self,white_pieces:list, black_pieces:list, start_position:str, end_position:str):
        pass

class Bishop(AbstractChessPiece):
    def __init__(self,colour:str,position:int,active_status:bool):
        super().__init__(colour,position,active_status)
        
    def move(self,white_pieces:list, black_pieces:list, start_position:str, end_position:str):
        pass

class Queen(AbstractChessPiece):
    def __init__(self,colour:str,position:int,active_status:bool):
        super().__init__(colour,position,active_status)
        
    def move(self,white_pieces:list, black_pieces:list, start_position:str, end_position:str):
        pass

class King(AbstractChessPiece):
    def __init__(self,colour:str,position:int,active_status:bool):
        super().__init__(colour,position,active_status)
        
    def move(self,white_pieces:list, black_pieces:list, start_position:str, end_position:str):
        pass




if __name__ == "__main__":
    
    pawn1 = Pawn("white","a1",True)
    print(pawn1.active_status,pawn1.colour,pawn1.position)
    print(pawn1)
    rook1 = Rook("black","b2",True)
    print(rook1)
