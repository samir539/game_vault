import math
from game_functions import make_pieces

nums_to_letters = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h"}

class Board:
    def __init__(self,pieces_white:list,pieces_black:list):
        self._pieces_white = pieces_white
        self._pieces_black = pieces_black
        
        
        
    def move(self):
        #move piece, if piece captures another remove captured piece
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
    